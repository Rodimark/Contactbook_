import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import os
import json

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Névjegyzék")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        self.contacts = {}
        self.file_path = "nevjegyzek.json"
        self.load_contacts()

        self.treeview = ttk.Treeview(self.root, columns=("Telefonszám", "Email"))
        self.treeview.heading("#0", text="Név")
        self.treeview.heading("Telefonszám", text="Telefonszám")
        self.treeview.heading("Email", text="Email")
        self.treeview.column("#0", width=150)
        self.treeview.column("Telefonszám", width=150)
        self.treeview.column("Email", width=250)
        self.treeview.pack(fill="both", expand=True, padx=10, pady=10)
        self.treeview.bind("<<TreeviewSelect>>", self.show_contact_details)
        self.treeview.pack(fill = "both", expand = True, padx = 10, pady = 10)

        self.detail_label = tk.Label(self.root, text="Válassz ki egy személyt a listából hogy lásd a részleteket", font=("Arial", 12), anchor = "w")
        self.detail_label.pack(fill="x", padx=10, pady=5)

        self.add_btn = tk.Button(self.root, text = "Új személy hozzáadása", command=self.add_contact)
        self.add_btn.pack(side="left", padx=10, pady=10)

        self.edit_btn = tk.Button(self.root, text="Meglévő személy szerkesztése", command=self.edit_contact)
        self.edit_btn.pack(side="left", padx=10, pady=10)

        self.delete_btn = tk.Button(self.root, text="Meglévő személy törlése", command=self.delete_contact, state = "disabled")
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
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        for name in sorted(self.contacts.keys()):
            self.treeview.insert("", "end", text=name, values=(self.contacts[name]["phone"], self.contacts[name]["email"]))

    def show_contact_details(self, event):
        selected = self.treeview.selection()
        if selected:
            item = self.treeview.item(selected[0])
            name = item["text"]
            details = self.contacts[name]
            self.detail_label.config(text = f"Név: {name}\nTelefonszám: {details['phone']}\nEmail cím: {details['email']}", font=("Arial", 12), anchor = "w")
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
            messagebox.showerror("Hiba", "Mar létezik ilyen név.")
            return
        phone = simpledialog.askstring("Új személy hozzáadása", "Telefonszám: ")
        email = simpledialog.askstring("Új személy hozzáadása", "E-mail cim: ")
        self.contacts[name] = {"phone": phone, "email": email}
        self.save_contacts()
        self.refresh_list()

    def edit_contact(self):
        selected = self.treeview.selection()
        if selected:
            item = self.treeview.item(selected[0])
            name = item["text"]
            new_phone = simpledialog.askstring("Szerkesztés", "Adj meg egy új telefonszámot: ", initialvalue=self.contacts[name]["phone"])
            new_email = simpledialog.askstring("Szerkesztés", "Adj meg egy új email címet: ", initialvalue=self.contacts[name]["email"])
            self.contacts[name] = {"phone": new_phone, "email": new_email}
            self.save_contacts()
            self.refresh_list()

    def delete_contact(self):
        selected = self.treeview.selection()
        if selected:
            item = self.treeview.item(selected[0])
            name = item["text"]
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