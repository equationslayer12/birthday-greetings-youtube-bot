from videoMaker import videoMaker
from thumbnailMaker import thumbnailMaker


def main():
    vid_maker = videoMaker.VideoMaker()
    thumb_maker = thumbnailMaker.ThumbnailMaker()

    for video_name in ["daniel.mp4", "equations.mp4"]:
        vid_maker.create_video(video_name)
        thumb_maker.create_thumbnail(video_name)

if __name__ == "__main__":
    main()
