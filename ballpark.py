import sql
import os


class Ballpark:
    ballpark_id = ''
    year = 0
    name = ""
    city = ""
    location = ""
    home_team = ""
    single_left = 0
    single_right = 0
    homerun_left = 0
    homerun_right = 0
    custom_park = False
    player_type = 'B'

    def __init__(self, ballpark_id=''):
        if ballpark_id != '':
            ballpark_data = sql.get_ballpark_data(ballpark_id)
        else:
            ballpark_data = ['', 1900, 'None', 'None', 'None', 'NA', 0, 0, 0, 0, 1]
        self.ballpark_id = ballpark_id
        self.year = ballpark_data[1]
        self.location = ballpark_data[2]
        self.name = ballpark_data[3]
        self.city = ballpark_data[4]
        self.state = ballpark_data[5]
        self.single_left = ballpark_data[6]
        self.single_right = ballpark_data[7]
        self.homerun_left = ballpark_data[8]
        self.homerun_right = ballpark_data[9]
        if ballpark_data[10] == 1:
            self.custom_park = True
        else:
            self.custom_park = False
        self.full_name = ballpark_data[2]


def open_ballpark_list(file_name, custom_parks):
    file = open(os.path.join(os.curdir, 'data', 'ballpark_lists', '{}.txt'.format(file_name)))
    data = file.readlines()
    ballpark_list = []
    for line in data:
        line = line.replace('\n', '')
        ballpark_list.append(line)
    if custom_parks:
        custom = ['AVG', 'H0S0', 'H0S20', 'H20S0', 'H20S20']
        ballpark_list.extend(custom)
    return ballpark_list


def load_ballparks(ballpark_list):
    ballparks = []
    for b in ballpark_list:
        ballpark_data = sql.get_ballpark_data(b)
        print(ballpark_data)
        bp = Ballpark(ballpark_data[0])
        ballparks.append(bp)
    return ballparks
