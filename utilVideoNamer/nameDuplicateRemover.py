from videoNamer import sort_txt_file_alphabetically

NAMES_FILE_PATH = r"../footage/names.txt"
NEW_NAMES_FILE_PATH = r"../footage/new_names.txt"


def new_txt():
    with open(NAMES_FILE_PATH, 'r', encoding='utf-8') as names_file:
        names = names_file.read()
    names = names.split()

    return names


def check_duplicates(name_list):
    unique_names_list = []

    for name in name_list:
        if name not in unique_names_list:
            unique_names_list.append(name)

    return unique_names_list


def new_names_txt(location, unique_list):
    with open(location, 'w', encoding='utf-8') as new_file:
        for name in unique_list:
            new_file.write(f"{name}\n")

    sort_txt_file_alphabetically(location)


if __name__ == "__main__":
    unique_names = check_duplicates(new_txt())
    new_names_txt(NEW_NAMES_FILE_PATH, unique_names)
