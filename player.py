import baseball_lookups as be
import results
import sql
from ballpark import Ballpark


class Defense:

    def __init__(self, position, def_range, def_error):
        self.position = position
        self.def_range = def_range
        self.def_error = def_error


class Player:
    player_id = ''
    card_id = ''
    year = 0
    first_name = ''
    last_name = ''
    player_type = ''
    bats = ''
    bunt = ''
    hit_run = ''
    running = 0
    power_left = False
    power_right = False
    stealing = 'E'
    asterisk_stealing = False
    front_stealing = 0
    back_stealing = 0
    stealing_lead_string = '-----------'

    def __init__(self, card_id):
        # get player data from sql
        player_data = sql.get_player_data(card_id)
        name = sql.get_player_name(player_data[0])
        # create player data
        self.player_id = player_data[0]
        self.card_id = player_data[1]
        self.year = player_data[3]
        self.first_name = name[1]
        self.last_name = name[2]
        self.full_name = '{}, {}'.format(self.last_name, self.first_name)
        self.player_type = 'H'
        self.bats = player_data[5]
        self.bunt = player_data[6]
        self.hit_run = player_data[7]
        self.running = player_data[8]
        self.power_left = False
        if player_data[9] == 1:
            self.power_left = True
        self.power_right = False
        if player_data[10] == 1:
            self.power_right = True
        self.stealing = player_data[11]
        self.asterisk_stealing = False
        if player_data[12] == 1:
            self.asterisk_stealing = True
        self.front_stealing = player_data[13]
        self.back_stealing = player_data[14]
        self.stealing_lead_string = player_data[15]


