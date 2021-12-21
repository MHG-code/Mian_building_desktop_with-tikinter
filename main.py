import tkinter as tk
import New_order
import Return

LARGE_FONT = ("Verdana", 12)


class Frames(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.pack_propagate(False)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (New_order.New_order, Return.Return):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
            # self.frames[F].grid(row=0, column=0, sticky="nsew")


        self.show_frame(New_order.New_order)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == '__main__':
    app = Frames()
    app.mainloop()