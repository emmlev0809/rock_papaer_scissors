# Import Module
import tkinter as tk
from game_objects import Game, PlayerObject, ComputerPlayer
from tkinter import ttk


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.options_page = OptionsPage(self)
        # self.options_page.pack()
        title = "☆ Rock Paper Scissors ☆" \
                "\n(Lizard Spock)"

        self.human_name = "Player"
        self.max_rounds = 1

        title_label = tk.Label(self, text=title, fg="red",  font=("Sawarabi Mincho", 20))
        self.frames = {
            "frame_one": OptionsPage(self),
            "frame_two": GamePage(self)
        }
        title_label.pack(side=tk.TOP)
        self.show_frame("frame_one")


    def show_frame(self, frame):
        widgets = self.winfo_children()

        for w in widgets:
            if w.winfo_class() == "Frame":
                w.pack_forget()

        frameshow = self.frames[frame]
        frameshow.pack(side=tk.TOP)
        frameshow.setup()



class OptionsPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.controller = master
        self.is_spock = False


        self.input_name_text = tk.Label(self,
                                        text="☆ Enter player name.",
                                        font=("Sawarabi Mincho", 10)
                                        )
        self.input_rounds_text = tk.Label(self,
                                          text="☆ Enter round number.",
                                          font=("Sawarabi Mincho", 10)
                                          )

        self.start_game_button = tk.Button(self, text="Start Game",
                                           fg="white", bg="red", font=("Sawarabi Mincho",10),
                                           command = self.next_page
                                           )

        self.enter_name_box = tk.Entry(self, width=40)
        self.enter_name_box.insert(0, "Player")
        self.enter_rounds_box = tk.Entry(self, width=40)
        self.enter_rounds_box.insert(0, "1")

        self.place_widgets()

    def next_page(self):
        if self.enter_name_box.get():
            self.controller.human_name = self.enter_name_box.get()

        if self.enter_rounds_box.get():
            self.controller.max_rounds = self.enter_rounds_box.get()
        self.controller.show_frame("frame_two")


    def place_widgets(self):
        for i in range(0, 3):
            self.grid_columnconfigure(i, weight=1, uniform="Column")

        self.enter_name_box.grid(row=1, column=1, padx=5, pady=5, sticky="NEWS", columnspan=3)
        self.enter_rounds_box.grid(row=2, column=1, padx=5, pady=5, sticky="NEWS", columnspan=3)
        self.start_game_button.grid(row=7, column=1, padx=5, pady=5, sticky="NES")


        self.input_name_text.grid(row=1, column=0, padx=5, pady=5, sticky="NEWS")
        self.input_rounds_text.grid(row=2, column=0, padx=5, pady=5, sticky="NEWS")

    def setup(self):
        pass

