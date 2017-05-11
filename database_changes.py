import sql
import os.path as path


def add_ballparks(file_name, year):
    file = open(path.join('data', str(year), file_name))
    data = file.readlines()
    ballparks = []
    for line in data:
        line = line.replace('\n', '')
        line = line.split(',')
        for i in [1, 6, 7, 8, 9, 10]:
            line[i] = int(line[i])
        ballparks.append(line)
    sql.add_ballpark_data(ballparks)


def add_default_ballparks():
    file = open(path.join('data', 'custom_ballparks.csv'))
    data = file.readlines()
    ballparks = []
    for line in data:
        line = line.replace('\n', '')
        line = line.split(',')
        for i in [1, 6, 7, 8, 9, 10]:
            line[i] = int(line[i])
        ballparks.append(line)
    sql.add_ballpark_data(ballparks)


def add_players_to_db(file_name, year):
    file = open(path.join('data', str(year), file_name))
    data = file.readlines()
    players = []
    for line in data:
        line = line.replace('\n', '')
        line = line.split(',')
        for i in [3, 8, 9, 10, 12, 13, 14]:
            line[i] = int(line[i])
        players.append(line)
    sql.add_players_data(players)


def add_hitters_to_db(file_name, year):
    file = open(path.join('data', str(year), file_name))
    data = file.readlines()
    hitters = []
    for line in data:
        line = line.replace('\n', '')
        line = line.split(',')
        for i in [9, 10, 11, 12]:
            if line[i] == '':
                line[i] = 0
            else:
                line[i] = int(line[i])
        hitters.append(line)
    sql.add_hitters_data(hitters)


def add_pitchers_to_db(file_name, year):
    file = open(path.join('data', str(year), file_name))
    data = file.readlines()
    pitchers = []
    for line in data:
        line = line.replace('\n', '')
        line = line.split(',')
        for i in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
            if line[i] == 'NULL':
                line[i] = 0
            else:
                line[i] = int(line[i])
        pitchers.append(line)
    sql.add_pitchers_data(pitchers)


def add_double_duty_to_db(file_name, year):
    file = open(path.join('data', str(year), file_name))
    data = file.readlines()
    players = []
    for line in data:
        line = line.replace('\n', '')
        line = line.split(',')
        for i in [9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22]:
            if line[i] == 'NULL' or line[i] == '':
                line[i] = 0
            else:
                line[i] = int(line[i])
        players.append(line)
    sql.add_double_duty_data(players)


def add_hitter_results_to_db(file_name, year):
    file = open(path.join('data', str(year), file_name))
    data = file.readlines()
    hitter_results = []
    for line in data:
        line = line.replace('\n', '')
        line = line.split(',')
        hitter_results.append(line)
    sql.add_hitters_results_data(hitter_results)


def add_pitcher_results_to_db(file_name, year):
    file = open(path.join('data', str(year), file_name))
    data = file.readlines()
    pitcher_results = []
    for line in data:
        line = line.replace('\n', '')
        line = line.split(',')
        pitcher_results.append(line)
    sql.add_pitchers_results_data(pitcher_results)


def add_blank_hitters():
    file = open(path.join('data', 'custom_players.csv'))
    data = file.readlines()
    players = []
    for line in data:
        line = line.replace('\n', '')
        line = line.split(',')
        for i in [3, 8, 9, 10, 12, 13, 14]:
            line[i] = int(line[i])
        players.append(line)
    sql.add_players_data(players)
    file = open(path.join('data', 'custom_hitters.csv'))
    data = file.readlines()
    hitters = []
    for line in data:
        line = line.replace('\n', '')
        line = line.split(',')
        for i in [9, 10, 11, 12]:
            if line[i] == '':
                line[i] = 0
            else:
                line[i] = int(line[i])
        hitters.append(line)
    sql.add_hitters_data(hitters)
    file = open(path.join('data', 'custom_hitters_results.csv'))
    data = file.readlines()
    hitter_results = []
    for line in data:
        line = line.replace('\n', '')
        line = line.split(',')
        hitter_results.append(line)
    sql.add_hitters_results_data(hitter_results)

