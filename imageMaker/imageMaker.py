from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class ImageMaker:
    def __init__(self, base_image_path: str, output_dir: str, font_path: str, font_size=320, offset_y=0):
        self.base_image_path = base_image_path
        self.base_image = None
        self.output_dir = output_dir
        self.font = ImageFont.truetype(font_path, font_size)
        self.offset_y = offset_y

    def __enter__(self):
        self.base_image = Image.open(self.base_image_path)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.base_image.close()
        self.base_image = None
        self.center_pos = None

    def make_image(self, name: str, file_name=None) -> None:
        if not file_name:
            file_name = name
        new_image: Image = self.base_image.copy()
        draw = ImageDraw.Draw(new_image)
        _, _, text_width, text_height = draw.textbbox((0, 0), text=name, font=self.font)
        center_pos = (
            (new_image.width - text_width) // 2,
            (new_image.height - text_height) // 2 + self.offset_y
        )
        draw.text(
            center_pos,
            name[::-1],
            (255, 255, 255),
            align="center",
            font=self.font,
            stroke_fill=(0, 0, 0),
            stroke_width=10
        )

        new_image.save(self.output_dir + file_name + ".png")


if __name__ == "__main__":
    names = ["דניאל"]
    with ImageMaker(r"../footage/base_images/base_thumbnail.jpg",
                    "../birthdays_slayed/youtube_videos/thumbnails/",
                    font_path="../SecularOne.ttf", offset_y=-100) as image_maker:
        for name in names:
            image_maker.make_image(name=name)
