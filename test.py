import os

def delete_temp_files(directories):
    temp_extension = ['.tmp', '.temp', '.log', '.cache']
    deleted_files = 0

    for directory in directories:
        if os.path.exists(directory):
            for filename in os.listdir(directory):
                if any(filename.endswith(ext) for ext in temp_extension):
                    file_path = os.path.join(directory, filename)
                    os.remove(file_path)
                    deleted_files += 1
                    print(f"Удалён файл: {file_path}")
                else:
                    print(f"Директория не найдена: {directory}")
directories_input = input("Введите пути к папкам (через запятую): ")
directories = [d.strip() for d in directories_input.split(',')]
delete_temp_files(directories)