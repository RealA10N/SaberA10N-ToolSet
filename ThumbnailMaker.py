from PIL import Image, ImageFont, ImageDraw
from os import path, getcwd


class Thumbnail:

    thumb_assets_folder = path.join(getcwd(), "Assets", "ThumbnailMaker")
    font = path.join(thumb_assets_folder, "Robot Crush.ttf")
    text_sizes = (125, 100, 80)
    text_y_offset = (575, 586, 600)
    text_color = "black"

    size = (1280, 720)
    min_text_padding = 70  # min amout of pixels between text and the edge of the thumbnail

    overlay_path_options = [
        path.join(thumb_assets_folder, 'ThumbnailOverlay1.png'),
        path.join(thumb_assets_folder, 'ThumbnailOverlay2.png')
    ]

    def __init__(self, text):
        self.text = text.lower()

        # generate all font sizes
        all_fonts = list()
        for cur_size in self.text_sizes:
            all_fonts.append(ImageFont.truetype(self.font, cur_size))
        self.all_fonts = all_fonts

    # will draw the self.text on the given image, with the indexed font.
    # font list is self.all_fonts
    def _draw_text(self, base_image, font_index):

        font = self.all_fonts[font_index]
        text_w, text_h = font.getsize(self.text)

        draw_img = ImageDraw.Draw(base_image)
        drawing_x = (self.size[0] - text_w) // 2
        drawing_y = self.text_y_offset[font_index]

        draw_img.text((drawing_x, drawing_y), self.text, font=font, fill=self.text_color)

    # returns only the alpha overlay layer
    def generate(self, option=0):
        img = Image.open(self.overlay_path_options[option]).resize(self.size)  # open overlay Image

        drawed = False
        for font_index, font in enumerate(self.all_fonts):
            font_w, font_h = font.getsize(self.text)
            if font_w <= self.size[0] - self.min_text_padding:
                self._draw_text(img, font_index)
                drawed = True
                break

        if not drawed:
            self._draw_text(img, len(self.text_sizes) - 1)

        return img

    # generates the alpha overlay layer, and composites it on the given image.
    def paste_on_image(self, image, option=0):
        overlay_img = self.generate(option)
        base_image = image.resize(self.size)

        return Image.alpha_composite(base_image, overlay_img)
