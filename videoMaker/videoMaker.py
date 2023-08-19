from moviepy.editor import *
from random import choice, shuffle
from os import listdir
from imageMaker import imageMaker

FONT_SIZE = 75
AMOUNT_OF_WISHES = 8
NAME_OF_END_IMAGE = "ending_image"
FRAME_SIZE = (1920, 1080)


def resize_clips(clips) -> list:
    max_width = max(clip.size[0] for clip in clips)
    max_height = max(clip.size[1] for clip in clips)

    resized_clips = []
    for clip in clips:
        aspect_ratio = clip.size[0] / clip.size[1]
        new_width = min(max_width, int(max_height * aspect_ratio))
        new_height = min(max_height, int(max_width / aspect_ratio))
        resized_clip = clip.resize((new_width, new_height))
        resized_clips.append(resized_clip)

    return resized_clips


def create_image(name: str, footage_dir: str, video_maker_dir: str, font_path: str) -> str:
    """ Returns path to end image """
    with imageMaker.ImageMaker(f"{footage_dir}/base_images/base_end_of_video.png", video_maker_dir,
                               font_path, 150, -50) as image_maker:
        image_maker.make_image(name, NAME_OF_END_IMAGE)

    return f"{video_maker_dir}/{NAME_OF_END_IMAGE}.png"


def create_end_clip(name: str, footage_dir: str, video_maker_dir: str, font_path: str) -> str:
    """ Returns path to end clip """
    ending_clip_audio = AudioFileClip(f"{footage_dir}/part_3_audio.mp3")
    ending_clip = ImageClip(create_image(name, footage_dir, video_maker_dir, font_path)).set_duration(ending_clip_audio.
                                                                                                      duration)
    ending_clip = ending_clip.set_audio(ending_clip_audio)
    ending_clip.write_videofile(f"{video_maker_dir}/ending_clip.mp4", fps=24)

    return f"{video_maker_dir}/ending_clip.mp4"


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
    def __init__(self, footage_dir: str, video_maker_dir: str, birthdays_slayed_dir: str):
        base_videos_dir = f"{footage_dir}/base_videos"
        base_videos_to_include_dir = f"{footage_dir}/base_videos_to_always_include"
        self.birthdays_slayed_dir = birthdays_slayed_dir
        self.footage_dir = footage_dir
        self.video_maker_dir = video_maker_dir
        self.clips = [f"{base_videos_dir}/{file_name}" for file_name in listdir(base_videos_dir)]
        self.include_clips = [f"{base_videos_to_include_dir}/{file_name}" for file_name in
                              listdir(base_videos_to_include_dir)]

    def make_video(self, video_path, name, font_path) -> str:
        """ Returns path to the video """
        name_clip = VideoFileClip(video_path)
        end_clip_path = create_end_clip(name, self.footage_dir, self.video_maker_dir, font_path)
        end_clip = VideoFileClip(end_clip_path)
        wishes = []
        for wish in birthday_wishes(self.clips, self.include_clips):
            clip = VideoFileClip(wish)
            wishes.append(clip)

        final_video = concatenate_videoclips(resize_clips([name_clip] + wishes + [end_clip]), method="compose")
        final_video.write_videofile(f"{self.birthdays_slayed_dir}/youtube_videos/{name}.mp4")

        return f"{self.birthdays_slayed_dir}/youtube_videos/{name}.mp4"

    def make_short(self, video_path, name):
        video = VideoFileClip(video_path)
        x1 = int((video.w - (video.w * (6 / 19))) // 2)
        y1 = 0
        x2 = video.w - x1
        y2 = video.h
        short = video.crop(x1=x1, y1=y1, x2=x2, y2=y2)
        short.write_videofile(f"{self.birthdays_slayed_dir}/youtube_shorts/{name}.mp4")


if __name__ == "__main__":
    video_maker = VideoMaker("../footage", "./", "../birthdays_slayed")
    video_maker.make_video("../footage/name_videos/דניאל.mp4", "דניאל", "../SecularOne.ttf")
