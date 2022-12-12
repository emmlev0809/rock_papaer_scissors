from game_objects import Game, PlayerObject, ComputerPlayer

#command line interface

class CommandLine:
    def __init__(self):
        self.game = Game()
        self.players = self.game.players

    def set_up(self):
        print("welcome to rock paper scissors lizard spock!! ")
        human_name = input("what is your name :)")

        self.game.add_human_player(human_name)
        self.game.add_computer_player()
        print("a computer player is added!")


    def input_max_rounds(self):
        rounds = input("how many rounds would you like?")
        while rounds.isdigit() is False:
            rounds = input("input a number for rounds you would like!")
        self.game.set_max_rounds(int(rounds))

    def get_choices(self):
        choice = input("\nchoose a move!")
        while choice not in self.game.allowable_objects:
            choice = input("that isn't a valid move...\nchoose a move!")
        self.players[0].choose_object(choice)
        self.players[1].choose_object()

    def run_game(self):
        self.game.next_round()
        self.get_choices()
        self.game.find_winner()
        print(self.game.report_round())
        print(self.game.report_winner())
        print(self.game.report_score())


    def run_sequence(self):
        self.set_up()
        self.input_max_rounds()
        while self.game.current_round < self.game.max_rounds:
            self.run_game()
        print("GAME DONE")
        self.game.reset()

if __name__ == "__main__":
    cli = CommandLine()
    cli.run_sequence()