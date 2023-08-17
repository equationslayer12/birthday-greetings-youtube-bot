from moviepy.editor import *
from random import choice
from os import listdir


FONT_SIZE = 75
VIDEOS_PATH = "../birthdays_slayed/youtube_videos"
SHORTS_PATH = "../birthdays_slayed/youtube_shorts"


# doesn't work, need to install "ImageMagick" or some shit like that and I don't know how
def add_name_to_video(video_path: str, name: str):
    clip = VideoFileClip(video_path)
    text = TextClip(name, fontsize=FONT_SIZE, color="black")
    text = text.set_position("center").set_duration(5)
    video = CompositeVideoClip([clip, text])

    return video


class VideoMaker:
    def __init__(self, base_videos_dir: str):
        self.clips = []

        for file_name in listdir(base_videos_dir):
            self.clips.append(VideoFileClip(f"{base_videos_dir}/{file_name}"))

    def make_video(self, video_path, name) -> str:
        """ Returns path to the video """
        name_clip = VideoFileClip(video_path)
        end_clip = add_name_to_video("./EquationSlayerBirthdayEnding.mp4", name)
        final_video = concatenate_videoclips([name_clip, choice(self.clips), end_clip])
        final_video.write_videofile(f"{VIDEOS_PATH}/{name}.mp4")

        return f"{VIDEOS_PATH}/{name}.mp4"

    def make_short(self, video_path, name):
        video = VideoFileClip(video_path)
        x1 = int((video.w - (video.w * (6 / 19))) // 2)
        y1 = 0
        x2 = video.w - x1
        y2 = video.h
        short = video.crop(x1=x1, y1=y1, x2=x2, y2=y2)
        short.write_videofile(f"{SHORTS_PATH}/{name}.mp4")


if __name__ == "__main__":
    video_maker = VideoMaker("../footage/base_videos")
    video_maker.make_short("./daniel.mp4")
