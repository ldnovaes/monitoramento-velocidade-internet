import json
import os
import platform
import tkinter

import customtkinter
from PIL import Image

from functions.functions import add_to_startup_windows, get_path_documents


class TelaInicial(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("1200x800")
        self.title("Velocinet v1.0")
        self.resizable(width=False, height=False)

        self.main_container = customtkinter.CTkFrame(self)
        self.main_container.pack(fill=tkinter.BOTH, expand=True)

        # painel esquerdo
        self.left_side_panel = customtkinter.CTkFrame(self.main_container, width=600, fg_color="white")
        self.left_side_panel.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False)

        # painel direito
        self.right_side_panel = customtkinter.CTkFrame(self.main_container, width=600)
        self.right_side_panel.pack(side=tkinter.RIGHT,
                                   fill=tkinter.BOTH,
                                   expand=True)

        self.image_right_side_panel = customtkinter.CTkImage(light_image=Image.open(os.path.join(os.getcwd(), "assets", "imagem_right_side_panel.png")), size=(600, 800))
        self.label_right_side_panel = customtkinter.CTkLabel(self.right_side_panel, image=self.image_right_side_panel,
                                                             text="")
        self.label_right_side_panel.pack(expand=True, fill=tkinter.BOTH)

        # label de 'url'
        self.label_time = customtkinter.CTkLabel(self.left_side_panel, text="Velocinet", font=customtkinter.CTkFont(
            family=(os.path.join(os.getcwd(), "fonts", "Poppins-ExtraBold.ttf")), weight="bold", size=35), width=600)
        self.label_time.place(y=100)  # Posiciona o widget na primeira linha

        # label de insira a url
        self.text_title_screen = customtkinter.CTkLabel(self.left_side_panel,
                                                        text="Configure o monitoramento antes de iniciá-lo",
                                                        font=customtkinter.CTkFont(
                                                            family=(os.path.join(os.getcwd(), "fonts",
                                                                                 "Poppins-Light.ttf")),
                                                            size=15),
                                                        width=600,
                                                        text_color="#555555")

        self.text_title_screen.place(y=150)

        self.opcoes = ["30 minutos", "60 minutos", "90 minutos", "120 minutos"]
        self.time_monitoramento = customtkinter.StringVar()
        self.time_monitoramento.set(self.opcoes[0])
        self.type_url_entry = customtkinter.CTkOptionMenu(self, values=self.opcoes, variable=self.time_monitoramento,
                                                          font=customtkinter.CTkFont(size=24), width=450, height=75, fg_color="gray92", button_color="gray78", text_color="gray45", bg_color="white")

        self.type_url_entry.place(x=145, y=200)
        self.type_url_entry.configure(width=300)

        self.visibilidade_var = customtkinter.StringVar()
        self.visibilidade = customtkinter.CTkCheckBox(self,
                                                      text="Iniciar automaticamente",
                                                      fg_color="blue",
                                                      bg_color="white",
                                                      hover_color="blue",
                                                      variable=self.visibilidade_var,
                                                      font=customtkinter.CTkFont(
                                                          family=(os.path.join(os.getcwd(), "fonts",
                                                                               "Poppins-ExtraBold.ttf")),
                                                          size=15)
                                                      )
        self.visibilidade.place(x=185, y=325)

        self.bota_salvar = customtkinter.CTkButton(self, bg_color="white",
                                                   text="Salvar",
                                                   height=50,
                                                   fg_color="#191970",
                                                   text_color="gray92",
                                                   corner_radius=15,
                                                   command=self.update_config_user,
                                                   hover_color="forest green",
                                                   width=125,
                                                   font=customtkinter.CTkFont(
                                                           family=(os.path.join(os.getcwd(), "fonts",
                                                                                "Poppins-Regular.ttf")),
                                                           size=16,
                                                           weight="normal")
                                                   )

        self.bota_salvar.place(x=237.5, y=400)

        self.line = customtkinter.CTkFrame(self.left_side_panel, fg_color='gray93', height=2, width=450)
        self.line.place(x=75, y=585)

        self.label_iniciar = customtkinter.CTkLabel(self.left_side_panel, text="Velocinet", font=customtkinter.CTkFont(
            family=(os.path.join(os.getcwd(), "fonts", "Poppins-ExtraBold.ttf")), weight="bold", size=15), width=200)
        self.label_iniciar.place(x=200, y=570)

        self.descricao = customtkinter.CTkLabel(self.left_side_panel,
                                                        text="Clique em Início para começar a monitorar seu provedor!",
                                                        font=customtkinter.CTkFont(
                                                            family=(os.path.join(os.getcwd(), "fonts",
                                                                                 "Poppins-Light.ttf")),
                                                            size=15),
                                                        width=600,
                                                        text_color="#555555")

        self.descricao.place(y=620)

        self.botao_inicio = customtkinter.CTkButton(self, bg_color="white",
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

    def start(self):

        if "windows" in platform.system().lower():
            add_to_startup_windows(os.path.join(os.getcwd(), "monitoramento", "monitoramento.py"))

        elif "linux" in platform.system().lower():
            pass

    def update_config_user(self):

        if self.get_visibilidade_entry() == True:
            self.change_config_user("inicio_automatico", True)
        else:
            self.change_config_user("inicio_automatico", False)

        self.change_config_user("tempo_monitoramento", self.get_time_monitoramento_entry())

    def get_visibilidade_entry(self):

        visibilidade = self.visibilidade_var.get()

        if visibilidade == str(1):
            return True

        return False

    def get_time_monitoramento_entry(self):
        return self.time_monitoramento.get()

    def get_config_user(self):

        config_path = os.path.join(get_path_documents(), "config.json")

        # Se o arquivo não existir, cria-o com um dicionário vazio
        if not os.path.exists(config_path):
            with open(config_path, "w") as config_file:
                json.dump({}, config_file)

        with open(config_path, "r") as config_file:
            try:
                return json.load(config_file)
            except json.decoder.JSONDecodeError:
                return {}

    def set_config_user(self, **kwargs):
        dicionario = self.get_config_user()

        for key, value in kwargs.items():
            dicionario[key] = value

        self.save_config_user(dicionario)

    def change_config_user(self, key, value):
        dicionario = self.get_config_user()
        dicionario[key] = value
        self.save_config_user(dicionario)

    def save_config_user(self, dicionario):

        config_path = os.path.join(get_path_documents(), "config.json")

        with open(config_path, "w") as config:
            json.dump(dicionario, config)



