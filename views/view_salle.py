import customtkinter as ctk
from services.services_salle import ServiceSalle

class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.service_salle = ServiceSalle()

        self.title("Gestion des salles")
        self.geometry("700x500")

        self.cadreInfo = ctk.CTkFrame(self, corner_radius=10)
        self.cadreInfo.pack(pady=10, padx=10, fill="x")

        self.cadreActions = ctk.CTkFrame(self, corner_radius=10)
        self.cadreActions.pack(pady=10, padx=10, fill="x")