from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

font_path = "./thumbnailMaker/SecularOne.ttf"
if __name__ == "__main__":
    font_path = "./SecularOne.ttf"

FONT = ImageFont.truetype(font_path, 320)


class ThumbnailMaker:
    def __init__(self, base_image_path: str, output_dir: str):
        self.base_image_path = base_image_path
        self.base_image = None
        self.output_dir = output_dir

    def __enter__(self):
        self.base_image = Image.open(self.base_image_path)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.base_image.close()
        self.base_image = None
        self.center_pos = None

    def make_thumbnail(self, name: str) -> None:
        new_image: Image = self.base_image.copy()
        draw = ImageDraw.Draw(new_image)
        _, _, text_width, text_height = draw.textbbox((0, 0), text=name, font=FONT)
        center_pos = (
            (new_image.width - text_width) // 2,
            (new_image.height - text_height) // 2
        )
        draw.text(
            center_pos,
            name[::-1],
            (255, 255, 255),
            align="center",
            font=FONT,
            stroke_fill=(0, 0, 0),
            stroke_width=10
        )

        new_image.save(self.output_dir + name + ".png")


if __name__ == "__main__":
    names = ["דניאל", "רועי", "הראל", "נועה", "יעקב", "שמואל", "שרה", "פתח תקווה", "ירשולים", "ביבי", "דונדה", "פבלו",
             "רשיף", "מחמוד", "קוף", "גרגמל", "ינאי"]
    with ThumbnailMaker(r"../footage/base_thumbnail.jpg",
                        "../birthdays_slayed/youtube_videos/thumbnails/") as thumbnail_maker:
        for name in names:
            thumbnail_maker.make_thumbnail(name=name)
