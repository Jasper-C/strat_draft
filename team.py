from ballpark import Ballpark


class Team:
    def __init__(self, name):
        self.name = name
        self.roster = []
        self.ballpark = Ballpark()
        self.suggest_park = 'AVG'
        self.team_values = {
            'sp': [0, 0, 0, 0],
            'rp': {'L': [0, 0, 0, 0], 'R': [0, 0, 0, 0]},
            'ph': {'vs L': {'L': [0, 0, 0, 0], 'R': [0, 0, 0, 0]},
                   'vs R': {'L': [0, 0, 0, 0], 'R': [0, 0, 0, 0]}},
            'c': {'L': 0, 'R': 0},
            '1b': {'L': 0, 'R': 0},
            '2b': {'L': 0, 'R': 0},
            '3b': {'L': 0, 'R': 0},
            'ss': {'L': 0, 'R': 0},
            'lf': {'L': 0, 'R': 0},
            'cf': {'L': 0, 'R': 0},
            'rf': {'L': 0, 'R': 0},
        }
        self.team_rating = 0

    def __str__(self):
        return self.name

    def change_name(self, name):
        self.name = name

    def add_player(self, player):
        self.roster.append(player)

    def change_ballpark(self, ballpark):
        self.ballpark = ballpark
        self.suggest_park = ballpark.ballpark_id

    def change_ballpark_suggestions(self, ballpark_id):
        self.suggest_park = ballpark_id

    def update_team_values(self, values):
        for s in ['L', 'R']:
            for pos in self.team_values:
                self.team_values[pos][s] = values[pos][s]

    def update_roster(self, roster):
        self.roster = roster[:]

    def update_team_values(self, replacement_values):
        pass
