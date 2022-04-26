import tkinter as tk
from Environment import *
from Agent import *

class Mines(tk.Frame):

    def __init__(self, oir_env, ag):
        tk.Frame.__init__(self)
        self.master.title("Minesweeper")
        # self.master.resizable(False, False)
        self.pack(expand=tk.NO, fill=tk.BOTH)
        self.label_matrix = []
        self.env = oir_env
        self.agent = ag
        self.init_step()


    def click_reset(self):
        self.env.new_game()
        self.agent.reset_agent(self.env)
        for i in range(self.env.dim):
            for j in range(self.env.dim):
                self.label_matrix[i][j].configure(text="?",bg="grey")

    def click_next(self):
        self.env.update_clear_mark()
        score = self.agent.inference_onestep()
        for i in range(self.env.dim):
            for j in range(self.env.dim):
                if self.env.hidden_board[i][j] == 1:
                    cell_value = self.env.board[i][j]
                    if cell_value == -1:
                        bg_str = "red"
                    else:
                        bg_str = "white"
                    self.label_matrix[i][j].configure(text=str(cell_value),bg=bg_str)
                elif self.env.hidden_board[i][j] == -1:
                    self.label_matrix[i][j].configure(text="M",bg="red")
                elif self.env.hidden_board[i][j] == 2:
                    self.label_matrix[i][j].configure(text="C",bg="green")
        if score != -1:
            print(score)
        else:
            print("you finished the game")

    def init_step(self):
        frame1 = tk.Frame(bg='black')
        for i in range(self.env.dim):
            label_list = []
            for j in range(self.env.dim):
                label_list.append(tk.Label(frame1, text="?", bg="grey", width=2, height=1, font=('Arial', 15)))
                label_list[j].grid(row=i, column=j, padx=1, pady=1)
            self.label_matrix.append(label_list)
        frame1.pack()
        frame2 = tk.Frame()
        self.next_button = tk.Button(frame2, text = 'next', width = 6, height = 1, command = self.click_next)
        self.reset_button = tk.Button(frame2, text = 'reset', width = 6, height = 1, command = self.click_reset)
        self.next_button.pack()
        self.reset_button.pack()
        frame2.pack()




if __name__=='__main__':
    oir_env = Environment(10, 10, 0)
    ag = Agent(oir_env, 1)
    m = Mines(oir_env, ag)
    m.mainloop()
