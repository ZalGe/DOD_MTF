import customtkinter
import os
from Functionality import play_pong


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
customtkinter.deactivate_automatic_dpi_awareness()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self._width = self.winfo_screenwidth()
        self._height = self.winfo_screenheight()
        self.attributes('-fullscreen', True)
        self.state('zoomed')
        # self.geometry(f"{1100}x{580}")

        # configure grid layout (7x3)
        # self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure((0,1,2), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

        # create side_menu frame with widgets
        self.side_menu_frame = customtkinter.CTkFrame(self, width=int(self._width/8), corner_radius=15)
        self.side_menu_frame.grid(row=0, column=0, rowspan=7, sticky="nsew")
        self.side_menu_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.side_menu_frame, text="Menu", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.side_menu_button_1 = customtkinter.CTkButton(self.side_menu_frame, height=55, text="Add new game", command=self.side_menu_button_event)
        self.side_menu_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.side_menu_button_2 = customtkinter.CTkButton(self.side_menu_frame, height=55, text="Delete game", command=self.side_menu_button_event)
        self.side_menu_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.side_menu_button_3 = customtkinter.CTkButton(self.side_menu_frame, height=55, text="Quit", command=self.quit)
        self.side_menu_button_3.grid(row=3, column=0, padx=20, pady=100)
        self.appearance_mode_label = customtkinter.CTkLabel(self.side_menu_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.side_menu_frame, height=55, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.side_menu_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.side_menu_frame, height=55, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create scrollable core_game_menu frame
        self.core_game_menu_frame = customtkinter.CTkScrollableFrame(self, width=int(int((self._width - self._width / 8) / 2)), label_text="Select core game")
        self.core_game_menu_frame.grid(row=0, column=1, padx=(20, 0), pady=(40, 0), rowspan=3, sticky="nsew")
        self.core_game_menu_frame.grid_columnconfigure(0, weight=1)
        self.core_game_menu_button_1 = customtkinter.CTkButton(self.core_game_menu_frame, text="Pong", width=int((self._width - self._width / 8) / 2), height=55, command=play_pong)
        self.core_game_menu_button_1.grid(row=1, column=1, padx=0, pady=10)
        self.core_game_menu_button_2 = customtkinter.CTkButton(self.core_game_menu_frame, text="Flappy bird", width=int((self._width - self._width / 8) / 2), height=55, command=self.side_menu_button_event)
        self.core_game_menu_button_2.grid(row=2, column=1, padx=0, pady=10)
        self.core_game_menu_button_3 = customtkinter.CTkButton(self.core_game_menu_frame, text="Chrome Dino", width=int((self._width - self._width / 8) / 2), height=55, command=self.side_menu_button_event)
        self.core_game_menu_button_3.grid(row=3, column=1, padx=0, pady=10)
        self.core_game_menu_button_4 = customtkinter.CTkButton(self.core_game_menu_frame, text="Game 4", width=int((self._width - self._width / 8) / 2), height=55, command=self.side_menu_button_event)
        self.core_game_menu_button_4.grid(row=4, column=1, padx=0, pady=10)
        self.core_game_menu_button_5 = customtkinter.CTkButton(self.core_game_menu_frame, text="Game 5", width=int((self._width - self._width / 8) / 2), height=55, command=self.side_menu_button_event)
        self.core_game_menu_button_5.grid(row=5, column=1, padx=0, pady=10)
        self.core_game_menu_button_6 = customtkinter.CTkButton(self.core_game_menu_frame, text="Game 6", width=int((self._width - self._width / 8) / 2), height=55, command=self.side_menu_button_event)
        self.core_game_menu_button_6.grid(row=6, column=1, padx=0, pady=10)
        self.core_game_menu_button_7 = customtkinter.CTkButton(self.core_game_menu_frame, text="Game 7", width=int((self._width - self._width / 8) / 2), height=55, command=self.side_menu_button_event)
        self.core_game_menu_button_7.grid(row=7, column=1, padx=0, pady=10)
        self.core_game_menu_button_8 = customtkinter.CTkButton(self.core_game_menu_frame, text="Game 8", width=int((self._width - self._width / 8) / 2), height=55, command=self.side_menu_button_event)
        self.core_game_menu_button_8.grid(row=8, column=1, padx=0, pady=10)

        # create scrollable add_game_menu frame
        self.add_game_menu_frame = customtkinter.CTkScrollableFrame(self, width=int(int((self._width - self._width / 8) / 2)), label_text="Select added game")
        self.add_game_menu_frame.grid(row=3, column=1, padx=(20, 0), pady=(20, 0), rowspan=3, sticky="nsew")
        self.add_game_menu_frame.grid_columnconfigure(0, weight=1)
        self.add_game_menu_button_1 = customtkinter.CTkButton(self.add_game_menu_frame, text="Game 1", width=int((self._width - self._width / 8) / 2), height=55, command=self.side_menu_button_event)
        self.add_game_menu_button_1.grid(row=1, column=1, padx=0, pady=10)
        self.add_game_menu_button_2 = customtkinter.CTkButton(self.add_game_menu_frame, text="Game 2", width=int((self._width - self._width / 8) / 2), height=55, command=self.side_menu_button_event)
        self.add_game_menu_button_2.grid(row=2, column=1, padx=0, pady=10)
        self.add_game_menu_button_3 = customtkinter.CTkButton(self.add_game_menu_frame, text="Game 3", width=int((self._width - self._width / 8) / 2), height=55, command=self.side_menu_button_event)
        self.add_game_menu_button_3.grid(row=3, column=1, padx=0, pady=10)
        self.add_game_menu_button_4 = customtkinter.CTkButton(self.add_game_menu_frame, text="Game 4", width=int((self._width - self._width / 8) / 2), height=55, command=self.side_menu_button_event)
        self.add_game_menu_button_4.grid(row=4, column=1, padx=0, pady=10)
        self.add_game_menu_button_5 = customtkinter.CTkButton(self.add_game_menu_frame, text="Game 5", width=int((self._width - self._width / 8) / 2), height=55, command=self.side_menu_button_event)
        self.add_game_menu_button_5.grid(row=5, column=1, padx=0, pady=10)
        self.add_game_menu_button_6 = customtkinter.CTkButton(self.add_game_menu_frame, text="Game 6", width=int((self._width - self._width / 8) / 2), height=55, command=self.side_menu_button_event)
        self.add_game_menu_button_6.grid(row=6, column=1, padx=0, pady=10)
        self.add_game_menu_button_7 = customtkinter.CTkButton(self.add_game_menu_frame, text="Game 7", width=int((self._width - self._width / 8) / 2), height=55, command=self.side_menu_button_event)
        self.add_game_menu_button_7.grid(row=7, column=1, padx=0, pady=10)
        self.add_game_menu_button_8 = customtkinter.CTkButton(self.add_game_menu_frame, text="Game 8", width=int((self._width - self._width / 8) / 2), height=55, command=self.side_menu_button_event)
        self.add_game_menu_button_8.grid(row=8, column=1, padx=0, pady=10)

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=int((self._width-self._width/8)/2 - 75))
        self.textbox.grid(row=0, column=2, padx=(20, 0), pady=(40, 0), rowspan=7, sticky="nsew")
        self.start_game_button_1 = customtkinter.CTkButton(self.textbox, text="Start game", width=int((self._width - self._width / 8) / 2) - 75, height=55, command=self.side_menu_button_event)
        self.start_game_button_1.grid(row=7, column=0, padx=0, pady=10)

        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.textbox.insert("0.0", "Popis\n\n" + "--------------------\n\n\n\n\n\n\n" +
                            "tu sa bude nachadzat obrazok/gif hry\n\n\n\n\n\n\n" +
                            "--------------------\n\n" + "Tu bude slovny popis k hre|Tu bude slovny popis k hre|"
                                                         "Tu bude slovny popis k hre|Tu bude slovny popis k hre|"
                                                         "Tu bude slovny popis k hre|Tu bude slovny popis k hre|"
                                                         "Tu bude slovny popis k hre|Tu bude slovny popis k hre|"
                                                         "Tu bude slovny popis k hre|Tu bude slovny popis k hre|"
                                                         "Tu bude slovny popis k hre|Tu bude slovny popis k hre|"
                                                         "Tu bude slovny popis k hre|Tu bude slovny popis k hre|"
                                                         "Tu bude slovny popis k hre|Tu bude slovny popis k hre|"
                                                         "Tu bude slovny popis k hre|Tu bude slovny popis k hre|"
                                                         "Tu bude slovny popis k hre|Tu bude slovny popis k hre|"
                                                         "Tu bude slovny popis k hre|Tu bude slovny popis k hre|"
                                                         "Tu bude slovny popis k hre|Tu bude slovny popis k hre|"
                                                         "Tu bude slovny popis k hre|Tu bude slovny popis k hre|"
                                                         "Tu bude slovny popis k hre|Tu bude slovny popis k hre|"
                                                         "Tu bude slovny popis k hre|Tu bude slovny popis k hre|"
                                                         "Tu bude slovny popis k hre|Tu bude slovny popis k hre|"
                                                         "Tu bude slovny popis k hre|Tu bude slovny popis k hre|"
                                                         "Tu bude slovny popis k hre|Tu bude slovny popis k hre|"
                                                         "Tu bude slovny popis k hre|Tu bude slovny popis k hre|"
                                                         "Tu bude slovny popis k hre|Tu bude slovny popis k hre|")


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)


    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)


    def side_menu_button_event(self):
        print("side_menu_button click")


    def play_pong(self):
        os.system('python pong_experimental.py')


if __name__ == "__main__":
    app = App()
    app.mainloop()
    