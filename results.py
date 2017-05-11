import baseball_lookups


class Result:
    location = 0
    side = ''
    primary_result = 0
    secondary_result = 0
    split = 0
    injury = False

    def __init__(self, location, side, primary, secondary, split, injury):
        self.location = location
        self.side = side
        self.primary_result = primary
        self.secondary_result = secondary
        self.split = split
        self.injury = injury


class HitterResult(Result):
    clutch = False

    def __init__(self, location, side, primary, secondary, split, injury, clutch):
        Result.__init__(self, location, side, primary, secondary, split, injury)
        self.clutch = clutch


class PitcherResult(Result):
    pow_dot = False

    def __init__(self, location, side, primary, secondary, split, injury, dot):
        Result.__init__(self, location, side, primary, secondary, split, injury)
        self.pow_dot = dot


class Stats:

    def __init__(self, results):
        self.base_stats = {
            'walk': {'L': 0, 'R': 0},
            'single_1': {'L': 0, 'R': 0},
            'single_2': {'L': 0, 'R': 0},
            'single_open': {'L': 0, 'R': 0},
            'double_2': {'L': 0, 'R': 0},
            'double_3': {'L': 0, 'R': 0},
            'double_open': {'L': 0, 'R': 0},
            'triple': {'L': 0, 'R': 0},
            'homerun': {'L': 0, 'R': 0},
            'ballpark_single': {'L': 0, 'R': 0},
            'ballpark_homerun': {'L': 0, 'R': 0},
            'gbA': {'L': 0, 'R': 0},
            'gbA_corner': {'L': 0, 'R': 0},
            'gbA_middle': {'L': 0, 'R': 0},
            'gbB': {'L': 0, 'R': 0},
            'gbB_corner': {'L': 0, 'R': 0},
            'gbB_middle': {'L': 0, 'R': 0},
            'gbC': {'L': 0, 'R': 0},
            'gbC_corner': {'L': 0, 'R': 0},
            'gbC_middle': {'L': 0, 'R': 0},
            'fly_B': {'L': 0, 'R': 0},
            'fly_Bx': {'L': 0, 'R': 0},
            'pure_out': {'L': 0, 'R': 0},
            'lomax': {'L': 0, 'R': 0},
            'injury': {'L': 0, 'R': 0},
            'x_chart': {'L': 0, 'R': 0},
            'hits': {'L': 0, 'R': 0},
            'on_base': {'L': 0, 'R': 0},
            'total_bases': {'L': 0, 'R': 0},
        }
        chance_layout = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
        for i in range(66):
            primary_chances = results[i].split * chance_layout[results[i].location % 11]
            secondary_chances = (20 - results[i].split) * chance_layout[results[i].location % 11]
            primary_list = baseball_lookups.get_result_list(results[i].primary_result)
            secondary_list = baseball_lookups.get_result_list(results[i].secondary_result)
            for stat in primary_list:
                self.base_stats[stat][results[i].side] += primary_chances
            for stat in secondary_list:
                self.base_stats[stat][results[i].side] += secondary_chances


class HitterStats(Stats):

    def __init__(self, power, hitter_results):
        Stats.__init__(self, hitter_results)
        self.base_stats['power'] = {'L': power[0], 'R': power[1]}
        self.base_stats['ballpark_string'] = self.get_ballpark_string(self.base_stats['power'],
                                                                      self.base_stats['ballpark_homerun'],
                                                                      self.base_stats['ballpark_single'])
        self.base_stats['clutch'] = self.get_clutch_stats(hitter_results)

    @staticmethod
    def get_clutch_stats(results):
        chance_layout = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
        clutch = {'L': 0, 'R': 0}
        for i in range(66):
            clutch_result = chance_layout[results[i].location % 11] * baseball_lookups.clutch_lookup(results[i])
            clutch[results[i].side] += clutch_result
        return clutch

    @staticmethod
    def get_ballpark_string(power, dia, tri):
        bp_string = dict()
        for s in ['L', 'R']:
            if not power[s]:
                bp_string[s] = 'W'
            else:
                bp_string[s] = '{:1.0f}'.format(dia[s] / 20)
            if tri[s] == 0:
                bp_string[s] += '\u25bc\u2009'
        return bp_string


class PitcherStats(Stats):
    def __init__(self, results):
        Stats.__init__(self, results)
        self.base_stats['ballpark_string'] = self.get_ballpark_string(self.base_stats['ballpark_homerun'],
                                                                      self.base_stats['ballpark_homerun'])

    @staticmethod
    def get_ballpark_string(dia, tri):
        bp_string = dict()
        for s in ['L', 'R']:
            bp_string[s] = '{:1.0f}'.format(dia[s] / 20)
            if tri[s] == 0:
                bp_string[s] += '\u25bc\u2009'
        return bp_string


