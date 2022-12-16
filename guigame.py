# Import Module
import tkinter as tk
from tkinter import ttk


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.options_page = OptionsPage(self)
        # self.options_page.pack()
        title = "Emma's super app"
        title_label = tk.Label(self, text=title, bg="purple", fg="yellow", width=40, font=("Sawarabi Mincho", 20))
        self.frames = {
            "frame_one": OptionsPage(self)
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
        frameshow.set_up()


class OptionsPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.config(bg="red")

        self.rps_text = tk.Label(self,
                                 text="Rock Paper Scissors (Lizard Spock)",
                                 font=("Sawarabi Mincho", 20)
                                 )
        self.input_name_text = tk.Label(self,
                                        text="Enter player name.",
                                        font=("Arial", 10)
                                        )
        self.input_rounds_text = tk.Label(self,
                                          text="Enter round number.",
                                          font=("Arial", 10)
                                          )

        self.start_game_button = tk.Button(self, text="Start Game",
                                           fg="white", bg="red")
        self.enter_name_box = tk.Entry(self, width=40)
        self.enter_rounds_box = tk.Entry(self, width=40)

        # self.rps_text.grid(row=0, column=0)


        self.place_widgets()

    def place_widgets(self):
        self.grid_columnconfigure(0, weight=1, uniform="Column")
        self.grid_columnconfigure(1, weight=1, uniform="Column")
        self.grid_columnconfigure(2, weight=1, uniform="Column")
        self.grid_columnconfigure(3, weight=1, uniform="Column")

        self.enter_name_box.grid(row=1, column=1, padx=5, pady=5, sticky="W", columnspan=3)
        self.enter_rounds_box.grid(row=2, column=1, padx=5, pady=5, sticky="W", columnspan=3)
        self.start_game_button.grid(row=7, column=1, padx=5, pady=5, sticky="SW")
        self.rps_text.grid(row=0, column=0, padx=5, pady=5, sticky="w", columnspan=3)

        self.input_name_text.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.input_rounds_text.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    def set_up(self):
        pass

class GamePage(tk.Frame):
    pass


if __name__ == '__main__':
    main_app = GUI()
    main_app.mainloop()
