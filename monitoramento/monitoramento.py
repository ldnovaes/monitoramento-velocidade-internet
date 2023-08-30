import json
import os
import time

import pandas as pd
import speedtest

from functions.functions import get_path_documents


def criar_teste():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    s.results.share()

    resultados = s.results.dict()

    df_planilha = pd.read_excel('dados.xlsx', engine='openpyxl')

    df_resultados = {
        "velocidade_download": [resultados["download"]],
        "velocidade_upload": [resultados["upload"]],
        "ping": [resultados["ping"]],
        "url_teste": [resultados["server"]["url"]],
        "hora_teste": [resultados["timestamp"]],
        "print_teste": [resultados["share"]]
    }

    df_resultados = pd.DataFrame.from_dict(df_resultados)

    df_concatenado = pd.concat([df_planilha, df_resultados])

    df_concatenado.to_excel(os.path.join(get_path_documents(), 'dados.xlsx'), sheet_name='base', index=False)

def executar_indefinidamente():

    config = configuracoes()

    if config["inicio_automatico"]:
        print("Iniciando")
        while True:
            criar_teste()
            time.sleep(int(config["tempo_monitoramento"].split(" ")[0].strip()))

    else:
        print("Não é iniciado")

def configuracoes():

    with open(os.path.join(get_path_documents(), "config.json"), "r") as config:
        return json.load(config)

if __name__ == "__main__":
    executar_indefinidamente()