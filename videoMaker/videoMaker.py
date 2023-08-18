from moviepy.editor import *
from random import choice, shuffle
from os import listdir
from imageMaker import imageMaker

FONT_SIZE = 75
VIDEOS_PATH = "../birthdays_slayed/youtube_videos"
SHORTS_PATH = "../birthdays_slayed/youtube_shorts"
BASE_IMAGE_PATH = "../footage/base_images/base_end_of_video.png"
ENDING_AUDIO_PATH = "../footage/part_3_audio.mp3"
AMOUNT_OF_WISHES = 8


def create_image(name: str):
    """ Returns path to end image """
    with imageMaker.ImageMaker(BASE_IMAGE_PATH, "./", "../SecularOne.ttf", 150, -50) as image_maker:
        image_maker.make_image(name)

    return f"./{name}.png"


def create_end_clip(name: str) -> str:
    """ Returns path to end clip """
    ending_clip_audio = AudioFileClip(ENDING_AUDIO_PATH)
    ending_clip = ImageClip(create_image(name)).set_duration(ending_clip_audio.duration)
    ending_clip = ending_clip.set_audio(ending_clip_audio)
    ending_clip.write_videofile("./ending_clip.mp4", fps=24)

    return "./ending_clip.mp4"


def birthday_wishes(every_base_video: list, every_base_video_to_include: list) -> list:
    wishes = every_base_video.copy()
    include_wishes = every_base_video_to_include.copy()
    if (len(wishes) + len(include_wishes)) < AMOUNT_OF_WISHES:
        print("Not enough base videos")
        return []
    shuffle(wishes)
    wishes = wishes[:AMOUNT_OF_WISHES - len(include_wishes)]
    wishes += include_wishes
    shuffle(wishes)

    return wishes


class VideoMaker:
    def __init__(self, base_videos_dir: str, base_videos_to_include_dir: str):
        self.clips = [f"{base_videos_dir}/{file_name}" for file_name in listdir(base_videos_dir)]
        self.include_clips = [f"{base_videos_to_include_dir}/{file_name}" for file_name in listdir(base_videos_to_include_dir)]

    def make_video(self, video_path, name) -> str:
        """ Returns path to the video """
        name_clip = VideoFileClip(video_path)
        end_clip_path = create_end_clip(name)
        end_clip = VideoFileClip(end_clip_path)
        wishes = []
        for path in birthday_wishes(self.clips, self.include_clips):
            clip = VideoFileClip(path)
            print(path, clip.duration)
            wishes.append(clip)
        final_video = concatenate_videoclips([name_clip] + wishes + [end_clip], method="compose")
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
    video_maker = VideoMaker("../footage/base_videos", "../footage/base_videos_to_always_include")
    video_maker.make_short(video_maker.make_video(r"D:\Downloads\the truth.mp4", "דניאל"), "דניאל")
