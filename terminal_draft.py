from baseball_lookups import get_position_from_int, get_full_position_name_from_int, get_position_int_from_string,  pitcher_positions
from ballpark import Ballpark
import sanatize as san
from os import listdir
from os.path import isfile, join, curdir
import re


def setup_menu(dft):
    print('1-Name of Draft: {}'.format(dft.draft_name))
    print('2-Number of Teams: {}'.format(dft.number_of_teams))
    print('3-Number of Rounds: {}'.format(dft.number_of_rounds))
    print('4-Select Position in Draft for Ratings: #{}'.format(dft.main_team_index + 1))
    print('5-Time per pick (0 means timer is off): {}'.format(dft.time_per_pick))
    print('6-Player Set: {}'.format(dft.player_set))
    print('7-Ballpark Set: {}'.format(dft.ballpark_set))
    print('8-Start Draft')


# Pre Draft
def setup_draft(dft):
    while True:
        setup_menu(dft)
        # choice tree
        choice = san.sanitize_int("Make a selection: ", 1, 8)
        if choice == 1:
            name = input("Enter the name of the draft: ")
            dft.change_name_of_draft(name)
        elif choice == 2:
            teams = san.sanitize_int("Enter the number of teams: ", 2, 32)
            dft.change_number_of_teams(teams)
        elif choice == 3:
            rounds = san.sanitize_int("Enter the number of rounds: ", 1, 99)
            dft.change_number_of_rounds(rounds)
        elif choice == 4:
            main_team_index = san.sanitize_int('Enter what position you will draft in: ', 1, dft.number_of_teams) - 1
            dft.change_main_index(main_team_index)
        elif choice == 5:
            time = san.sanitize_int("Enter the number seconds allowed per pick: ", 15, 3600)
            dft.adjust_time_per_pick(time)
        elif choice == 6:
            player_list = change_player_list()
            dft.change_player_set(player_list)
        elif choice == 7:
            bp_list = change_ballpark_list()
            dft.change_ballpark_set(bp_list)
        elif choice == 8:
            break
    return dft, main_team_index


def select_team_names(dft):
    dft.setup_teams()
    team_names = []
    for i in range(dft.number_of_teams):
        team = 'Team #{}'.format(i + 1)
        team_names.append(team)
    while True:
        print("Team Names:")
        for i in range(len(team_names)):
            print('{:2}- {}'.format(i + 1, team_names[i]))
        choice = san.sanitize_int("Choose Team Name to Change (0 to end): ", 0, len(team_names))
        if choice == 0:
            break
        else:
            team_names[choice - 1] = input("Team {}: ".format(choice))
    return team_names


def change_player_list():
    player_list_path = join(curdir(), 'data', 'player_lists')
    list_choices = [f for f in listdir(player_list_path) if isfile(join(player_list_path, f))]
    for i in range(len(list_choices)):
        print('{:3}- {}'.format(i + 1, list_choices[i][:-4].replace('_', ' ').title()))
    choice = san.sanitize_int("Choose the player list you would like to use: ", 1, len(list_choices))
    return list_choices[choice - 1][:-4]


def change_ballpark_list():
    ballpark_list_path = join(curdir(), 'data', 'ballpark_lists')
    list_choices = [f for f in listdir(ballpark_list_path) if isfile(join(ballpark_list_path, f))]
    for i in range(len(list_choices)):
        print('{:3}- {}'.format(i + 1, list_choices[i][:-4].replace('_', ' ').title()))
    choice = san.sanitize_int("Choose the ballpark list you would like to use: ", 1, len(list_choices))
    return list_choices[choice - 1][:-4]


# Full Draft Displays
def full_draft_header(dft, draft_type):
    print('\n{:3}|'.format(draft_type), end='')
    width = int(140 / dft.number_of_teams)
    if width > 16:
        width = 16
    for i in range(dft.number_of_teams):
        team_display = dft.teams[i].name
        if len(team_display) > width:
            team_display = team_display[:width]
        print('{0:^{width}}|'.format(team_display, width=width), end='')
    print('{:3}'.format(draft_type))
    return width


