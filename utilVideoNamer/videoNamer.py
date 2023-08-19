from os import listdir, rename


class VideoNamer:
    def __init__(self, name_videos_dir: str, names_text_file_path: str):
        self.name_videos_dir = name_videos_dir
        self.names_text_file_path = names_text_file_path

    def name_videos(self):
        with open(self.names_text_file_path, "r", encoding="utf-8") as f:
            for current_file_name, new_file_name in zip(listdir(self.name_videos_dir), f.readlines()):
                rename(f"{self.name_videos_dir}/{current_file_name}", f"{self.name_videos_dir}/{new_file_name[:-1]}.mp4")


if __name__ == "__main__":
    video_namer = VideoNamer("../footage/name_videos", "../footage/new_names.txt")
    video_namer.name_videos()
