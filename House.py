import tkinter as tk


class Window(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.canvas = tk.Canvas(self, width=500, height=550)
        self.canvas.pack()
        self.canvas.create_rectangle(100, 150, 300, 300, fill="white", outline="black", width=2, tags="background")
        self.canvas.create_polygon(100, 150, 300, 150, 200, 50, fill="white", outline="black", width=2, tags="background")
        self.canvas.create_rectangle(150, 170, 250, 250, fill="white", outline="black", width=2, tags="background")

if __name__ == "__main__":
    root = tk.Tk()
    app = Window(root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()