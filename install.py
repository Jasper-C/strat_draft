import sql
import database_changes as dc


def setup_db():
    sql.setup_draft_table()
    sql.setup_team_table()
    sql.setup_picks_table()
    sql.setup_names_table()
    sql.setup_names_data()
    sql.setup_players_table()
    sql.setup_hitters_table()
    sql.setup_pitchers_table()
    sql.setup_double_duty_table()
    sql.setup_hitters_results_table()
    sql.setup_pitchers_results_table()
    sql.setup_ballparks_table()
    dc.add_default_ballparks()
    dc.add_blank_hitters()


def import_season(year):
    dc.add_ballparks("{}_ballparks.csv".format(year), year)
    dc.add_players_to_db("{}_players.csv".format(year), year)
    dc.add_hitters_to_db("{}_hitters.csv".format(year), year)
    dc.add_pitchers_to_db("{}_pitchers.csv".format(year), year)
    try:
        dc.add_double_duty_to_db("{}_double_duty.csv".format(year), year)
    except FileNotFoundError:
        pass
    dc.add_hitter_results_to_db("{}_hitters_results.csv".format(year), year)
    dc.add_pitcher_results_to_db("{}_pitchers_results.csv".format(year), year)


def install():
    setup_db()
