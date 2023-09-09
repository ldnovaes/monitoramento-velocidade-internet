import os
import platform

import customtkinter
import psutil

from functions.functions import add_to_startup_windows
from monitoramento.monitoramento import executar_indefinidamente


class Rodape(customtkinter.CTk):

    def __init__(self, root, **kwargs):
        super().__init__(**kwargs)
        self.root = root

        self.line = customtkinter.CTkFrame(self.root.get_left_panel(), fg_color='gray93', height=2, width=450)
        self.line.place(x=75, y=585)

        self.label_iniciar = customtkinter.CTkLabel(self.root.get_left_panel(), text="Velocinet", font=customtkinter.CTkFont(
            family=(os.path.join(os.getcwd(), "fonts", "Poppins-ExtraBold.ttf")), weight="bold", size=15), width=200)
        self.label_iniciar.place(x=200, y=570)

        self.descricao = customtkinter.CTkLabel(self.root.get_left_panel(),
                                                text="Clique em Início para começar a monitorar seu provedor!",
                                                font=customtkinter.CTkFont(
                                                    family=(os.path.join(os.getcwd(), "fonts",
                                                                         "Poppins-Light.ttf")),
                                                    size=15),
                                                width=600,
                                                text_color="#555555")

        self.descricao.place(y=620)

        self.botao_inicio = customtkinter.CTkButton(self.root.get_left_panel(), bg_color="white",
                                                    text="Iniciar",
                                                    height=50,
                                                    fg_color="green",
                                                    text_color="gray92",
                                                    corner_radius=15,
                                                    command=self.start,
                                                    hover_color="forest green",
                                                    width=125,
                                                    font=customtkinter.CTkFont(
                                                        family=(os.path.join(os.getcwd(), "fonts",
                                                                             "Poppins-Regular.ttf")),
                                                        size=16,
                                                        weight="normal")
                                                    )

        self.botao_inicio.place(x=237.5, y=680)

        self.verifica_processo()
        self.update_verifica_processo()


    def start(self):

        if "windows" in platform.system().lower():
            self.root.update_config_user()

            if self.root.get_config_user()["inicio_automatico"] == True:
                add_to_startup_windows(os.path.join(os.getcwd(), "dist", "monitoramento", "monitoramento.exe"))
                executar_indefinidamente()
            else:
                executar_indefinidamente()

        elif "linux" in platform.system().lower():
            executar_indefinidamente()


    def frame_inicializacao_posterior(self): # quando houver um processo, significa que o usuário já iniciou a execução do monitoramento, então troca o botão
        self.descricao.configure(text="Você pode cancelar o monitoramento clicando no botão abaixo")
        self.botao_inicio.configure(text="Cancelar", hover_color="red4", fg_color="red", command=self.kill_process_monitoramento)
    
    def frame_inicializacao_default(self):
        self.descricao.configure(text="Clique em Início para começar a monitorar seu provedor!")
        self.botao_inicio.configure(text="Iniciar", fg_color="green",
                                                    command=self.start,
                                                    hover_color="forest green")
    
    def verifica_processo(self):

        for process in psutil.process_iter(attrs=['name']):

            if 'monitoramento' in process.info['name'].lower():
                self.frame_inicializacao_posterior()
                return True
        else:
            self.frame_inicializacao_default()
            return False

    def update_verifica_processo(self):
        self.verifica_processo()
        self.after(1000, self.update_verifica_processo)

    def kill_process_monitoramento(self):

        for process in psutil.process_iter(attrs=['name']):

            if 'monitoramento' in process.info['name'].lower():
                process.terminate()
                return True
        else:
            return False
