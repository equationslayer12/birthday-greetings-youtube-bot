from videoMaker import videoMaker
from thumbnailMaker import thumbnailMaker
from os import listdir

RAW_VID_DIR = "raw_videos/"

def get_videos_in_folder(folder_path):
    video_paths = [f"{folder_path}/{video_name}" for video_name in listdir(folder_path)]

    return video_paths


def main():
    vid_maker = videoMaker.VideoMaker("/footage/base_videos")
    names = ["daniel", "equations"]

    with thumbnailMaker.ThumbnailMaker(r"/footage/base_thumbnail/base.jpg") as thumb_maker:
        for name in names:
            video_path = RAW_VID_DIR + name + ".mp4"
            vid_maker.make_video(video_path, name)
            vid_maker.make_short(video_path)
            thumb_maker.create_thumbnail(video_path)


if __name__ == "__main__":
    main()
