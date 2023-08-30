import json
import os
import time
from _decimal import Decimal
from datetime import datetime

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

    path_excel = os.path.join(get_path_documents(), 'dados.xlsx')

    try:
        df_planilha = pd.read_excel(path_excel, engine='openpyxl')

    except FileNotFoundError:
        df = pd.DataFrame()
        df.to_excel(path_excel, index=False)
        df_planilha = pd.read_excel(path_excel, engine='openpyxl')

    df_resultados = {
        "velocidade_download": [resultados['download']],
        "velocidade_upload": [resultados['upload']],
        "ping": [resultados["ping"]],
        "url_teste": [resultados["server"]["url"]],
        "hora_teste": [str(datetime.strptime(resultados["timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%d/%m/%Y %H:%M:%S.%f")[:-3])],
        "print_teste": [resultados["share"]]
    }

    df_resultados = pd.DataFrame.from_dict(df_resultados)

    df_concatenado = pd.concat([df_planilha, df_resultados])

    df_concatenado.to_excel(path_excel, sheet_name='base', index=False)

def executar_indefinidamente():

    config = configuracoes()

    if config["inicio_automatico"] == True:
        print("Iniciando")
        while True:
            criar_teste()
            time.sleep(int(config["tempo_monitoramento"].split(" ")[0].strip()) * 60)

    else:
        print("Não é iniciado")

def configuracoes():

    try:
        with open(os.path.join(get_path_documents(), 'config.json'), "r") as config:
            return json.load(config)

    except FileNotFoundError:
        with open(os.path.join(get_path_documents(), 'config.json'), "w") as config:

            default = {"inicio_automatico": True, "tempo_monitoramento": "30 minutos"}

            json.dump(default, config)

            return default

if __name__ == "__main__":
    executar_indefinidamente()