class Hitter(Player):
    defense = []
    of_arm = 0
    c_arm = 0
    c_t_rtg = 0
    c_pb = 0
    hitting_results = []

    def __init__(self, card_id):
        Player.__init__(self, card_id)
        # hitter data from sql
        hitter_data = sql.get_hitter_data(card_id)
        hitter_results_data = sql.get_hitter_results_data(card_id)

        # hitter data
        self.defense = hitter_data[1:8]
        self.of_arm = hitter_data[9]
        self.c_arm = hitter_data[10]
        self.c_t_rtg = hitter_data[11]
        self.c_pb = hitter_data[12]

        # hitters results data
        self.hitting_results = []
        for i in range(66):
            loc = hitter_results_data[i][3]
            side = hitter_results_data[i][2]
            primary = hitter_results_data[i][4]
            secondary = hitter_results_data[i][5]
            split = hitter_results_data[i][6]
            injury = False
            if hitter_results_data[i][7] == 1:
                injury = True
            clutch = False
            if hitter_results_data[i][8] == 1:
                clutch = True
            hitting_result = results.HitterResult(loc, side, primary, secondary, split, injury, clutch)
            self.hitting_results.append(hitting_result)

        self.hitting_card = create_hitting_card(self.hitting_results)

        # create combined strings
        self.defense_string = be.create_defense_string(hitter_data)
        self.error_ratings = be.create_error_string(hitter_data)
        self.defensive_rating = be.create_defense_ratings(hitter_data)
        self.stealing_string = be.build_stealing_string(self.asterisk_stealing, self.front_stealing,
                                                        self.back_stealing, self.stealing_lead_string)

        # create stat lines
        self.hitter_stats = results.HitterStats(
            [self.power_left, self.power_right], self.hitting_results)
        self.hitting_stat_lines = dict()

    def add_hitting_stat_line(self, id_, ballpark):
        self.hitting_stat_lines[id_] = results.CompositeStatsHitter(self.hitter_stats,
                                                                    self.defensive_rating,
                                                                    self.bats, ballpark)

    def display_card(self):
        name = self.first_name + " " + self.last_name
        print("{} | {:36} {:^26}     hit & run-{}  bunting-{}  running 1-{:2}"
              .format(self.bats, name[:36], self.stealing_string, self.hit_run, self.bunt, self.running))
        print('{:-^108}'.format('-'))
        print("     {}".format(self.defense_string))
        print("     {}".format(self.error_ratings))
        print('{:-^108}'.format('-'))
        print(' {:>5.2f}    {:4}   |  {:3.0f}  {:3.0f}  {:3.0f}  | {:>4}  {:3.0f}  {:3.0f}  |'
              '| {:>5.2f}    {:4}   |  {:3.0f}  {:3.0f}  {:3.0f}  | {:>4}  {:3.0f}  {:3.0f}  '
              .format(self.hitter_stats.base_stats['homerun']['L'] / 20,
                      self.hitter_stats.base_stats['ballpark_string']['L'],
                      self.hitter_stats.base_stats['hits']['L'] / 20,
                      self.hitter_stats.base_stats['on_base']['L'] / 20,
                      self.hitter_stats.base_stats['total_bases']['L'] / 20,
                      be.leading_plus(self.hitter_stats.base_stats['clutch']['L']),
                      (self.hitter_stats.base_stats['hits']['L'] + self.hitter_stats.base_stats['clutch']['L']) / 20,
                      self.hitter_stats.base_stats['gbA']['L'] / 20,
                      self.hitter_stats.base_stats['homerun']['R'] / 20,
                      self.hitter_stats.base_stats['ballpark_string']['R'],
                      self.hitter_stats.base_stats['hits']['R'] / 20,
                      self.hitter_stats.base_stats['on_base']['R'] / 20,
                      self.hitter_stats.base_stats['total_bases']['R'] / 20,
                      be.leading_plus(self.hitter_stats.base_stats['clutch']['R']),
                      (self.hitter_stats.base_stats['hits']['R'] + self.hitter_stats.base_stats['clutch']['R']) / 20,
                      self.hitter_stats.base_stats['gbA']['R'] / 20,
                      ))
        print('{:-^108}'.format('-'))
        for i in range(len(self.hitting_card[0])):
            print('{0:>4}{1:13}|{2:>4}{3:13}|{4:>4}{5:13}||{6:>4}{7:13}|{8:>4}{9:13}|{10:>4}{11:13}'
                  .format(self.hitting_card[0][i], self.hitting_card[1][i], self.hitting_card[2][i],
                          self.hitting_card[3][i], self.hitting_card[4][i], self.hitting_card[5][i],
                          self.hitting_card[6][i], self.hitting_card[7][i], self.hitting_card[8][i],
                          self.hitting_card[9][i], self.hitting_card[10][i], self.hitting_card[11][i]))
        print()


def create_hitting_card(hitting_results):
    results_display = []
    for i in range(6):
        dice_column = []
        result_column = []
        for j in range(11):
            dice_roll = ''
            result = ''
            second_result = ''
            if hitting_results[i * 11 + j].split == 20:
                if hitting_results[i * 11 + j].clutch:
                    dice_roll = "{}{}-".format('\u03a9', j + 2)
                else:
                    dice_roll = '{}-'.format(j + 2)
                result = '{}'.format(be.long_results(hitting_results[i * 11 + j].primary_result))
                dice_column.append(dice_roll)
                result_column.append(result)
                if hitting_results[i * 11 + j].injury:
                    dice_column.append('')
                    result_column.append(' plus INJURY')
            else:
                dice_roll = '{}-'.format(j + 2)
                result = '{:8}{:^5}'.format(be.short_results(hitting_results[i * 11 + j].primary_result),
                                            be.front_split(hitting_results[i * 11 + j].split))
                second_result = '{:8}{:^5}'.format(be.short_results(hitting_results[i * 11 + j].secondary_result),
                                                   be.back_split(hitting_results[i * 11 + j].split))
                dice_column.append(dice_roll)
                dice_column.append('')
                result_column.append(result)
                result_column.append(second_result)
        while len(dice_column) < 15:
            dice_column.append('')
            result_column.append('')
        results_display.append(dice_column)
        results_display.append(result_column)
    return results_display


