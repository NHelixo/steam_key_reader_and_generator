import pytesseract
from PIL import Image
import re
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\sasas\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
image_folder = "image"

def image_string():
    data = ""
    try:
        for filename in os.listdir(image_folder):
            if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".tiff")):
                image_path = os.path.join(image_folder, filename)
                print(f"Обробка: {image_path}")
                text = pytesseract.image_to_string(Image.open(image_path), lang='eng')
                data += text + "\n"
    except FileNotFoundError:
        print(f"Папка '{image_folder}' не знайдена!")
        return data
    return data

def load_used_keys(filename):
    if filename:
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = f.read()
        except FileNotFoundError:
            return []
    else:
        data = image_string()
        if not data.strip():
            return []
        pattern = r"\b[A-Z0-9]{5}-[A-Z0-9]{5}-[A-Z0-9]{5}\b"
        keys = re.findall(pattern, data.upper())
        return keys

    pattern = r"\b[A-Z0-9]{5}-[A-Z0-9]{5}-[A-Z0-9]{5}\b"
    keys = re.findall(pattern, data.upper())
    return keys

option = input("1 - Записати ключі з тексту\n2 - Записати ключі з фото\n")

if option == "1":
    keys_option = load_used_keys("used_keys_trash")
elif option == "2":
    keys_option = load_used_keys("")
else:
    print("Такої опції не існує!")
    exit()

if not keys_option:
    exit()

keys = load_used_keys("used_keys") + keys_option
keys = list(set(keys))

keys.sort()

keys_u = load_used_keys("used_keys")

print(f"Знайдено унікальних ключів: {len(keys) - len(keys_u)}")

with open("used_keys", "w", encoding="utf-8") as f:
    for key in keys:
        f.write(key + "\n")

open("used_keys_trash", "w").close()

for filename in os.listdir(image_folder):
    file_path = os.path.join(image_folder, filename)
    if os.path.isfile(file_path):
        os.remove(file_path)

print("✅ Всі файли з папки видалені")
