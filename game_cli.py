from game_objects import Game, PlayerObject, ComputerPlayer

#command line interface

class CommandLine:
    def __init__(self):
        self.game = Game()
        self.players = self.game.players

    def set_up(self):
        print("WELCOME TO GAME! IT IS ROCK PAPER SCISSORS LIZARD SPOCK")
        human_name = input("WHAT IS YOUR NAME")
        self.game.add_human_player(human_name)
        self.game.add_computer_player()
        print("COMPUTER PLAYER ADDED")


    def input_max_rounds(self):
        rounds = int(input("HOW MANY ROUNDS"))
        self.game.set_max_rounds(rounds)

    def get_choices(self):
        choice = input("WHAT DO YOU CHOOSE")
        self.players[0].choose_object(choice)
        self.players[1].choose_object()

    def run_game(self):
        self.game.next_round()
        self.get_choices()
        self.game.find_winner()
        print (self.game.report_round())
        print (self.game.report_winner())
        print (self.game.report_score())


    def run_sequence(self):
        self.set_up()
        self.input_max_rounds()
        while self.game.current_round < self.game.max_rounds:
            self.run_game()


if __name__ == "__main__":
    cli = CommandLine()
    cli.run_sequence()