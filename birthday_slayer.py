from videoMaker import videoMaker
from imageMaker import imageMaker
from os import listdir

NAME_VID_DIR = "./footage/name_videos"
BASE_VIDEOS_DIR = "./footage/base_videos"
BASE_THUMBNAIL_PATH = "./footage/base_images/base_thumbnail.jpg"
NAMES_PATH = "./footage/new_names.txt"
FONT_PATH = "./SecularOne.ttf"
BIRTHDAYS_SLAYED_DIR = "./birthdays_slayed"


def get_videos_in_folder(folder_path):
    video_paths = [f"{folder_path}/{video_name}" for video_name in listdir(folder_path)]

    return video_paths


def names_generator() -> str:
    with open(NAMES_PATH, "r", encoding="utf-8") as names_file:
        for name in names_file:
            yield name[:-1]


def main():
    with imageMaker.ImageMaker(BASE_THUMBNAIL_PATH, r"./birthdays_slayed/youtube_videos/thumbnails/", FONT_PATH) as \
            image_maker:
        video_maker = videoMaker.VideoMaker("./footage", "./videoMaker", BIRTHDAYS_SLAYED_DIR)
        try:
            for name in names_generator():
                video_path = f"{NAME_VID_DIR}/{name}.mp4"
                new_video_path = video_maker.make_video(video_path, name, FONT_PATH)
                video_maker.make_short(new_video_path, name)
                image_maker.make_image(name)
        except OSError:
            print("Out of name videos or names from txt file.")


if __name__ == "__main__":
    main()
