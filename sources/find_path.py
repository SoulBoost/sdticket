import os

def passage(file_name, folder):
    for element in os.scandir(folder):
        if element.is_file():
            if element.name == file_name:
                yield folder
        else:
            yield from passage(file_name, element.path)


path_to_env = " ".join(passage('.env', os.getcwd())).split(" ")[0] + r'\.env'