class CompositeStats:

    def __init__(self, stat_line):
        self.composite_stats = {
            'single': {'L': 0, 'R': 0},
            'double': {'L': 0, 'R': 0},
            'triple': {'L': 0, 'R': 0},
            'homerun': {'L': 0, 'R': 0},
            'hits': {'L': 0, 'R': 0},
            'on_base': {'L': 0, 'R': 0},
            'total_bases': {'L': 0, 'R': 0},
            'score_from_second': {'L': 0, 'R': 0},
            'rating': {'L': 0, 'R': 0},
        }
        for s in ['L', 'R']:
            self.composite_stats['single'][s] = \
                stat_line.base_stats['single_1'][s] + \
                stat_line.base_stats['single_2'][s] + \
                stat_line.base_stats['single_open'][s]
            self.composite_stats['double'][s] = \
                stat_line.base_stats['double_2'][s] + \
                stat_line.base_stats['double_3'][s] + \
                stat_line.base_stats['double_open'][s]
            self.composite_stats['triple'][s] = stat_line.base_stats['triple'][s]
            self.composite_stats['homerun'][s] = stat_line.base_stats['homerun'][s]
            self.composite_stats['hits'][s] = \
                self.composite_stats['single'][s] + \
                self.composite_stats['double'][s] + \
                self.composite_stats['triple'][s] + \
                self.composite_stats['homerun'][s]
            self.composite_stats['on_base'][s] = \
                self.composite_stats['hits'][s] + \
                stat_line.base_stats['walk'][s]
            self.composite_stats['total_bases'][s] = \
                self.composite_stats['hits'][s] + \
                self.composite_stats['double'][s] + \
                (self.composite_stats['triple'][s] * 2) + \
                (self.composite_stats['homerun'][s] * 3)
            self.composite_stats['score_from_second'][s] = \
                self.composite_stats['hits'][s] - \
                (stat_line.base_stats['single_1'][s] +
                 stat_line.base_stats['single_open'][s])

    def add_ballpark_stats(self, stat_line, singles, homeruns):
        single = dict()
        homerun = dict()
        for s in ['L', 'R']:
            singles_to_add = (stat_line.base_stats['ballpark_single'][s] / 20) * singles[s]
            homeruns_to_add = (stat_line.base_stats['ballpark_homerun'][s] / 20) * homeruns[s]
            self.composite_stats['single'][s] += singles_to_add
            self.composite_stats['homerun'][s] += homeruns_to_add
            self.composite_stats['hits'][s] += singles_to_add + homeruns_to_add
            self.composite_stats['on_base'][s] += singles_to_add + homeruns_to_add
            self.composite_stats['total_bases'][s] += singles_to_add + (homeruns_to_add * 4)
            self.composite_stats['score_from_second'][s] += homeruns_to_add
            single[s] = singles_to_add
            homerun[s] = homeruns_to_add
        return single, homerun

    def get_rating(self, stat_line, single, homerun):
        for s in ['L', 'R']:
            self.composite_stats['rating'][s] = \
                (stat_line.base_stats['walk'][s] * 0.036) + \
                ((stat_line.base_stats['single_1'][s] +
                  stat_line.base_stats['single_open'][s] +
                  single[s]) * 0.045) + \
                (stat_line.base_stats['single_2'][s] * 0.045) + \
                (self.composite_stats['double'][s] * 0.064) + \
                (self.composite_stats['triple'][s] * 0.086) + \
                ((self.composite_stats['homerun'][s] + homerun[s]) * 0.098) + \
                (stat_line.base_stats['gbA'][s] * -0.007)


class CompositeStatsHitter(CompositeStats):

    def __init__(self, stat_line, defense, bats, ballpark):
        CompositeStats.__init__(self, stat_line)
        if bats.upper() == 'L':
            single = {'L': ballpark.single_left, 'R': ballpark.single_left}
            homerun = {'L': ballpark.homerun_left, 'R': ballpark.homerun_left}
        elif bats.upper() == 'R':
            single = {'L': ballpark.single_right, 'R': ballpark.single_right}
            homerun = {'L': ballpark.homerun_right, 'R': ballpark.homerun_right}
        elif bats.upper() == 'S':
            single = {'L': ballpark.single_right, 'R': ballpark.single_left}
            homerun = {'L': ballpark.homerun_right, 'R': ballpark.homerun_left}
        singles, homeruns = self.add_ballpark_stats(stat_line, single, homerun)
        self.get_rating(stat_line, singles, homeruns)
        self.composite_stats['defense_rating'] = {
            'c': defense['c'], '1b': defense['1b'],
            '2b': defense['2b'], '3b': defense['3b'],
            'ss': defense['ss'], 'lf': defense['lf'],
            'cf': defense['cf'], 'rf': defense['rf']}
        self.composite_stats['total_ratings'] = {
            'c': {'L': 0, 'R': 0},
            '1b': {'L': 0, 'R': 0},
            '2b': {'L': 0, 'R': 0},
            '3b': {'L': 0, 'R': 0},
            'ss': {'L': 0, 'R': 0},
            'lf': {'L': 0, 'R': 0},
            'cf': {'L': 0, 'R': 0},
            'rf': {'L': 0, 'R': 0}}
        self.get_total_ratings()

    def get_total_ratings(self):
        for s in ['L', 'R']:
            for position in self.composite_stats['defense_rating']:
                if self.composite_stats['defense_rating'][position] == 0:
                    self.composite_stats['total_ratings'][position][s] = 0
                else:
                    self.composite_stats['total_ratings'][position][s] = \
                        self.composite_stats['rating'][s] - \
                        self.composite_stats['defense_rating'][position]


class CompositeStatsPitcher(CompositeStats):

    def __init__(self, stat_line, ballpark):
        CompositeStats.__init__(self, stat_line)
        single = {'L': ballpark.single_left, 'R': ballpark.single_left}
        homerun = {'L': ballpark.homerun_left, 'R': ballpark.homerun_left}
        singles, homeruns = self.add_ballpark_stats(stat_line, single, homerun)
        self.get_rating(stat_line, singles, homeruns)
