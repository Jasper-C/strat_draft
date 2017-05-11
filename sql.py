import sqlite3 as sql


# Setup Database with tables
def setup_draft_table():
    con = sql.connect('strat.db')
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Drafts")
        cur.execute("CREATE TABLE Drafts("
                    "Id INTEGER PRIMARY KEY, "
                    "Teams INTEGER, "
                    "Rounds INTEGER, "
                    "Player_Set TEXT, "
                    "Type TEXT, "
                    "Style TEXT, "
                    "Ballparks BOOL, "
                    "Keepers BOOL, "
                    "Pick_Time INTEGER)")


def setup_team_table():
    con = sql.connect('strat.db')
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Teams")
        cur.execute("CREATE TABLE Teams("
                    "Id INTEGER PRIMARY KEY, "
                    "Draft_Id Integer, "
                    "Draft_Position INTEGER, "
                    "Owner TExT)")


def setup_picks_table():
    con = sql.connect('strat.db')
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Picks")
        cur.execute("CREATE TABLE Picks("
                    "Id INTEGER PRIMARY KEY, "
                    "Draft_Id INTEGER, "
                    "Team_Id INTEGER, "
                    "Pick_Number_Draft INTEGER, "
                    "Pick_Number_Round INTEGER, "
                    "Round_Number INTEGER, "
                    "Player_Id TEXT)")


def setup_names_table():
    con = sql.connect('strat.db')
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Names")
        cur.execute("CREATE TABLE Names("
                    "Id TEXT PRIMARY KEY, "
                    "First_Name TEXT, "
                    "Last_Name TEXT)")


def setup_names_data():
    file = open('./data/names.csv', encoding='utf-8')
    data = file.readlines()
    names = []
    for line in data:
        line = line.replace('\n', '')
        line = line.split(',')
        names.append(line)
    add_names_data(names)


def setup_players_table():
    con = sql.connect('strat.db')
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Players")
        cur.execute("CREATE TABLE Players("
                    "PlayerId TEXT, "
                    "CardId TEXT PRIMARY KEY, "
                    "Stock_Team_Id TEXT, "
                    "Year INT, "
                    "Player_Type TEXT, "
                    "Bats TEXT, "
                    "Bunt TEXT, "
                    "Hit_Run TEXT, "
                    "Running INTEGER, "
                    "Power_Left INTEGER, "
                    "Power_Right INTEGER, "
                    "Stealing TEXT, "
                    "Asterisk_Stealing INTEGER, "
                    "Front_Stealing INTEGER, "
                    "Back_Stealing INTEGER, "
                    "Stealing_Lead TEXT, "
                    "FOREIGN KEY(PlayerId) REFERENCES Names(Id) "
                    # "FOREIGN KEY(Stock_Team_Id) REFERENCES Teams(Id)"
                    ")")


def setup_hitters_table():
    con = sql.connect('strat.db')
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Hitters")
        cur.execute("CREATE TABLE Hitters("
                    "CardId TEXT, "
                    "Defense1 TEXT, "
                    "Defense2 TEXT, "
                    "Defense3 TEXT, "
                    "Defense4 TEXT, "
                    "Defense5 TEXT, "
                    "Defense6 TEXT, "
                    "Defense7 TEXT, "
                    "Defense8 TEXT, "
                    "of_arm INTEGER, "
                    "c_arm INTEGER, "
                    "c_t_rtg INTEGER, "
                    "c_bp INTEGER, "
                    "FOREIGN KEY(CardId) REFERENCES Players(CardId)"
                    ")")


def setup_pitchers_table():
    con = sql.connect('strat.db')
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Pitchers")
        cur.execute("CREATE TABLE Pitchers("
                    "CardId TEXT, "
                    "Arm TEXT, "
                    "Endurance_starter INTEGER, "
                    "Endurance_reliever INTEGER, "
                    "Endurance_closer INTEGER, "
                    "Hold INTEGER, "
                    "Wild_pitch INTEGER, "
                    "Balk INTEGER, "
                    "Def_range INTEGER, "
                    "Def_error INTEGER, "
                    "Pitcher_hitting_card INTEGER, "
                    "FOREIGN KEY(CardId) REFERENCES Players(CardId)"
                    ")")