def display_draft_by_round(dft):
    width = full_draft_header(dft, 'Rd')
    for rd in range(1, dft.current_round + 1):
        print('{:3}|'.format(rd), end='')
        # todo: enter picks here
        for pk in range(dft.number_of_teams):
            pick = [x for x in dft.draftable_object_list if rd == x.round and pk == (x.team - 1)]
            try:
                name = pick[0].dft_object.full_name
            except:
                name = ''
            if len(name) > width:
                name = name[:width]
            print('{0:<{width}}|'.format(name, width=width), end='')
        print('{:3}'.format(rd))
    print()


def display_draft_by_position(dft):
    width = full_draft_header(dft, 'Pos')
    positions = ['c', 'c', '1b', '1b', '2b', '2b', '3b', '3b', 'ss', 'ss',
                 'lf', 'lf', 'cf', 'cf', 'rf', 'rf', 'utl', 'utl', 'utl', 'utl', '---',
                 'sp1', 'sp2', 'sp3', 'sp4', 'sp5', 'lrp', 'lrp', 'lrp', 'lrp',
                 'rrp', 'rrp', 'rrp', 'rrp', 'rrp', 'rrp']
    for pos in positions:
        print('{:3}|'.format(pos), end='')
        # todo: enter players at each position here
        for pk in range(dft.number_of_teams):
            print('{0:<{width}}|'.format('', width=width), end='')
        print('{:3}'.format(pos))
    print()
    input()


