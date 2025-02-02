import tkinter as tk
from os import getcwd, path


class Window(tk.Tk):

    _assets_path = path.join(getcwd(), "Assets")
    _pad = 5

    _dark_color_palette = {"background": "#454545", "foreground": "#f0f0f0"}
    _normal_color_palette = {"background": "#f0f0f0", "foreground": "black"}
    _color_palette = _normal_color_palette

    def __init__(self):
        tk.Tk.__init__(self)

        # window title
        title = "SaberA10N ToolSet"
        self.title(title)

        # window icon
        icon_path = path.join(self._assets_path, "icon.ico")
        self.iconbitmap(icon_path)

        # window color
        self.config(background=self._color_palette["background"])

        self.mainloop()

    def get_color(self, color=None):
        if color is not None:
            return self._color_palette[color]
        return self._color_palette  # returns color palette dict


if __name__ == "__main__":
    window = Window()