def setup_double_duty_table():
    con = sql.connect('strat.db')
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS DoubleDuty")
        cur.execute("CREATE TABLE DoubleDuty("
                    "CardId TEXT, "
                    "Defense1 TEXT, "
                    "Defense2 TEXT, "
                    "Defense3 TEXT, "
                    "Defense4 TEXT, "
                    "Defense5 TEXT, "
                    "Defense6 TEXT, "
                    "Defense7 TEXT, "
                    "Defense8 TEXT, "
                    "of_arm INTEGER, "
                    "c_arm INTEGER, "
                    "c_t_rtg INTEGER, "
                    "c_bp INTEGER, "
                    "Arm TEXT, "
                    "Endurance_starter INTEGER, "
                    "Endurance_reliever INTEGER, "
                    "Endurance_closer INTEGER, "
                    "Hold INTEGER, "
                    "Wild_pitch INTEGER, "
                    "Balk INTEGER, "
                    "Def_range INTEGER, "
                    "Def_error INTEGER, "
                    "Pitcher_hitting_card INTEGER, "
                    "FOREIGN KEY(CardId) REFERENCES Players(CardId)"
                    ")")


def setup_hitters_results_table():
    con = sql.connect('strat.db')
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS HittersResults")
        cur.execute("CREATE TABLE HittersResults("
                    "LineId INTEGER PRIMARY KEY, "
                    "CardId TEXT, "
                    "Side TEXT, "
                    "Location INTEGER, "
                    "PrimaryResult INTEGER, "
                    "SecondaryResult INTEGER, "
                    "Split INTEGER, "
                    "Injury INTEGER, "
                    "Clutch INTEGER, "
                    "FOREIGN KEY(CardId) REFERENCES Players(CardId)"
                    ")")


def setup_pitchers_results_table():
    con = sql.connect('strat.db')
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS PitchersResults")
        cur.execute("CREATE TABLE PitchersResults("
                    "LineId INTEGER PRIMARY KEY, "
                    "CardId TEXT, "
                    "Side TEXT, "
                    "Location INTEGER, "
                    "PrimaryResult INTEGER, "
                    "SecondaryResult INTEGER, "
                    "Split INTEGER, "
                    "Injury INTEGER, "
                    "Pow INTEGER, "
                    "FOREIGN KEY(CardId) REFERENCES Players(CardId)"
                    ")")


def setup_ballparks_table():
    con = sql.connect('strat.db')
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Ballparks")
        cur.execute("CREATE TABLE Ballparks("
                    "Id TEXT PRIMARY KEY, "
                    "Year INTEGER, "
                    "Location TEXT, "
                    "Name TEXT, "
                    "City TEXT, "
                    "State TEXT, "
                    "single_left INTEGER, "
                    "single_right INTEGER, "
                    "homerun_left INTEGER, "
                    "homerun_right INTEGER, "
                    "custom_park INTEGER)")


# Add Data to tables
def add_draft_data(data):
    try:
        con = sql.connect('strat.db')
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO Drafts VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)", data)
    except sql.IntegrityError:
        print(sql.IntegrityError)


def add_team_data(data):
    pass


def add_picks_data(data):
    pass


def add_names_data(data):
    try:
        con = sql.connect('strat.db')
        with con:
            cur = con.cursor()
            cur.executemany("INSERT INTO Names VALUES(?, ?, ?)", data)
    except sql.IntegrityError:
        print(sql.IntegrityError)


