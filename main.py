import tkinter as tk
import os
import json
from tkinter import messagebox, simpledialog, ttk

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Névjegyzék")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        self.tree = ttk.Treeview(self.root, columns=('nev', 'telefon', 'email'), show='headings')
        self.tree.heading('nev', text='Név')
        self.tree.heading('telefon', text='Telefonszám')
        self.tree.heading('email', text='Email cím')

        self.tree.column('nev', width=150)
        self.tree.column('telefon', width=150)
        self.tree.column('email', width=200)

        self.tree.pack(expand=True, fill="both", padx=10, pady=10)
        self.tree.bind("<<TreeviewSelect>>", self.show_contact_details)

        self.contacts = {}
        self.file_path = "nevjegyzek.json"
        self.load_contacts()

        self.detail_label = tk.Label(self.root, text="Válassz ki egy személyt a listából hogy lásd a részleteket", font=("Arial", 12))
        self.detail_label.pack(fill="x", padx=10, pady=5)

        self.add_btn = tk.Button(self.root, text="Új személy hozzaadása", command=self.add_contact)
        self.add_btn.pack(side="left", padx=10, pady=10)

        self.edit_btn = tk.Button(self.root, text="Meglévő személy szerkesztése", command=self.edit_contact)
        self.edit_btn.pack(side="left", padx=10, pady=10)

        self.delete_btn = tk.Button(self.root, text="Meglévő személy törlése", command=self.delete_contact)
        self.delete_btn.pack(side="right", padx=10, pady=10)

        self.refresh_list()

    def load_contacts(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                self.contacts = json.load(file)
        else:
            self.contacts = {}

    def save_contacts(self):
        with open(self.file_path, "w") as file:
            json.dump(self.contacts, file, indent=4)

    def refresh_list(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

