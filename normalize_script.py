from pathlib import Path
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

# створення словника
TRANS = {}
for c, l in zip (CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()    
    


def normalize(path, moved_path):
    path_to_file = Path(path)
    file_name = path_to_file.stem # отримали ім'я без розширення
    normalized_file_name = file_name.translate(TRANS)+path_to_file.suffix # нормалізували ім'я
    full_normalized_name = path_to_file.replace(Path(moved_path) / normalized_file_name) # перемістили файл в нове місце
    
    return full_normalized_name

# path = 'D:\\user\\pathlib_learn\\test.txt'
# start_path = 'D:\\user\\pathlib_learn'
