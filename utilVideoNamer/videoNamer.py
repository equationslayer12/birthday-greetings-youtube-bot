from os import listdir, rename


def sort_txt_file_alphabetically(path_to_txt_file):
    with open(path_to_txt_file, "r", encoding="utf-8") as f:
        words = f.readlines()
        words.sort()
    with open(path_to_txt_file, "w", encoding="utf-8") as f:
        f.write("".join(words))


class VideoNamer:
    def __init__(self, name_videos_dir: str, names_text_file_path: str):
        self.name_videos_dir = name_videos_dir
        self.names_text_file_path = names_text_file_path

    def name_videos(self):
        sort_txt_file_alphabetically(self.names_text_file_path)

        with open(self.names_text_file_path, "r", encoding="utf-8") as f:
            for current_file_name, new_file_name in zip(listdir(self.name_videos_dir), f.readlines()):
                existing_filename = f"{self.name_videos_dir}/{current_file_name}"
                new_filename = f"{self.name_videos_dir}/{new_file_name[:-1]}.mp4"
                rename(existing_filename, new_filename)


if __name__ == "__main__":
    video_namer = VideoNamer("../footage/name_videos", "../footage/new_names.txt")
    video_namer.name_videos()
