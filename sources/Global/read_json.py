import json
from PIL import ImageGrab


# преобразует json в словарь python
def json_to_dict(file_path: str, encoding="cp1251"):
    with open(file_path, "r", encoding=encoding) as read_file:
        data = json.load(read_file)
    return data


# делает скриншот
def do_screen(file):
    image = ImageGrab.grab()
    image.save(file)


if __name__ == '__main__':
    do_screen('ror_screen.png')
