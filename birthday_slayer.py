from videoMaker import videoMaker
from thumbnailMaker import thumbnailMaker
from os import listdir


def get_videos_in_folder(folder_path):
    video_paths = [f"{folder_path}/{video_name}" for video_name in listdir(folder_path)]

    return video_paths


def main():
    vid_maker = videoMaker.VideoMaker()
    thumb_maker = thumbnailMaker.ThumbnailMaker()

    for video_name in ["daniel.mp4", "equations.mp4"]:
        vid_maker.create_video(video_name)
        thumb_maker.create_thumbnail(video_name)


if __name__ == "__main__":
    main()
