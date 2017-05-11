import os.path as path
from itertools import combinations

from team import Team
import ballpark as bp
import player
import baseball_lookups as bl
import draftable_object as do
import sql


class Draft:
    def __init__(self):
        self.draft_name = 'Draft'
        self.number_of_teams = 12
        self.number_of_rounds = 26
        self.player_set = "1911_players"
        self.ballpark_set = '1911_ballparks'
        self.draftable_object_list = []
        self.type = "tournament"
        self.style = "serpentine"
        self.choose_ballparks = True
        self.custom_ballparks = True
        self.league_keepers = False
        self.time_per_pick = 60

        self.teams = []
        self.main_team_index = 0
        self.main_team = None

        self.save_file = ''

        self.current_pick = 0
        self.current_round = 0
        self.current_team = 0

        self.replacement_value = {
            'c': {'L': 0, 'R': 0},
            '1b': {'L': 0, 'R': 0},
            '2b': {'L': 0, 'R': 0},
            '3b': {'L': 0, 'R': 0},
            'ss': {'L': 0, 'R': 0},
            'lf': {'L': 0, 'R': 0},
            'cf': {'L': 0, 'R': 0},
            'rf': {'L': 0, 'R': 0},
        }

# draft set up region
    # functions used for setup of draft
    def change_name_of_draft(self, name):
        self.draft_name = name

    def change_number_of_teams(self, teams):
        self.number_of_teams = teams

    def change_number_of_rounds(self, rounds):
        self.number_of_rounds = rounds

    def change_player_set(self, player_list):
        self.player_set = player_list

    def change_ballpark_set(self, bp_list):
        self.ballpark_set = bp_list

    def change_draft_type(self):
        if self.type == "tournament":
            self.type = "league"
        elif self.type == "league":
            self.type = "tournament"
        else:
            raise ValueError("Invalid value for draft type.")

    def toggle_choose_ballparks(self):
        if self.choose_ballparks:
            self.choose_ballparks = False
        elif not self.choose_ballparks:
            self.choose_ballparks = True

    def toggle_league_keepers(self):
        if self.league_keepers:
            self.league_keepers = False
        elif not self.league_keepers:
            self.league_keepers = True

    def adjust_time_per_pick(self, time):
        self.time_per_pick = time

    def change_draft_style(self):
        if self.style == "serpentine":
            self.style = "straight"
        elif self.style == "straight":
            self.style = "serpentine"
        else:
            raise ValueError("Invalid value for draft style.")

    def assign_team_names(self, team_names):
        for i in range(len(team_names)):
            self.teams[i].change_name(team_names[i])
        self.main_team = self.teams[self.main_team_index]

    def change_main_team(self, new_index):
        self.main_team_index = new_index
        self.main_team = self.teams[self.main_team_index]

    @staticmethod
    def get_draft_indices(players):
        hitters = 0
        pitchers = 0
        double_duty = 0
        for p in players:
            if p[1] == 'H':
                hitters += 1
            elif p[1] == 'P':
                pitchers += 1
            elif p[1] == 'X':
                double_duty += 1
        hitter_index = 1
        pitcher_index = 501
        double_duty_index = 901
        ballpark_index = 1001
        if hitters > 500:
            pitcher_index = (hitters // 100) * 100 + 101
        if double_duty > 0:
            if pitcher_index + pitchers > 900:
                double_duty_index = ((pitchers + pitcher_index) // 100) * 100 + 101
        else:
            double_duty_index = ((pitchers + pitcher_index) // 100) * 100 + 101
        if double_duty_index != 901:
            ballpark_index = ((double_duty + double_duty_index) // 100) * 100 + 101
        if ballpark_index < 1001:
            ballpark_index = 1001
        return hitter_index, pitcher_index, double_duty_index, ballpark_index

    def load_draftable_objects(self):
        # get list of draftable_objects
        player_list = player.open_player_list(self.player_set)
        player_list_with_type = []
        for p in player_list:
            common_data = sql.get_player_data(p)
            player_list_with_type.append([p, common_data[4]])
        ballpark_list = bp.open_ballpark_list(self.ballpark_set, self.custom_ballparks)
        # determine draft_indices
        hitter_index, pitcher_index, double_duty_index, ballpark_index = \
            self.get_draft_indices(player_list)
        # create draftable objects list
        for p in player_list_with_type:
            if p[1] == 'H':
                self.draftable_object_list.append(do.DraftableObject(p[0], hitter_index, 'H'))
                hitter_index += 1
            elif p[1] == 'P':
                self.draftable_object_list.append(do.DraftableObject(p[0], pitcher_index, 'P'))
                pitcher_index += 1
            elif p[1] == "X":
                self.draftable_object_list.append(do.DraftableObject(p[0], double_duty_index, 'X'))
                double_duty_index += 1
        for b in ballpark_list:
            self.draftable_object_list.append(do.DraftableObject(b, ballpark_index, 'B'))
            ballpark_index += 1

    def setup_teams(self):
        for i in range(self.number_of_teams):
            self.teams.append(Team('Team #{}'.format(i+1)))
            self.teams[i].suggested_park = 'AVG'

    def compile_ballpark_stats(self):
        hitters = [x for x in self.draftable_object_list if x.object_type == 'H']
        pitchers = [x for x in self.draftable_object_list if x.object_type == 'P']
        ballparks = [x for x in self.draftable_object_list if x.object_type == 'B']
        for h in hitters:
            for b in ballparks:
                h.dft_object.add_hitting_stat_line(b.dft_object.ballpark_id, b.dft_object)
        for p in pitchers:
            for b in ballparks:
                p.dft_object.add_pitching_stat_line(b.dft_object.ballpark_id, b.dft_object)

    def create_replacement_values(self, ranking, ballpark):
        for s in ['L', 'R']:
            for pos in ranking:
                player_list = ranking[pos][s][:self.number_of_teams]
                values = [x.dft_object.hitting_stat_lines[ballpark].
                          composite_stats['total_ratings'][pos][s] for x in player_list]
                self.replacement_value[pos][s] = min(values)

    def get_hitters_for_position_list(self, team, ballpark):
        hitters = [x for x in self.draftable_object_list if
                   x.object_type == 'H' or x.object_type == 'X']
        if team != 0:
            hitters = [x for x in hitters if x.team == team]
        i = 0
        while len(hitters) < 10:
            h = do.DraftableObject('blank{}'.format(i), 9999-i, 'H')
            h.dft_object.add_hitting_stat_line(ballpark, bp.Ballpark())
            h.team = team
            hitters.append(h)
            i += 1
        return hitters

    @staticmethod
    def adjust_forced_rankings(ranking):
        for s in ['L', 'R']:
            for pos in ranking:
                test_list = [x for x in ranking[pos][s] if
                             'x{}{}'.format(bl.get_position_int_from_string(pos),s) in x.position]
                for x in ranking[pos][s]:
                    if 'x' not in x.position:
                        x.position = ''
                if len(test_list) == 1:
                    # move to top
                    find_index = ranking[pos][s].index(test_list[0])
                    ranking[pos][s] = ranking[pos][s].insert(ranking[pos][s].pop(find_index), 0)
                elif len(test_list) > 1:
                    print('Multiple players attempted to be forced into lineup.')
                    print('All players have had their forced to play removed.')
                    for x in test_list:
                        print('   ', x.dft_object.full_name)
                        x.position = ''
                    pass
        return ranking

    @staticmethod
    def force_into_lineup(player_, force_type, position):
        if force_type == 'L':
            player_.position = 'xL' + str(position)
        elif force_type == 'R':
            player_.position = 'xR' + str(position)
        elif force_type == 'LR':
            player_.position = 'xL{0} xR{1}'.format(position)
        return player_

    def organize_position_list(self, team, ballpark):
        hitters = self.get_hitters_for_position_list(team, ballpark)
        ranking = {
            'c': {'L': [x for x in hitters if 'c-' in x.dft_object.defense_string],
                  'R': [x for x in hitters if 'c-' in x.dft_object.defense_string]},
            '1b': {'L': [x for x in hitters if '1b' in x.dft_object.defense_string],
                   'R': [x for x in hitters if '1b' in x.dft_object.defense_string]},
            '2b': {'L': [x for x in hitters if '2b' in x.dft_object.defense_string],
                   'R': [x for x in hitters if '2b' in x.dft_object.defense_string]},
            '3b': {'L': [x for x in hitters if '3b' in x.dft_object.defense_string],
                   'R': [x for x in hitters if '3b' in x.dft_object.defense_string]},
            'ss': {'L': [x for x in hitters if 'ss' in x.dft_object.defense_string],
                   'R': [x for x in hitters if 'ss' in x.dft_object.defense_string]},
            'lf': {'L': [x for x in hitters if 'lf' in x.dft_object.defense_string],
                   'R': [x for x in hitters if 'lf' in x.dft_object.defense_string]},
            'cf': {'L': [x for x in hitters if 'cf' in x.dft_object.defense_string],
                   'R': [x for x in hitters if 'cf' in x.dft_object.defense_string]},
            'rf': {'L': [x for x in hitters if 'rf' in x.dft_object.defense_string],
                   'R': [x for x in hitters if 'rf' in x.dft_object.defense_string]},
        }
        rank_depth = 1
        if team == 0:
            rank_depth = self.number_of_teams
        for s in ['L', 'R']:
            for pos in ranking:
                ranking[pos][s].sort(key=lambda x: x.dft_object.hitting_stat_lines[ballpark].
                                     composite_stats['total_ratings'][pos][s], reverse=True)
        # move players to top if forced into lineup
        if team != 0:
            ranking = self.adjust_forced_rankings(ranking)
        compare_list = list(combinations(['c', '1b', '2b', '3b', 'ss', 'lf', 'cf', 'rf'], 2))
        duplicates = True
        while duplicates:
            duplicates = False
            for s in ['L', 'R']:
                for pos in compare_list:
                    for i in range(rank_depth):
                        for j in range(rank_depth):
                            if ranking[pos[0]][s][i].dft_object == ranking[pos[1]][s][j].dft_object:
                                if '{}{}x'.format(bl.get_position_int_from_string(pos[0]), s) in \
                                        ranking[pos[0]][s][i].position:
                                    ranking[pos[1]][s].pop(j)
                                elif '{}{}x'.format(bl.get_position_int_from_string(pos[1]), s) in \
                                        ranking[pos[1]][s][j].position:
                                    ranking[pos[0]][s].pop(i)
                                else:
                                    change_position_1 = ranking[pos[0]][s][i].dft_object.hitting_stat_lines \
                                        [ballpark].composite_stats['total_ratings'][pos[0]][s] + \
                                        ranking[pos[1]][s][rank_depth].dft_object.hitting_stat_lines[ballpark]. \
                                        composite_stats['total_ratings'][pos[1]][s]
                                    change_position_2 = ranking[pos[1]][s][j].dft_object.hitting_stat_lines \
                                        [ballpark].composite_stats['total_ratings'][pos[1]][s] + \
                                        ranking[pos[0]][s][rank_depth].dft_object.hitting_stat_lines[ballpark]. \
                                        composite_stats['total_ratings'][pos[0]][s]
                                    if change_position_1 > change_position_2:
                                        ranking[pos[1]][s].pop(j)
                                    else:
                                        ranking[pos[0]][s].pop(i)
                                duplicates = True
        for s in ['L', 'R']:
            for pos in ranking:
                for i in range(rank_depth):
                    if '{}{}'.format(bl.get_position_int_from_string(pos), s) not in ranking[pos][s][i].position:
                        ranking[pos][s][i].position += ' {}{}'.format(bl.get_position_int_from_string(pos), s)
        if team == 0:
            self.create_replacement_values(ranking, ballpark)
        else:
            self.generate_team_values(team - 1, ranking, ballpark)
        # for s in ['L', 'R']:
        #     for pos in ranking:
        #         print(pos, s)
        #         for x in ranking[pos][s]:
        #             if x.dft_object.hitting_stat_lines[ballpark].composite_stats['total_ratings'][pos][s] >= \
        #                     self.replacement_value[pos][s]:
        #                 print('{:20}   {:5.1f}'.format(x.dft_object.full_name[:20],
        #                                                x.dft_object.hitting_stat_lines['AVG'].
        #                                                composite_stats['total_ratings'][pos][s]))

    def generate_team_values(self, team_index, ranking, ballpark):
        team_values = {
            'c': {'L': 0, 'R': 0},
            '1b': {'L': 0, 'R': 0},
            '2b': {'L': 0, 'R': 0},
            '3b': {'L': 0, 'R': 0},
            'ss': {'L': 0, 'R': 0},
            'lf': {'L': 0, 'R': 0},
            'cf': {'L': 0, 'R': 0},
            'rf': {'L': 0, 'R': 0},
        }
        for s in ['L', 'R']:
            for pos in team_values:
                team_values[pos][s] = ranking[pos][s][0].dft_object.hitting_stat_lines \
                                        [ballpark].composite_stats['total_ratings'][pos][s]
        self.teams[team_index].update_team_values(team_values)

    # functions used during draft
    def generate_pick_values(self, team, ballpark):
        undrafted_players = [x for x in self.draftable_object_list if x.drafted]
        current_team_values = {
            'sp': [0, 0, 0, 0],
            'rp': [0, 0, 0, 0, 0],
            'c': {'L': 0, 'R': 0},
            '1b': {'L': 0, 'R': 0},
            '2b': {'L': 0, 'R': 0},
            '3b': {'L': 0, 'R': 0},
            'ss': {'L': 0, 'R': 0},
            'lf': {'L': 0, 'R': 0},
            'cf': {'L': 0, 'R': 0},
            'rf': {'L': 0, 'R': 0}
        }
        roster = [x for x in self.draftable_object_list if x.team == team]
        self.organize_position_list(team, 1, ballpark)

    def generate_save_file_header(self):
        self.save_file = '{},{},{},{},{},{},{}\n'.format(
            self.draft_name, self.number_of_teams, self.number_of_rounds, self.player_set,
            self.ballpark_set, self.type, self.style, self.time_per_pick)
        for t in self.teams:
            self.save_file += '{},'.format(t.name)
        self.save_file = self.save_file[:-1]
        self.save_file += '\n'
        self.save_draft()

    def save_draft(self):
        file = open(path.join(path.curdir, 'save', '{}.dft'.format(self.draft_name)), 'w')
        file.write(self.save_file)
        file.close()

    def recreate_save_file(self):
        self.generate_save_file_header()
        self.draftable_object_list.sort(key=lambda x: x.pick)
        partial_list = [x for x in self.draftable_object_list if x.drafted]
        for pick in partial_list:
            pick_line = self.make_pick_line(pick)
            self.save_file += pick_line
        self.save_file()

    # todo: make a way to load a draft from a save file
    def load_saved_draft(self):
        pass

    @staticmethod
    def make_pick_line(self, pick):
        if pick.object_type == 'B':
            pick_line = '{}'.format(pick.dft_object.ballpark_id)
        else:
            pick_line = '{}'.format(pick.dft_object.player_id)
        pick_line += ',{},{},{}\n'.format(self.current_pick, self.current_team, self.current_round)
        return pick_line

    def start_draft(self):
        self.current_pick = 1
        self.current_round = 1
        self.current_team = 1
        self.generate_save_file_header()

    def update_pick_numbers(self):
        self.current_round = (self.current_pick // self.number_of_teams) + 1
        if self.current_round % 2 == 1:
            self.current_team = (self.current_pick % self.number_of_teams) + 1
        else:
            self.current_team = self.number_of_teams - (self.current_pick % self.number_of_teams)
        self.current_pick += 1

    def make_pick(self, draft_object):
        draft_object.make_pick(self.current_team, self.current_round, self.current_pick)
        if draft_object.object_type == 'B':
            self.teams[self.current_team - 1].change_ballpark(draft_object)
        else:
            self.teams[self.current_team - 1].roster.append(draft_object)
        self.update_pick_numbers()
        return self

    def remove_pick(self, draft_object):
        draft_object.remove_pick()
        self.recreate_save_file()