class GamePage(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.controller = master
        self.is_spock = False
        self.objects = ['rock', 'paper', 'scissors', 'lizard', 'spock']


    def last_page(self):
        self.controller.show_frame("frame_one")

    def switch_game_mode(self):
        if self.is_spock:
            self.is_spock = False
        else:
            self.is_spock = True

    def setup(self):

        self.game = Game()
        self.players = self.game.players


        self.player_rock_button = tk.Button(self, text="Rock",
                                            fg="white", bg="red", font=("Sawarabi Mincho", 10),
                                            activebackground='yellow', command=self.play_round_rock)
        self.player_paper_button = tk.Button(self, text="Paper",
                                             fg="white", bg="red", font=("Sawarabi Mincho", 10),
                                             activebackground='yellow', command=self.play_round_paper)
        self.player_scissors_button = tk.Button(self, text="Scissors",
                                                fg="white", bg="red", font=("Sawarabi Mincho", 10),
                                                activebackground='yellow', command=self.play_round_scissors)
        self.player_lizard_button = tk.Button(self, text="Lizard",
                                                fg="white", bg="red", font=("Sawarabi Mincho", 10),
                                                activebackground='yellow', command=self.play_round_lizard)
        self.player_spock_button = tk.Button(self, text="Spock",
                                                fg="white", bg="red", font=("Sawarabi Mincho", 10),
                                                activebackground='yellow', command=self.play_round_spock)

        self.computer_rock_button = tk.Button(self, text="Rock",
                                              fg="white", bg="blue", font=("Sawarabi Mincho", 10),
                                              state="disable")
        self.computer_paper_button = tk.Button(self, text="Paper",
                                               fg="white", bg="blue", font=("Sawarabi Mincho", 10),
                                               state="disable")
        self.computer_scissors_button = tk.Button(self, text="Scissors",
                                                  fg="white", bg="blue", font=("Sawarabi Mincho", 10),
                                                  state="disable")
        self.computer_lizard_button = tk.Button(self, text="Lizard",
                                               fg="white", bg="blue", font=("Sawarabi Mincho", 10),
                                               state="disable")
        self.computer_spock_button = tk.Button(self, text="Spock",
                                                  fg="white", bg="blue", font=("Sawarabi Mincho", 10),
                                                  state="disable")

        self.back_button = tk.Button(self, text="Back to menu",
                                     fg="white", bg="red", font=("Sawarabi Mincho", 10),
                                     activebackground='yellow', command=self.last_page)

        self.switch_button = tk.Button(self, text="Switch game mode",
                                       fg="white", bg="red", font=("Sawarabi Mincho", 10),
                                       activebackground='yellow', command=self.switch_game_mode)


        for w in (self.player_rock_button, self.player_paper_button, self.player_scissors_button, self.player_lizard_button, self.player_spock_button):
            w.config(state="normal", bg = "red", fg = "white")


        self.game.add_human_player(self.controller.human_name)
        self.game.add_computer_player()

        self.game.set_max_rounds(int(self.controller.max_rounds))


        self.player_text = tk.Label(self,
                                        text=f"{self.controller.human_name}\n(Score: 0)",
                                        font=("Sawarabi Mincho", 10)
                                        )

        self.computer_text = tk.Label(self,
                                      text="Computer\n(Score: 0)",
                                      font=("Sawarabi Mincho", 10)
                                      )

        self.rounds_text = tk.Label(self,
                                          text=f"Round {self.game.current_round} / {self.game.max_rounds}",
                                          font=("Sawarabi Mincho", 10)
                                          )

        self.round_info_text = tk.Label(self,
                                          text=f"☆ Input your move!",
                                          font=("Sawarabi Mincho", 10)
                                          )

        self.place_widgets()


    def colour_change(self, user, object, colour):
        if user == "player":
            if object == "rock":

                if colour == "yellow":
                    self.player_rock_button.configure(text="Rock", fg="black", bg="yellow", font=("Sawarabi Mincho", 10),
                                                      activebackground='yellow', command=self.play_round_rock)
                elif colour == "red":
                    self.player_rock_button.configure(text="Rock", fg="white", bg="red", font=("Sawarabi Mincho", 10),
                                                      activebackground='yellow', command=self.play_round_rock)

            elif object == "paper":
                
                if colour == "yellow":
                    self.player_paper_button.configure(text="Paper", fg="black", bg="yellow", font=("Sawarabi Mincho", 10),
                                                      activebackground='yellow', command=self.play_round_paper)
                elif colour == "red":
                    self.player_paper_button.configure(text="Paper", fg="white", bg="red", font=("Sawarabi Mincho", 10),
                                                      activebackground='yellow', command=self.play_round_paper)
            elif object == "scissors":
                
                if colour == "yellow":
                    self.player_scissors_button.configure(text="Scissors", fg="black", bg="yellow", font=("Sawarabi Mincho", 10),
                                                      activebackground='yellow', command=self.play_round_scissors)
                elif colour == "red":
                    self.player_scissors_button.configure(text="Scissors", fg="white", bg="red", font=("Sawarabi Mincho", 10),
                                                      activebackground='yellow', command=self.play_round_scissors)

            elif object == "lizard":

                if colour == "yellow":
                    self.player_lizard_button.configure(text="Lizard", fg="black", bg="yellow",
                                                      font=("Sawarabi Mincho", 10),
                                                      activebackground='yellow', command=self.play_round_lizard)
                elif colour == "red":
                    self.player_lizard_button.configure(text="Lizard", fg="white", bg="red",
                                                      font=("Sawarabi Mincho", 10),
                                                      activebackground='yellow', command=self.play_round_lizard)
            elif object == "spock":

                if colour == "yellow":
                    self.player_spock_button.configure(text="Spock", fg="black", bg="yellow",
                                                      font=("Sawarabi Mincho", 10),
                                                      activebackground='yellow', command=self.play_round_spock)
                elif colour == "red":
                    self.player_spock_button.configure(text="Spock", fg="white", bg="red",
                                                      font=("Sawarabi Mincho", 10),
                                                      activebackground='yellow', command=self.play_round_spock)
        elif user == "computer":
            if object == "rock":
                if colour == "blue":
                    self.computer_rock_button.configure(text="Rock", fg="white", bg="blue", font=("Sawarabi Mincho", 10),
                                                      activebackground='yellow', state="disable")
                elif colour == "yellow-d":
                    self.computer_rock_button.configure(text="Rock", fg="black", bg="yellow",
                                                      font=("Sawarabi Mincho", 10),
                                                      activebackground='yellow', state="disable")
            elif object == "paper":
                if colour == "blue":
                    self.computer_paper_button.configure(text="Paper", fg="white", bg="blue", font=("Sawarabi Mincho", 10),
                                                      activebackground='yellow', state="disable")
                elif colour == "yellow-d":
                    self.computer_paper_button.configure(text="Paper", fg="black", bg="yellow",
                                                      font=("Sawarabi Mincho", 10),
                                                      activebackground='yellow', state="disable")

            elif object == "scissors":
                if colour == "blue":
                    self.computer_scissors_button.configure(text="Scissors", fg="white", bg="blue",
                                                      font=("Sawarabi Mincho", 10),
                                                      activebackground='yellow', state="disable")
                elif colour == "yellow-d":
                    self.computer_scissors_button.configure(text="Scissors", fg="black", bg="yellow",
                                                      font=("Sawarabi Mincho", 10),
                                                      activebackground='yellow', state="disable")
            elif object == "lizard":
                if colour == "blue":
                    self.computer_lizard_button.configure(text="Lizard", fg="white", bg="blue",
                                                      font=("Sawarabi Mincho", 10),
                                                      activebackground='yellow', state="disable")
                elif colour == "yellow-d":
                    self.computer_lizard_button.configure(text="Lizard", fg="black", bg="yellow",
                                                      font=("Sawarabi Mincho", 10),
                                                      activebackground='yellow', state="disable")

            elif object == "spock":
                if colour == "blue":
                    self.computer_spock_button.configure(text="Spock", fg="white", bg="blue",
                                                      font=("Sawarabi Mincho", 10),
                                                      activebackground='yellow', state="disable")
                elif colour == "yellow-d":
                    self.computer_spock_button.configure(text="Spock", fg="black", bg="yellow",
                                                      font=("Sawarabi Mincho", 10),
                                                      activebackground='yellow', state="disable")


    def play_round_rock(self):
        self.players[0].choose_object("rock")

        for e in self.objects:
            self.colour_change("player", e, "red")
        self.colour_change("player", "rock", "yellow")

        self.play_round()

    def play_round_paper(self):
        self.players[0].choose_object("paper")

        for e in self.objects:
            self.colour_change("player", e, "red")
        self.colour_change("player", "paper", "yellow")

        self.play_round()

    def play_round_scissors(self):
        self.players[0].choose_object("scissors")

        for e in self.objects:
            self.colour_change("player", e, "red")
        self.colour_change("player", "scissors", "yellow")

        self.play_round()

    def play_round_lizard(self):
        self.players[0].choose_object("lizard")

        for e in self.objects:
            self.colour_change("player", e, "red")
        self.colour_change("player", "lizard", "yellow")

        self.play_round()

    def play_round_spock(self):
        self.players[0].choose_object("spock")

        for e in self.objects:
            self.colour_change("player", e, "red")
        self.colour_change("player", "spock", "yellow")

        self.play_round()

    def play_round(self):

        self.players[1].choose_object()


        if self.players[1].current_object.name == "rock":
            for e in self.objects:
                self.colour_change("computer", e, "blue")
            self.colour_change("computer", "rock", "yellow-d")

        elif self.players[1].current_object.name == "paper":
            for e in self.objects:
                self.colour_change("computer", e, "blue")
            self.colour_change("computer", "paper", "yellow-d")

        elif self.players[1].current_object.name == "scissors":
            for e in self.objects:
                self.colour_change("computer", e, "blue")
            self.colour_change("computer", "scissors", "yellow-d")

        elif self.players[1].current_object.name == "lizard":
            for e in self.objects:
                self.colour_change("computer", e, "blue")
            self.colour_change("computer", "lizard", "yellow-d")

        elif self.players[1].current_object.name == "spock":
            for e in self.objects:
                self.colour_change("computer", e, "blue")
            self.colour_change("computer", "spock", "yellow-d")


        self.game.find_winner()
        self.round_info_text.config( text = f"{self.game.report_winner()}")

        self.rounds_text.config(
                                          text=f"Round {self.game.current_round} / {self.game.max_rounds}",
                                          font=("Sawarabi Mincho", 10)
                                          )
        self.player_text.config( text=f"{self.controller.human_name}\n(Score: {self.game.players[0].score})",
                                        font=("Sawarabi Mincho", 10))

        self.computer_text.config( text=f"Computer\n(Score: {self.game.players[1].score})",
                                        font=("Sawarabi Mincho", 10))

        if self.game.current_round == self.game.max_rounds:
            self.round_info_text.config( text = f"☆ Game over!")
            for w in (self.player_rock_button, self.player_paper_button, self.player_scissors_button, self.player_lizard_button, self.player_spock_button):
                w.config(state="disabled", bg = "red", fg = "white")

            for w in (self.computer_rock_button, self.computer_paper_button, self.computer_scissors_button, self.computer_lizard_button, self.computer_spock_button):
                w.config(state="disabled", bg = "blue", fg = "white")

        else:
            self.game.next_round()

    def place_widgets(self):

        for i in range(0,6):
            self.grid_columnconfigure(i, weight=1, uniform="Column")
        for i in range(0,6):
            self.grid_rowconfigure(i, weight=1, uniform="Row")

        self.player_rock_button.grid(row=1, column=1, padx=5, pady=5, sticky="NEWS")
        self.player_paper_button.grid(row=1, column=2, padx=5, pady=5, sticky="NEWS")
        self.player_scissors_button.grid(row=1, column=3, padx=5, pady=5, sticky="NEWS")
        self.player_lizard_button.grid(row=1, column=4, padx=5, pady=5, sticky="NEWS")
        self.player_spock_button.grid(row=1, column=5, padx=5, pady=5, sticky="NEWS")

        self.computer_rock_button.grid(row=2, column=1, padx=5, pady=5, sticky="NEWS")
        self.computer_paper_button.grid(row=2, column=2, padx=5, pady=5, sticky="NEWS")
        self.computer_scissors_button.grid(row=2, column=3, padx=5, pady=5, sticky="NEWS")
        self.computer_lizard_button.grid(row=2, column=4, padx=5, pady=5, sticky="NEWS")
        self.computer_spock_button.grid(row=2, column=5, padx=5, pady=5, sticky="NEWS")

        self.back_button.grid(row=4, column=3, padx=5, pady=5, sticky="NEWS")

        self.computer_text.grid(row=2, column=0, padx=5, pady=5, sticky="NEWS")
        self.player_text.grid(row=1, column=0, padx=5, pady=5, sticky="NEWS")

        self.rounds_text.grid(row=3, column=1, padx=5, pady=5, sticky="NEWS")


        self.round_info_text.grid(row=3, column=3, padx=5, pady=5, sticky="NEWS", )


if __name__ == '__main__':
    main_app = GUI()
    main_app.mainloop()

