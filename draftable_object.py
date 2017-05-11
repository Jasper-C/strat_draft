from ballpark import Ballpark
from player import Hitter, Pitcher, DoubleDuty


class DraftableObject:
    """
    Docstring:
    drafted : bool
    team, round, pick, draft_id : integer
    object_type : string (1 char)
    dft_object : player or ballpark
    aps : integer
    ratings_position, team_position : string
    pick_value : float
    """
    drafted = False
    team = 0
    round = 0
    pick = 0
    dft_object = None
    draft_id = 0
    object_type = None
    aps = 0
    position = ''
    pick_value = 0.0

    def __init__(self, object_id, draft_id, object_type):
        if object_type == 'B':
            self.dft_object = Ballpark(object_id)
        elif object_type == 'H':
            self.dft_object = Hitter(object_id)
        elif object_type == 'P':
            self.dft_object = Pitcher(object_id)
        elif object_type == 'X':
            self.dft_object = DoubleDuty(object_id)
        self.draft_id = draft_id
        self.object_type = object_type
        self.pick_value = 0

    def make_pick(self, team, rd, pick):
        self.drafted = True
        self.team = team
        self.round = rd
        self.pick = pick

    def remove_pick(self):
        self.drafted = False
        self.team = 0
        self.round = 0
        self.pick = 0

    def adjust_ratings(self, position):
        self.position += position

    def clear_position(self):
        self.position = ''

    def change_pick_value(self, new_value):
        self.pick_value = new_value
