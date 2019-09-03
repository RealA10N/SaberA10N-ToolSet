import tkinter as tk
from os import getcwd, path


class Window(tk.Tk):

    _assets_path = path.join(getcwd(), "Assets")
    _color_palette = {"bg": "#454545", "text": "#f0f0f0"}

    def __init__(self):
        tk.Tk.__init__(self)

        # window title
        title = "SaberA10N ToolSet"
        self.title(title)

        # window icon
        icon_path = path.join(self._assets_path, "icon.ico")
        self.iconbitmap(icon_path)

        # window color
        self.config(background=self._color_palette["bg"])

        self.mainloop()

    def get_color(self, color=None):
        if color is not None:
            return self._color_palette[color]
        return self._color_palette  # returns color palette dict


if __name__ == "__main__":
    window = Window()
