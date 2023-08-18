def new_txt():
    with open('../footage/names.txt', 'r', encoding='utf-8') as names_file:
        names = names_file.read()
    names_tab = names.replace(' ', '\n')
    name_list = names_tab.split()
    return name_list


def check_duplicates(name_list):
    unique_names = []
    duplicates = []

    for name in name_list:
        if name in unique_names:
            duplicates.append(name)
        else:
            unique_names.append(name)

    return duplicates, unique_names


def new_names_txt(location,unique_list):
    with open(location, 'w', encoding='utf-8') as new_file:
        for name in unique_list:
            new_file.write(name + '\n')


a = check_duplicates(new_txt())[1]

new_names_txt('../footage/newNames1.txt', a)