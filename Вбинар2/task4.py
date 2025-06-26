def test_file_path(file_path):
    """Путь до файла
    :param file_path: абсолютный путь до файла
    :return: название файла без расширения, названия диска и корневую папку
    """
    # todo Здесь нужно написать код
    file_path1 = file_path.split('\\')
    f_n = file_path1[-1][::-1]
    t = f_n.find(".")
    f_n = f_n[t + 1::]
    file_name = f_n[::-1]
    disk_name = file_path.split(':')[0]
    root_folder = file_path1[1]
    return file_name, disk_name, root_folder