def display_hitting_result(dice_roll, hitting_result):
    result = ''
    if hitting_result.clutch:
        result += "X"
    else:
        result += " "
    result += "{:2}-".format(dice_roll)
    result += "{}".format(be.long_results(hitting_result.primary_result))
    if hitting_result.injury:
        result += "+INJ"
    return result


class Pitcher(Player):
    arm = ''
    endurance_starter = 0
    endurance_reliever = 0
    endurance_closer = 0
    hold = 0
    wild_pitch = 0
    balk = 0
    def_range = 0
    def_error = 0
    pitcher_hitting_card = 0
    pitching_results = []

    def __init__(self, card_id):
        Player.__init__(self, card_id)
        # pitcher data from sql
        pitcher_data = sql.get_pitcher_data(card_id)
        pitcher_results_data = sql.get_pitcher_results_data(card_id)
        # pitcher data
        self.arm = pitcher_data[1]
        self.endurance_starter = pitcher_data[2]
        self.endurance_reliever = pitcher_data[3]
        self.endurance_closer = pitcher_data[4]
        self.hold = pitcher_data[5]
        self.wild_pitch = pitcher_data[6]
        self.balk = pitcher_data[7]
        self.def_range = pitcher_data[8]
        self.def_error = pitcher_data[9]
        self.pitcher_hitting_card = pitcher_data[10]

        # pitchers results data
        self.pitching_results = []
        for i in range(66):
            loc = pitcher_results_data[i][3]
            side = pitcher_results_data[i][2]
            primary = pitcher_results_data[i][4]
            secondary = pitcher_results_data[i][5]
            split = pitcher_results_data[i][6]
            injury = False
            if pitcher_results_data[i][7] == 1:
                injury = True
            weakness_dot = False
            if pitcher_results_data[i][8] == 1:
                weakness_dot = True
            pitching_result = results.PitcherResult(loc, side, primary, secondary, split, injury, weakness_dot)
            self.pitching_results.append(pitching_result)

        self.pitching_card = create_pitching_card(self.pitching_results)

        # create combined strings
        self.stealing_string = be.build_stealing_string(self.asterisk_stealing, self.front_stealing,
                                                     self.back_stealing, self.stealing_lead_string)
        self.error_string = be.get_error_numbers(1, self.def_error)

        # create stat lines
        self.pitcher_stats = results.PitcherStats(self.pitching_results)
        self.pitching_stat_lines = dict()

    def add_pitching_stat_line(self, id_, ballpark):
        self.pitching_stat_lines[id_] = results.CompositeStatsPitcher(self.pitcher_stats, ballpark)

    def display_card(self):
        name = self.first_name + " " + self.last_name
        starter_end = ''
        relief_end = ''
        closer_end = ''
        if self.endurance_closer == -1:
            closer_end = 'N'
        else:
            closer_end = str(self.endurance_closer)
        power = 'W'
        if self.power_left:
            power = 'N'
        hitting = '{}{}{}'.format(self.pitcher_hitting_card, power, self.bats)
        if self.endurance_starter > 0:
            starter_end = 'starter-({}) \u25cf'.format(self.endurance_starter)
        if self.endurance_reliever > 0:
            relief_end = 'relief-({})/{} \u25cf'.format(self.endurance_reliever, closer_end)
        if self.arm == 'L':
            arm = 'LEFT'
        else:
            arm = 'RIGHT'
        print("{:40}       bk-{:<2}   wp-{:<2}   e{:<2}  #{}  run-{}  pitcher-{}   {}"
              .format(name[:40], self.balk, self.wild_pitch, self.def_error, hitting, self.running, self.def_range, starter_end))
        print("  {:^26} {:^17}  throws {:<5}        hold {:<2}     bunting-{}    {}"
              .format(self.error_string, self.stealing_string, arm, be.leading_plus(self.hold), self.bunt, relief_end))
        print('{:-^108}'.format('-'))
        print(' {:>5.2f}    {:4}   |  {:3.0f}  {:3.0f}  {:3.0f}  |             {:2.0f}  |'
              '| {:>5.2f}    {:4}   |  {:3.0f}  {:3.0f}  {:3.0f}  |             {:2.0f}  '
              .format(self.pitcher_stats.base_stats['homerun']['L'] / 20,
                      self.pitcher_stats.base_stats['ballpark_string']['L'],
                      self.pitcher_stats.base_stats['hits']['L'] / 20,
                      self.pitcher_stats.base_stats['on_base']['L'] / 20,
                      self.pitcher_stats.base_stats['total_bases']['L'] / 20,
                      self.pitcher_stats.base_stats['gbA']['L'] / 20,
                      self.pitcher_stats.base_stats['homerun']['R'] / 20,
                      self.pitcher_stats.base_stats['ballpark_string']['R'],
                      self.pitcher_stats.base_stats['hits']['R'] / 20,
                      self.pitcher_stats.base_stats['on_base']['R'] / 20,
                      self.pitcher_stats.base_stats['total_bases']['R'] / 20,
                      self.pitcher_stats.base_stats['gbA']['R'] / 20,
                      ))
        print('{:-^108}'.format('-'))
        for i in range(len(self.pitching_card[0])):
            print('{0:>4}{1:13}|{2:>4}{3:13}|{4:>4}{5:13}||{6:>4}{7:13}|{8:>4}{9:13}|{10:>4}{11:13}'
                  .format(self.pitching_card[0][i], self.pitching_card[1][i], self.pitching_card[2][i],
                          self.pitching_card[3][i], self.pitching_card[4][i], self.pitching_card[5][i],
                          self.pitching_card[6][i], self.pitching_card[7][i], self.pitching_card[8][i],
                          self.pitching_card[9][i], self.pitching_card[10][i], self.pitching_card[11][i]))
        print()


