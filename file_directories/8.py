import os

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.path.isfile(file_path):
            if os.access(file_path, os.W_OK):
                os.remove(file_path)
                print(f"Файл '{file_path}' успешно удален.")
            else:
                print(f"У вас нет прав на удаление файла '{file_path}'.")
        else:
            print(f"Путь '{file_path}' не является файлом.")
    else:
        print(f"Файл по пути '{file_path}' не существует.")

file_path = r'D:\Code2\Lab6\example'
delete_file(file_path)

