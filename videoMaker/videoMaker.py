from moviepy.editor import *
from random import choice
from os import listdir

FONT_SIZE = 75


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

    def make_video(self, video_path, name):
        name_clip = VideoFileClip(video_path)
        end_clip = add_name_to_video("./EquationSlayerBirthdayEnding.mp4", name)
        final_video = concatenate_videoclips([name_clip, choice(self.clips), end_clip])
        final_video.write_videofile(f"./{name}.mp4")


if __name__ == "__main__":
    video_maker = VideoMaker("../footage/base_videos")
    video_maker.make_video("./name_clip_test.mp4", "sarah")
