import os
from normalize_script import normalize
from pathlib import Path
from shutil import rmtree


def creation_folders(path):

    """Створення пустих папок для переміщень"""

    for key in template_extensions.keys():
        folders_path = path + "\\" + key
        Path(folders_path).mkdir(exist_ok=True)

def delete_empty_folders(path):
    
    """Видалення порожніх папок та папок в папках"""

    for f in os.listdir(path):
        new_path = path+'\\'+f

        if os.path.isfile(new_path):
            continue
        elif f in "images, video, documents, music, archives, unknown": # пошук власноруч створених папок             
            if os.path.isdir(new_path):
                try:
                    Path(new_path).rmdir()
                except OSError:
                    continue
        else:
            rmtree(new_path)


def recursive_finding(path, level=1):

    """Рекурсивний прохід по папкам в пошуці файлів"""

    for i in os.listdir(path):
    
        if i not in "images, video, documents, music, archives, unknown": # пропуск власноруч створених папок
            
            new_path = path+'\\'+i
        
            if os.path.isdir(new_path):
                recursive_finding(new_path,level+1)

            elif os.path.isfile(new_path):
                file_extension_full = Path(new_path).suffix.upper()
                file_extension = file_extension_full[1:]
                sorting_files(file_extension, new_path, start_path)
            else:
                print('ELSE')
        else:
            continue
        

def sorting_files(extension, path, start_path):

    """Створення путі для переміщення. 
    Виклик функції нормалізування (перейменовує файл й переміщує файл).
    Додавання нового путі в список в словнику."""
    
    
    if extension in template_extensions["images"]:
        moved_path = start_path + '\\' + "images" # створюємо путь для переміщення в нову папку     
        new_moved_path = normalize(path, moved_path) # з путя бере імя і перейменовує. Переміщує файл
        finded_extensions["images"].append(new_moved_path) # додаємо файл в нову папку
        if extension not in finded_extensions["known"]:
            finded_extensions["known"].append(extension)
    elif extension in template_extensions["video"]:
        moved_path = start_path + '\\' + "video" # створюємо путь для переміщення в нову папку
        new_moved_path = normalize(path, moved_path) # з путя бере імя і перейменовує. Переміщує файл
        finded_extensions["video"].append(new_moved_path) # додаємо файл в нову папку
        if extension not in finded_extensions["known"]:
            finded_extensions["known"].append(extension)
    elif extension in template_extensions["documents"]:
        moved_path = start_path + '\\' + "documents" # створюємо путь для переміщення в нову папку
        new_moved_path = normalize(path, moved_path) # з путя бере імя і перейменовує. Переміщує файл
        finded_extensions["documents"].append(new_moved_path) # додаємо файл в нову папку
        if extension not in finded_extensions["known"]:
            finded_extensions["known"].append(extension)
    elif extension in template_extensions["music"]:
        moved_path = start_path + '\\' + "music" # створюємо путь для переміщення в нову папку
        new_moved_path = normalize(path, moved_path) # з путя бере імя і перейменовує. Переміщує файл
        finded_extensions["music"].append(new_moved_path) # додаємо файл в нову папку
        if extension not in finded_extensions["known"]:
            finded_extensions["known"].append(extension)
    elif extension in template_extensions["archives"]:
        moved_path = start_path + '\\' + "archives" # створюємо путь для переміщення в нову папку
        new_moved_path = normalize(path, moved_path) # з путя бере імя і перейменовує. Переміщує файл
        finded_extensions["archives"].append(new_moved_path) # додаємо файл в нову папку
        if extension not in finded_extensions["known"]:
            finded_extensions["known"].append(extension)
    else:
        moved_path = start_path + '\\' + "unknown" # створюємо путь для переміщення в нову папку
        new_moved_path = normalize(path, moved_path) # з путя бере імя і перейменовує. Переміщує файл
        if extension not in finded_extensions["unknown"]:
            finded_extensions["unknown"].append(extension)

    return finded_extensions # словник усіх файлів


# Оголошення базових розширень
template_extensions = {
    "images": ['JPEG', 'PNG', 'JPG', 'SVG'],
    "video": ['AVI', 'MP4', 'MOV', 'MKV'],
    "documents": ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'],
    "music": ['MP3', 'OGG', 'WAV', 'AMR'],
    "archives": ['ZIP', 'GZ', 'TAR'],
    "unknown": []
}
finded_extensions = {
    "images": [],
    "video": [],
    "documents": [],
    "music": [],
    "archives": [],
    "known": [],
    "unknown": []
}


# шлях до папки
start_path = 'C:\\Users\\user\\shit_sorting'


"""Старт програми!!"""
creation_folders(start_path) # створюємо папки

recursive_finding(path=start_path, level=1) # процес сортування

# РОЗПАКОВКА АРХІВІВ ДОПИСАТИ

delete_empty_folders(path=start_path) # видалення пустих папок


"""Лишилося дописати:
1. Розпаковка архівів
2. Шлях до стартової папки брати від користувача з блоком try except якщо к-вач нічого не ввів"""