def add_players_data(data):
    try:
        con = sql.connect('strat.db')
        with con:
            cur = con.cursor()
            cur.executemany("INSERT INTO Players VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    except sql.IntegrityError:
        print(sql.IntegrityError)


def add_hitters_data(data):
    try:
        con = sql.connect('strat.db')
        with con:
            cur = con.cursor()
            cur.executemany("INSERT INTO Hitters VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    except sql.IntegrityError:
        print(sql.IntegrityError)


def add_pitchers_data(data):
    try:
        con = sql.connect('strat.db')
        with con:
            cur = con.cursor()
            cur.executemany("INSERT INTO Pitchers VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    except sql.IntegrityError:
        print(sql.IntegrityError)


def add_double_duty_data(data):
    try:
        con = sql.connect('strat.db')
        with con:
            cur = con.cursor()
            cur.executemany("INSERT INTO DoubleDuty "
                            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    except sql.IntegrityError:
        print(sql.IntegrityError)


def add_hitters_results_data(data):
    try:
        con = sql.connect('strat.db')
        with con:
            cur = con.cursor()
            cur.executemany("INSERT INTO HittersResults VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    except sql.IntegrityError:
        print(sql.IntegrityError)


def add_pitchers_results_data(data):
    try:
        con = sql.connect('strat.db')
        with con:
            cur = con.cursor()
            cur.executemany("INSERT INTO PitchersResults VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?)", data)
    except sql.IntegrityError:
        print(sql.IntegrityError)


def add_ballpark_data(data):
    for ballparks in data:
        try:
            con = sql.connect('strat.db')
            with con:
                cur = con.cursor()
                cur.execute("INSERT INTO Ballparks VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", ballparks)
        except sql.IntegrityError:
            print(sql.IntegrityError)


# Get Data From Tables
def get_player_data(card_id):
    con = sql.connect('strat.db')
    with con:
        try:
            cur = con.cursor()
            cur.execute('SELECT * FROM Players '
                        'WHERE CardId = ?', (card_id, ))
            data = cur.fetchone()
        except sql.Error as e:
            print("Error {}".format(e.args))
            data = None
    return data


def get_hitter_data(card_id):
    con = sql.connect('strat.db')
    with con:
        try:
            cur = con.cursor()
            cur.execute('SELECT * FROM Hitters '
                        'WHERE CardId = ?', (card_id, ))
            data = cur.fetchone()
        except sql.Error as e:
            print("Error {}".format(e.args))
            data = None
    return data


def get_pitcher_data(card_id):
    con = sql.connect('strat.db')
    with con:
        try:
            cur = con.cursor()
            cur.execute('SELECT * FROM Pitchers '
                        'WHERE CardId = ?', (card_id, ))
            data = cur.fetchone()
        except sql.Error as e:
            print("Error {}".format(e.args))
            data = None
    return data


def get_player_name(player_id):
    con = sql.connect('strat.db')
    with con:
        try:
            cur = con.cursor()
            cur.execute('SELECT * FROM Names '
                        'WHERE ID = ?', (player_id, ))
            data = cur.fetchone()
        except sql.Error as e:
            print("Error {}".format(e.args))
            data = None
    return data


def get_hitter_results_data(card_id):
    con = sql.connect('strat.db')
    with con:
        try:
            cur = con.cursor()
            cur.execute('SELECT * FROM HittersResults '
                        'WHERE CardId = ?', (card_id, ))
            data = cur.fetchall()
        except sql.Error as e:
            print("Error {}".format(e.args))
            data = None
    return data


def get_pitcher_results_data(card_id):
    con = sql.connect('strat.db')
    with con:
        try:
            cur = con.cursor()
            cur.execute('SELECT * FROM PitchersResults '
                        'WHERE CardId = ?', (card_id, ))
            data = cur.fetchall()
        except sql.Error as e:
            print("Error {}".format(e.args))
            data = None
    return data


def get_ballpark_data(ballpark_id):
    con = sql.connect('strat.db')
    with con:
        try:
            cur = con.cursor()
            cur.execute('SELECT * FROM Ballparks '
                        'WHERE Id = ?', (ballpark_id, ))
            data = cur.fetchone()
        except sql.Error as e:
            print("Error {}".format(e.args))
            data = None
    return data


def list_ballparks():
    con = sql.connect('strat.db')
    with con:
        try:
            cur = con.cursor()
            cur.execute('SELECT * FROM Ballparks '
                        'WHERE single_right > 15')
            data = cur.fetchall()

            for line in data:
                print(line)

        except sql.Error:
            print("Error {}".format(sql.Error))
            data = None

    return data
