from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

FONT = ImageFont.truetype("SecularOne.ttf", 320)


class ThumbnailMaker:
    def __init__(self, base_image_path):
        self.base_image_path = base_image_path
        self.base_image = None

    def __enter__(self):
        print("entered")
        self.base_image = Image.open(self.base_image_path)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')
        self.base_image.close()
        self.base_image = None
        self.center_pos = None

    def create_thumbnail(self, name: str) -> None:
        new_image = self.base_image.copy()
        draw = ImageDraw.Draw(new_image)
        _, _, text_width, text_height = draw.textbbox((0, 0), text=name, font=FONT)
        center_pos = (
            (new_image.width - text_width) // 2,
            (new_image.height - text_height) // 2
        )
        draw.text(
            center_pos,
            name,
            (255, 255, 255),
            align="center",
            font=FONT,
            stroke_fill=(0, 0, 0),
            stroke_width=10
        )

        new_image.show()


if __name__ == "__main__":
    with ThumbnailMaker(r"../footage/base_thumbnail/base.jpg") as thumbnail_maker:
        thumbnail_maker.create_thumbnail(name="Name"[::-1])