def print_suggestions(dft, team_number, ballpark, players_to_display, hold):
    print('Suggestions for {}, Ballpark for ratings {}:'.format(dft.teams[team_number - 1].name, ballpark))
    pick_list = [x for x in dft.draftable_object_list if not x.drafted and x.object_type != 'B']
    team_base_values = {
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
        for pos in team_base_values:
            team_base_values[pos][s] = max(dft.replacement_value[pos][s],
                                           dft.teams[team_number-1].team_values[pos][s])
    for p in pick_list:
        if p.object_type == 'H':
            value = {'L': 0, 'R': 0}
            for s in value:
                for pos in team_base_values:
                    value[s] = max(p.dft_object.hitting_stat_lines[ballpark].
                                   composite_stats['total_ratings'][pos][s] -
                                   team_base_values[pos][s], value[s])
            pick_value = value['L'] * 0.25 + value['R'] * 0.75
            p.change_pick_value(pick_value)
    pick_list.sort(key=lambda x: x.pick_value, reverse=True)
    for i in range(players_to_display // 4):
        for j in range(4):
            plr = j * (players_to_display // 4) + i
            print('{0:3}- {1:17} {2:4.1f}   '.format(pick_list[plr].draft_id,
                                                     pick_list[plr].dft_object.full_name[:17],
                                                     pick_list[plr].pick_value), end='')
        print()
    print()
    return hold


def display_aps(dft):
    # Currently displays just the listing of all players, sorted by name
    pick_list = [x for x in dft.draftable_object_list if not x.drafted]
    pick_list.sort(key= lambda x: x.aps)
    print()
    print('Top 48 Players sorted by APS:')
    print()
    for i in range(12):
        for j in range(0, 48, 12):
            print('{:3}- {:17} {:3}  {:4.1f}   '.format(pick_list[i+j].draft_id,
                                                        pick_list[i+j].dft_object.full_name[:17],
                                                        pick_list[i+j].aps,
                                                        pick_list[i+j].pick_value), end='')
            if j >= 36:
                print()
    return True


# draft object filters
def filter_hitters_by_position(player_list, pos):
    pos_str = get_position_from_int(pos) + '-'
    hitters = [x for x in player_list if pos_str in x.dft_object.defense_string]
    return hitters


def filter_pitchers_by_position(player_list, pos):
    if pos == 'sp' or pos == 'lsp' or pos == 'rsp':
        player_list = [x for x in player_list if x.dft_object.endurance_starter > 0]
    if pos == 'rp' or pos == 'lrp' or pos == 'rrp':
        player_list = [x for x in player_list if x.dft_object.endurance_reliever > 0]
    if pos == 'lsp' or pos == 'lrp':
        player_list = [x for x in player_list if x.dft_object.arm.lower() == 'l']
    if pos == 'rsp' or pos == 'rrp':
        player_list = [x for x in player_list if x.dft_object.arm.lower() == 'r']
    return player_list


def filter_pitchers_by_starter(player_list):
    starters = [x for x in player_list if x.object_type == 'P' and x.dft_object.endurance_reliever > 0]
    return starters


def filter_relievers_by_handedness(player_list, hand):
    relief = [x for x in player_list if x.object_type == 'P' and
              x.dft_object.endurance_reliever > 0 and x.dft_object.arm.lower() == hand.lower()]
    return relief


# select a player or list of players
def make_pick_by_draft_id(dft, draft_id):
    pick = [x for x in dft.draftable_object_list if x.draft_id == draft_id and not x.drafted]
    if len(pick) == 0:
        print('No valid selections with pick id of: {}'.format(draft_id))
        input()
    elif len(pick) > 1:
        print('Multiple draft objects have the same draft id.')
        print('No Selection made.')
        print()
        print(' ID   Name')
        for p in pick:
            print('{:4}-{}'.format(p.draft_id, p.dft_object.full_name))
    elif len(pick) == 1:
        dft.make_pick(pick[0])
    return dft


def make_pick_by_name(dft, name):
    pick = [x for x in dft.draftable_object_list if x.dft_object.full_name.lower().startswith(name)]
    pick = [x for x in pick if not x.drafted]
    if len(pick) == 0:
        print("No valid selections with the string '{}'".format(name))
        input()
    elif len(pick) > 1:
        pick.sort(key=lambda x: x.dft_object.full_name)
        print("Multiple draft objects match the string '{}'.".format(name))
        print('No Selection made.')
        print()
        print(' ID   Name')
        for p in pick:
            print('{:4}- {}'.format(p.draft_id, p.dft_object.full_name))
    elif len(pick) == 1:
        dft.make_pick(pick[0])
    return dft


# Stat Displays
def hitter_stat_sort(stat, player_list, ballpark):
    str_stat = ''
    if stat == 'rt':
        stat = 'rating'
        str_stat = 'Pinch Hit Rating'
    elif stat == 'hi':
        stat = 'hits'
        str_stat = 'Hits'
    elif stat == 'ob':
        stat = 'on_base'
        str_stat = 'On Base'
    elif stat == 'tb':
        stat = 'total_bases'
        str_stat = 'Total Bases'
    left_list = sorted(player_list, key=lambda x: x.dft_object.hitting_stat_lines[ballpark].
                       composite_stats[stat]['L'], reverse=True)
    right_list = sorted(player_list, key=lambda x: x.dft_object.hitting_stat_lines[ballpark].
                        composite_stats[stat]['R'], reverse=True)
    return left_list, right_list, str_stat


def pitcher_stat_sort(stat, player_list, ballpark):
    str_stat = ''
    if stat == 'rt':
        stat = 'rating'
        str_stat = 'Pinch Hit Rating'
    elif stat == 'hi':
        stat = 'hits'
        str_stat = 'Hits'
    elif stat == 'ob':
        stat = 'on_base'
        str_stat = 'On Base'
    elif stat == 'tb':
        stat = 'total_bases'
        str_stat = 'Total Bases'
    left_list = sorted(player_list, key=lambda x: x.dft_object.pitching_stat_lines[ballpark].
                       composite_stats[stat]['L'])
    right_list = sorted(player_list, key=lambda x: x.dft_object.pitching_stat_lines[ballpark].
                        composite_stats[stat]['R'])
    return left_list, right_list, str_stat


def display_hitters_stats(dft, stat, position, ballpark):
    # get proper player lists
    player_list = [x for x in dft.draftable_object_list if ((x.object_type == 'H') or (x.object_type == 'X'))]
    player_list = [x for x in player_list if not x.drafted]
    if position != 0:
        player_list = filter_hitters_by_position(player_list, position)
    # sort by proper stats
    left_list, right_list, str_stat = hitter_stat_sort(stat, player_list, ballpark)
    if position == 0:
        str_position = 'All Players'
    else:
        str_position = get_full_position_name_from_int(position)
    print('\n{} By {}'.format(str_position, str_stat))
    print('{0:3} {1:16} {2:4} {3:3} {4:3} {5:3}      {0:3} {1:16} {6:4} {7:3} {8:3} {9:3}'
          .format('ID', 'Name', 'rtL', 'hL', 'obL', 'tbL', 'rtR', 'hR', 'obR', 'tbR'))
    display_players = 15
    if len(player_list) < display_players:
        display_players = len(player_list)
    for i in range(display_players):
        print('{0:3} {1:16} {2:4.1f} {3:3.0f} {4:3.0f} {5:3.0f}      {6:3} {7:16} {8:4.1f} {9:3.0f} {10:3.0f} {11:3.0f}'.format(
            left_list[i].draft_id,
            left_list[i].dft_object.full_name[:16],
            left_list[i].dft_object.hitting_stat_lines[ballpark].composite_stats['rating']['L'],
            left_list[i].dft_object.hitting_stat_lines[ballpark].composite_stats['hits']['L'] / 20,
            left_list[i].dft_object.hitting_stat_lines[ballpark].composite_stats['on_base']['L'] / 20,
            left_list[i].dft_object.hitting_stat_lines[ballpark].composite_stats['total_bases']['L'] / 20,
            right_list[i].draft_id,
            right_list[i].dft_object.full_name[:16],
            right_list[i].dft_object.hitting_stat_lines[ballpark].composite_stats['rating']['R'],
            right_list[i].dft_object.hitting_stat_lines[ballpark].composite_stats['hits']['R'] / 20,
            right_list[i].dft_object.hitting_stat_lines[ballpark].composite_stats['on_base']['R'] / 20,
            right_list[i].dft_object.hitting_stat_lines[ballpark].composite_stats['total_bases']['R'] / 20,))
    print()
    return True


def display_hitters_with_defense(dft, position, ballpark):
    # get proper player lists
    player_list = [x for x in dft.draftable_object_list if ((x.object_type == 'H') or (x.object_type == 'X'))]
    player_list = [x for x in player_list if not x.drafted]
    player_list = filter_hitters_by_position(player_list, position)
    str_stat = 'Overall Rating with Defense'
    position = get_position_from_int(position)
    left_list = sorted(player_list, key=lambda x: x.dft_object.hitting_stat_lines[ballpark].
                       composite_stats['total_ratings'][position]['L'], reverse=True)
    right_list = sorted(player_list, key=lambda x: x.dft_object.hitting_stat_lines[ballpark].
                        composite_stats['total_ratings'][position]['R'], reverse=True)
    str_position = get_full_position_name_from_int(position)
    print('\n{} By {}'.format(str_position, str_stat))
    print('{0:3}  {1:16} {2:4}  {3:4} {4:3} {5:3} {6:3}      {0:3}  {1:16} {7:4}  {8:4} {9:3} {10:3} {11:3}'
          .format('ID', 'Name', 'rtL', 'phL', 'hL', 'obL', 'tbL', 'rtR', 'phR', 'hR', 'obR', 'tbR'))
    display_players = 15
    if len(player_list) < display_players:
        display_players = len(player_list)
    for i in range(display_players):
        print('{0:3}  {1:16} {2:4.1f}  {3:4.1f} {4:3.0f} {5:3.0f} {6:3.0f}'
              '      {7:3}  {8:16} {9:4.1f}  {10:4.1f} {11:3.0f} {12:3.0f} {13:3.0f}'.format(
               left_list[i].draft_id,
               left_list[i].dft_object.full_name[:16],
               left_list[i].dft_object.hitting_stat_lines[ballpark].composite_stats['total_ratings'][position]['L'],
               left_list[i].dft_object.hitting_stat_lines[ballpark].composite_stats['rating']['L'],
               left_list[i].dft_object.hitting_stat_lines[ballpark].composite_stats['hits']['L'] / 20,
               left_list[i].dft_object.hitting_stat_lines[ballpark].composite_stats['on_base']['L'] / 20,
               left_list[i].dft_object.hitting_stat_lines[ballpark].composite_stats['total_bases']['L'] / 20,
               right_list[i].draft_id,
               right_list[i].dft_object.full_name[:16],
               right_list[i].dft_object.hitting_stat_lines[ballpark].composite_stats['total_ratings'][position]['R'],
               right_list[i].dft_object.hitting_stat_lines[ballpark].composite_stats['rating']['R'],
               right_list[i].dft_object.hitting_stat_lines[ballpark].composite_stats['hits']['R'] / 20,
               right_list[i].dft_object.hitting_stat_lines[ballpark].composite_stats['on_base']['R'] / 20,
               right_list[i].dft_object.hitting_stat_lines[ballpark].composite_stats['total_bases']['R'] / 20,))
    print()
    return True


def display_pitchers_stats(dft, stat, position, ballpark):
    # get specific player list
    player_list = [x for x in dft.draftable_object_list if x.object_type == 'P' or x.object_type == 'X']
    player_list = [x for x in player_list if not x.drafted]
    if position != 0:
        player_list = filter_pitchers_by_position(player_list, position)
    left_list, right_list, str_stat = pitcher_stat_sort(stat, player_list, ballpark)
    if position == 0:
        str_position = 'All Pitchers'
    else:
        str_position = pitcher_positions(position)
    print('\n{} By {}'.format(str_position, str_stat))
    print('{0:3} {1:16} {2:4} {3:3} {4:3} {5:3}      {0:3} {1:16} {6:4} {7:3} {8:3} {9:3}'
          .format('ID', 'Name', 'rtL', 'hL', 'obL', 'tbL', 'rtR', 'hR', 'obR', 'tbR'))
    display_players = 15
    if len(player_list) < display_players:
        display_players = len(player_list)
    for i in range(display_players):
        print('{0:3} {1:16} {2:4.1f} {3:3.0f} {4:3.0f} {5:3.0f}      {6:3} {7:16} {8:4.1f} {9:3.0f} {10:3.0f} {11:3.0f}'.format(
            left_list[i].draft_id,
            left_list[i].dft_object.full_name[:16],
            left_list[i].dft_object.pitching_stat_lines[ballpark].composite_stats['rating']['L'],
            left_list[i].dft_object.pitching_stat_lines[ballpark].composite_stats['hits']['L'] / 20,
            left_list[i].dft_object.pitching_stat_lines[ballpark].composite_stats['on_base']['L'] / 20,
            left_list[i].dft_object.pitching_stat_lines[ballpark].composite_stats['total_bases']['L'] / 20,
            right_list[i].draft_id,
            right_list[i].dft_object.full_name[:16],
            right_list[i].dft_object.pitching_stat_lines[ballpark].composite_stats['rating']['R'],
            right_list[i].dft_object.pitching_stat_lines[ballpark].composite_stats['hits']['R'] / 20,
            right_list[i].dft_object.pitching_stat_lines[ballpark].composite_stats['on_base']['R'] / 20,
            right_list[i].dft_object.pitching_stat_lines[ballpark].composite_stats['total_bases']['R'] / 20,))
    return True


def display_info(dft, dft_id):
    pick = [x for x in dft.draftable_object_list if x.draft_id == dft_id][0]
    if pick is not None:
        print()
        if pick.object_type == "H" or pick.object_type == "P":
            pick.dft_object.display_card()
        elif pick.object_type == "B":
            print(pick.dft_object.location)
            print('{} in {}, {}'.format(pick.dft_object.name, pick.dft_object.city, pick.dft_object.state))
            print()
            print('Singles vs. Left:   {:2}'.format(pick.dft_object.single_left))
            print('Singles vs. Right:  {:2}'.format(pick.dft_object.single_right))
            print('Homeruns vs. Left:  {:2}'.format(pick.dft_object.homerun_left))
            print('Homeruns vs. Right: {:2}'.format(pick.dft_object.homerun_right))
        else:
            print("Cannot figure out what to do.")
    else:
        print("Cannot figure out what to do.")
    print()
    return True


def display_team_header(number, name):
    print('Team {}: {}\n'.format(number, name))


def display_ballpark(draftable_object):
    if len(draftable_object) > 0:
        print('ballpark object:')
        ballpark = draftable_object[0].dft_object
    else:
        ballpark = Ballpark()
    print('Ballpark: {}'.format(ballpark.location), end='')
    if ballpark.name != 'None':
        print(', {}'.format(ballpark.name))
    else:
        print()
    print('{:2} | {:2}'.format(ballpark.single_left, ballpark.single_right))
    print('---+---')
    print('{:2} | {:2}\n'.format(ballpark.homerun_left, ballpark.homerun_right))
    print()
    print()
    return True


def display_pitchers_for_team(roster):
    sp = [x for x in roster if 'sp' in x.position]
    lrp = [x for x in roster if 'lrp' in x.position]
    rrp = [x for x in roster if 'rrp' in x.position]
    sp.sort(key=lambda x: x.team_position)
    lrp.sort(key=lambda x: x.team_position)
    rrp.sort(key=lambda x: x.team_position)
    length = max(4, len(sp), len(lrp), len(rrp))
    print("     Starting Pitchers                 Left Handed Relief                     Right Handed Relief")
    for i in range(length):
        # starting pitchers
        try:
            name = sp[i].dft_object.full_name[:18]
            if sp[i].dft_object.arm.lower() == 'l':
                name = sp[i].dft_object.full_name[:17] + '*'
            print(' {0:1}- {1:3} {2:18} {3:4.1f}/{4:4.1f}'
                  .format(i+1, sp[i].draft_id, name, 0, 0), end='')
        except IndexError:
            print(' {0:1}- {1:32}'.format(i+1, ''), end='')
    # left handed relief pitchers
        try:
            print(' {0:1}- {1:3} {2:18} {3:4.1f}/{4:4.1f}'
                  .format(i+1, lrp[i].draft_id, lrp[i].dft_object.full_name[:18], 0, 0), end='')
        except IndexError:
            print('  {0:34}'.format(''), end='')
    # right handed relief pitchers
        try:
            print(' {0:1}- {1:3} {2:18} {3:4.1f}/{4:4.1f}'
                  .format(i+1, rrp[i].draft_id, rrp[i].dft_object.full_name[:18], 0, 0))
        except IndexError:
            print('  {0:34}'.format(''))
    print()


def display_position_header():
    print('           Position Players')
    print('      vs Left                   vs Right                        Backup')


def display_position_for_team(position, roster):
    vs_left = [x for x in roster if '{}{}'.format(get_position_int_from_string(position), 'L') in x.position]
    vs_right = [x for x in roster if '{}{}'.format(get_position_int_from_string(position), 'R') in x.position ]
    backup_list = [x for x in roster if str(get_position_int_from_string(position)) not in x.position]
    backup_list = [x for x in backup_list if '{}-'.format(position) in x.dft_object.defense_string]
    left_name = ''
    right_name = ''
    backup = '  '
    if len(vs_left) > 1:
        left_name = '    ERROR, {} players'.format(len(vs_left))
    elif len(vs_left) == 0:
        left_name = ''
    elif len(vs_left) == 1:
        left_name = '{:3} {}'.format(vs_left[0].draft_id, vs_left[0].dft_object.full_name[:21])
    if len(vs_right) > 1:
        right_name = '    ERROR, {} players'.format(len(vs_right))
    elif len(vs_right) == 0:
        right_name = ''
    elif len(vs_right) == 1:
        right_name = '{:3} {}'.format(vs_right[0].draft_id, vs_right[0].dft_object.full_name[:21])
    for x in backup_list:
        backup += '{} {}  '.format(x.draft_id, x.dft_object.full_name)
    print('{:2}- {:25} {:25} {} '.format(position, left_name, right_name, backup[:-2]))


def display_team(dft, team_number):
    if team_number > dft.number_of_teams:
        print("Invalid team number, team # must be {} or lower"
              .format(dft.number_of_teams))
    else:
        # get the 0 based index for the team
        tm = team_number - 1
        # get the picks for the team
        roster = [x for x in dft.draftable_object_list if x.team == team_number]
        dft.organize_position_list(team_number, 'AVG')
        # call methods for header display
        display_team_header(team_number, dft.teams[tm].name)
        display_ballpark([x for x in roster if x.object_type == 'B'])
        # call methods for pitcher display
        display_pitchers_for_team(roster)
        # call methods for position display
        positions = ['c', '1b', '2b', '3b', 'ss', 'lf', 'cf', 'rf']
        display_position_header()
        for pos in positions:
            display_position_for_team(pos, roster)
        print()
    return True


def change_team_name(dft, team_number):
    if team_number > dft.number_of_teams:
        print("Invalid team number, team # must be {} or lower"
              .format(dft.number_of_teams))
    else:
        dft.teams[team_number - 1].change_name(input("Team Name for team #{}: ".format(team_number)))
        return dft


def force_player_into_lineup(dft):
    player_id = input('Enter Draft ID of player to force: ')
    if len([x for x in dft.draftable_object_list if x.drafted and x.draft_id == player_id]):
        player = [x for x in dft.draftable_object_list if x.drafted and x.draft_id == player_id][0]
        left_position = input("Force into what position vs Left (0 don't force")
        right_position = input("Force into what position vs Right (0 don't force")
        if left_position in range(2,10) and right_position in range(2, 10):
            force_type = 'LR'
            position = [left_position, right_position]
        elif left_position in range(2,10) and right_position not in range(2, 10):
            force_type = 'L'
            position = left_position
        elif left_position not in range(2,10) and right_position in range(2, 10):
            force_type = 'R'
            position = right_position
        else:
            print('No valid position chosen to force into lineup')
        dft.force_into_lineup(player, force_type, position)


def change_ballpark_suggestions(dft, team_number):
    ballparks = [x for x in dft.draftable_object_list if x.object_type == 'B' and not x.drafted]
    for b in ballparks:
        print('{} {}'.format(b.draft_id, b.dft_object.full_name))
    pick_id = san.sanitize_int('Select Ballpark to rate for:',
                               min([x.draft_id for x in ballparks]),
                               max([x.draft_id for x in ballparks]))
    ballpark_id = [x.dft_object.ballpark_id for x in ballparks if x.draft_id == pick_id][0]
    dft.teams[team_number - 1].change_ballpark_suggestions(ballpark_id)


def in_draft_decision(dft, choice):
    hold_at_end = False
    # display next 50 players by aps
    if re.search('^aps$', choice, re.I):
        hold_at_end = display_aps(dft)
    elif re.search('^s[0-9]+$', choice, re.I):
        hold_at_end = print_suggestions(dft, int(choice[1:]), dft.teams[int(choice[1:]) - 1].suggest_park, 60, True)
    # change ballpark suggestions
    elif re.search('^pk$', choice, re.I):
        change_ballpark_suggestions(dft, dft.current_team)
    # force player into a lineup
    elif re.search('^f$', choice, re.I):
        force_player_into_lineup(dft)
    # list of players by stats by position
    elif re.search('^(rt|hi|ob|tb)[2-9]$', choice, re.I):
        hold_at_end = display_hitters_stats(dft, choice[:2], int(choice[2]), dft.main_team.suggest_park)
    elif re.search('^(rt|hi|ob|tb)[2-9]t$', choice, re.I):
        hold_at_end = display_hitters_stats(dft, choice[:2], int(choice[2]), dft.teams[dft.current_team - 1].suggest_park)
    # list of players by stats
    elif re.search('^(rt|hi|ob|tb)$', choice, re.I):
        hold_at_end = display_hitters_stats(dft, choice, 0, dft.teams[dft.current_team - 1])
    elif re.search('^rd[2-9]$', choice, re.I):
        hold_at_end = display_hitters_with_defense(dft, int(choice[2]), dft.teams[dft.current_team - 1])
    # lister of pitchers by stats
    elif re.search('^p(rt|hi|ob|tb)$', choice, re.I):
        hold_at_end = display_pitchers_stats(dft, choice[1:], 0, dft.teams[dft.current_team - 1])
    elif re.search('^(l|r|)(s|r)p(rt|hi|ob|tb)$', choice, re.I):
        hold_at_end = display_pitchers_stats(dft, choice[-2:], choice[:-2], dft.teams[dft.current_team - 1])
    # display team for current pick
    elif re.search('^t$', choice, re.I):
        hold_at_end = display_team(dft, dft.current_team)
    # display team for a specific draft position
    elif re.search('^t[0-9]+$', choice, re.I):
        hold_at_end = display_team(dft, int(choice[1:]))
    # display info for a card or ballpark
    elif re.search('^i[0-9]+$', choice, re.I):
        hold_at_end = display_info(dft, int(choice[1:]))
    # change team name
    elif re.search('^n[0-9]+$', choice, re.I):
        dft = change_team_name(dft, int(choice[1:]))
    # select a player by name
    elif re.search('^[a-z]+$', choice, re.I):
        dft = make_pick_by_name(dft, choice)
    # select a player by id
    elif re.search('^[0-9]+$', choice, re.I):
        dft = make_pick_by_draft_id(dft, int(choice))
    if hold_at_end:
        input()
    return dft


def run_draft(dft):
    dft, main_team = setup_draft(dft)
    dft.assign_team_names(select_team_names(dft), main_team)
    dft.load_draftable_objects()
    dft.compile_ballpark_stats()
    dft.organize_position_list(0, 'AVG')
    dft.start_draft()
    # default draft settings
    draft_in_progress = True
    display_draft = True
    display_suggestions = True
    while draft_in_progress:
        if display_draft:
            display_draft_by_round(dft)
        if display_suggestions:
            dft.organize_position_list(dft.current_team, 'AVG')
            print_suggestions(dft, dft.current_team, dft.teams[dft.current_team - 1].suggest_park, 20, False)
        choice = input(" Pick #{}, Round #{}, {} is on the clock, Make a selection: "
                       .format(dft.current_pick,
                               dft.current_round,
                               dft.teams[dft.current_team - 1].name)).lower()
        # adjust draft settings
        if choice == 's':
            # toggle pick suggestions
            display_suggestions = not display_suggestions
        elif choice == 'd':
            # toggle draft display
            display_draft = not display_draft
        else:
            dft = in_draft_decision(dft, choice)
        # check for end of draft
        if dft.current_pick > (dft.number_of_teams * dft.number_of_rounds):
            draft_in_progress = False