def create_pitching_card(pitching_results):
    results_display = []
    for i in range(6):
        dice_column = []
        result_column = []
        for j in range(11):
            dice_roll = ''
            results = ''
            second_result = ''
            if pitching_results[i * 11 + j].split == 20:
                dice_roll = '{}-'.format(j + 2)
                result = '{}'.format(be.long_results(pitching_results[i * 11 + j].primary_result))
                if pitching_results[i * 11 + j].pow_dot:
                    result += ' \u25cf'
                dice_column.append(dice_roll)
                result_column.append(result)
            else:
                dice_roll = '{}-'.format(j + 2)
                result = '{:8}{:^5}'.format(be.short_results(pitching_results[i * 11 + j].primary_result),
                                            be.front_split(pitching_results[i * 11 + j].split))
                second_result = '{:8}{:^5}'.format(be.short_results(pitching_results[i * 11 + j].secondary_result),
                                                   be.back_split(pitching_results[i * 11 + j].split))
                dice_column.append(dice_roll)
                dice_column.append('')
                result_column.append(result)
                result_column.append(second_result)
        while len(dice_column) < 15:
            dice_column.append('')
            result_column.append('')
        results_display.append(dice_column)
        results_display.append(result_column)
    return results_display


class DoubleDuty(Hitter, Pitcher):
    def __init__(self, card_id):
        Hitter.__init__(self, card_id)
        Pitcher.__init__(self, card_id)

    def display_card(self):
        Hitter.display_card()
        Pitcher.display_card()


def open_player_list(file_name):
    file = open("./data/player_lists/{}.txt".format(file_name))
    data = file.readlines()
    player_list = []
    for line in data:
        line = line.replace('\n', '')
        player_list.append(line)
    return player_list


def load_players(player_list):
    players = []
    for p in player_list:
        player_data = sql.get_player_data(p)
        if player_data[4] == "H":
            plr = Hitter(player_data)
            players.append(plr)
        elif player_data[4] == "P":
            plr = Pitcher(player_data)
            players.append(plr)
    return players
