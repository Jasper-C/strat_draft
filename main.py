import sanatize
import install
import ballpark
import player
import sql
import draft as d
import terminal_draft as td


def print_main_menu():
    print("  1- Install Game and data files")
    print("  2- Install a season")
    print("  3- Start a tournament draft")
    print("* 4- Review a tournament draft")
    print("* 5- Continue a saved tournament draft")
    print("* 6- Start a league draft")
    print("* 7- Review a league draft")
    print("* 8- Continue a saved league draft")
    print("  9- Review a player set")
    print("* Selection not yet coded")


def main_menu():
    print_main_menu()
    choice = sanatize.sanitize_int("Enter a selection: ", 1, 9)
    if choice == 1:
        confirm = input('Are you sure, this will erase all data from the database.')
        if confirm.upper() == "Y" or confirm.upper() == "YES":
            install.install()
        else:
            print("Selection not confirmed, no changes made.")
    elif choice == 2:
        year = sanatize.sanitize_int("What Season Would you like to install:", 1901, 2017)
        install.import_season(year)
    elif choice == 3:
        td.run_draft(d.Draft())
    elif choice == 4:
        print("Review Tournament Draft not yet created, try again.")
    elif choice == 5:
        print("Continue Saved Tournament Draft not yet created, try again.")
    elif choice == 6:
        print("League Draft not yet created, try again.")
    elif choice == 7:
        print("Review League Draft not yet created, try again.")
    elif choice == 8:
        print("Continue Saved League Draft not yet created, try again.")
    elif choice == 9:
        player_list = player.open_player_list('1911_test')
        players = player.load_players(player_list)
        for p in players:
            p.display_card()
        input()


def main():
    while True:
        main_menu()


main()
