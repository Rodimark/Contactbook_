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

        # TreeView 3 oszloppal
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

        for name in sorted(self.contacts.keys()):
            details = self.contacts[name]
            self.tree.insert('', tk.END, values=(name, details['phone'], details['email']))

    def show_contact_details(self, event):
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected[0])
            name = item['values'][0]
            details = self.contacts[name]
            self.detail_label.config(text=f"Név: {name}\nTelefonszám: {details['phone']}\nEmail cím: {details['email']}")
            self.edit_btn.config(state="normal")
            self.delete_btn.config(state="normal")
        else:
            self.detail_label.config(text="Válassz ki egy személyt a listából hogy lásd a részleteket")
            self.edit_btn.config(state="disabled")
            self.delete_btn.config(state="disabled")

    def add_contact(self):
        name = simpledialog.askstring("Személy hozzáadása", "Adj meg egy nevet: ")
        if not name:
            return
        if name in self.contacts:
            messagebox.showerror("Hiba", "Mar létezik ilyen név a névjegyzékben.")
            return
        phone = simpledialog.askstring("Hozzáadás", "Adj meg egy telefonszámot: ")
        email = simpledialog.askstring("Hozzáadás", "Adj meg egy email cimet: ")
        self.contacts[name] = {"phone": phone, "email": email}
        self.save_contacts()
        self.refresh_list()

    def edit_contact(self):
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected[0])
            name = item['values'][0]
            new_phone = simpledialog.askstring("Szerkesztés", "Adj meg egy új telefonszámot: ", initialvalue=self.contacts[name]["phone"])
            new_email = simpledialog.askstring("Szerkesztés", "Adj meg egy új email címet: ", initialvalue=self.contacts[name]["email"])
            self.contacts[name] = {"phone": new_phone, "email": new_email}
            self.save_contacts()
            self.refresh_list()

    def delete_contact(self):
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected[0])
            name = item['values'][0]
            if messagebox.askyesno("Személy törlése", f"Biztosan törölni akarod '{name}'?"):
                del self.contacts[name]
                self.save_contacts()
                self.refresh_list()
                self.detail_label.config(text="Válassz ki egy személyt a listából hogy lásd a részleteket")
                self.edit_btn.config(state="disabled")
                self.delete_btn.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()