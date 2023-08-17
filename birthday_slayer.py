from videoMaker import videoMaker
from thumbnailMaker import thumbnailMaker
from os import listdir

NAME_VID_DIR = "./footage/name_videos"
BASE_VIDEOS_DIR = "./footage/base_videos"
NAMES_PATH = "./footage/names.txt"


def get_videos_in_folder(folder_path):
    video_paths = [f"{folder_path}/{video_name}" for video_name in listdir(folder_path)]

    return video_paths


def names_generator() -> str:
    with open(NAMES_PATH, "r", encoding="utf-8") as names_file:
        for name in names_file:
            yield name[:-1]


def main():
    # vid_maker = videoMaker.VideoMaker(BASE_VIDEOS_DIR)

    with thumbnailMaker.ImageMaker(r"footage/base_images/base_thumbnail.jpg",
                                       r"./birthdays_slayed/youtube_videos/thumbnails/") as thumb_maker:
        for name in names_generator():
            video_path = f"{NAME_VID_DIR}/{name}.mp4"
            # new_video_path = vid_maker.make_video(video_path, name)
            # vid_maker.make_short(new_video_path)
            thumb_maker.make_thumbnail(name)


if __name__ == "__main__":
    main()
