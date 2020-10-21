from Image.function import convertation


prev_ext = input("Введите входное расширение: ")
new_ext = input("Введите выходное расширение: ")
directory = input("Введите путь до файлов: ")

code = convertation(prev_ext, new_ext)

if code == 1:
    print("Конвертация выполнена")
else:
    print("Файлы с таким расширением не найдены")
