from coup import CoupGame

def run_game(game):
    game.play_game()


def main():
    print('Welcome to Coup!')
    print('Enter your name to play:')
    name = input()

    num_players = 0
    while True:
        try:
            print('Hi '+ name + ' how many players would you like to play with?')
            entry = input()
            num_players = int(entry)
            if num_players < 3 or num_players > 6:
                raise ValueError()
            break
        except ValueError:
            print('Please enter an integer between 3-6')
    
    game = CoupGame(num_players, name)
    run_game(game)
    

if __name__ == "__main__":
    main()
    