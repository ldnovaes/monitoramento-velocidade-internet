import getpass
import os
USER_NAME = getpass.getuser()


def add_to_startup_windows(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = f'C:\\Users\\{USER_NAME}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'

    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(f'python {file_path}')

def get_path_documents():
    dir_possiveis = ["Documentos", "Documents"]

    # Procurar pelo primeiro diretório existente
    config_dir = None

    for dir_nome in dir_possiveis:
        dir_path = os.path.join(os.path.expanduser("~"), dir_nome)

        if os.path.exists(dir_path):
            config_path = os.path.join(dir_path, "Monitoramento - Velocinet")

            if not os.path.exists(config_path):
                os.makedirs(config_path)
            return config_path

    if config_dir is None:
        raise Exception("Nenhum diretório de configuração encontrado.")

def byte_to_mb(nbytes):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while nbytes >= 1024 and i < len(suffixes)-1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])