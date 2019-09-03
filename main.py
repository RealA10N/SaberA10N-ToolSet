import tkinter as tk
from os import getcwd, path


class Window(tk.Tk):

    assets_path = path.join(getcwd(), "Assets")
    color_palette = {"bg": "#454545"}

    def __init__(self):
        tk.Tk.__init__(self)

        # window title
        title = "SaberA10N ToolSet"
        self.title(title)

        # window icon
        icon_path = path.join(self.assets_path, "icon.ico")
        self.iconbitmap(icon_path)

        # window color
        self.config(background=self.color_palette["bg"])

        self.mainloop()


if __name__ == "__main__":
    window = Window()
