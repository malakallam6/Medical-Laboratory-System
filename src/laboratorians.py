import tkinter as tk
from tkinter import messagebox
from db import get_connection
from styles import (BG, NAVY, BLUE, ACCENT, WHITE,
                    page_header, make_form, make_buttons, make_tree, page_footer)

def open_laboratorians():
    win = tk.Toplevel()
    win.title("Laboratorians")
    win.geometry("780x580")
    win.configure(bg=BG)

    page_header(win, "🔬", "Laboratorians", "Manage laboratory staff records")

    fields = ["Laboratorian ID", "Name", "Street", "City", "Apartment", "Phone"]
    entries = make_form(win, fields)

    tree = make_tree(win,
        ("ID","Name","Street","City","Apartment","Phone"),
        (60, 160, 130, 110, 100, 120))

    def load():
        for r in tree.get_children(): tree.delete(r)
        conn = get_connection(); cur = conn.cursor()
        cur.execute("""
            SELECT l.Laboratorian_ID, l.Name, l.Street, l.City, l.Apartment, lp.Lab_phone
            FROM Laboratorian l
            LEFT JOIN Lab_Phone lp ON l.Laboratorian_ID = lp.Laboratorian_ID
        """)
        for i, row in enumerate(cur.fetchall()):
            tree.insert("", tk.END, values=row, tags=("alt" if i%2 else "",))
        tree.tag_configure("alt", background="#dce6f7")
        conn.close()

    def add():
        lid  = entries["Laboratorian ID"].get()
        name = entries["Name"].get()
        if not lid or not name:
            messagebox.showwarning("Missing", "ID and Name required."); return
        conn = get_connection(); cur = conn.cursor()
        cur.execute(
            "INSERT INTO Laboratorian(Laboratorian_ID,Name,Street,City,Apartment) VALUES(%s,%s,%s,%s,%s)",
            (lid, name, entries["Street"].get(), entries["City"].get(), entries["Apartment"].get()))
        ph = entries["Phone"].get()
        if ph:
            cur.execute("INSERT INTO Lab_Phone(Laboratorian_ID,Lab_phone) VALUES(%s,%s)", (lid, ph))
        conn.commit(); conn.close()
        messagebox.showinfo("Success", "Laboratorian added!"); load()

    def delete():
        sel = tree.selection()
        if not sel: messagebox.showwarning("Select", "Please select a row."); return
        lid = tree.item(sel[0])["values"][0]
        conn = get_connection(); cur = conn.cursor()
        cur.execute("DELETE FROM Lab_Phone WHERE Laboratorian_ID=%s", (lid,))
        cur.execute("DELETE FROM Laboratorian WHERE Laboratorian_ID=%s", (lid,))
        conn.commit(); conn.close(); load()

    make_buttons(win, [
        ("➕  Add",             add,    BLUE),
        ("🗑  Delete Selected", delete, "#8b2020"),
        ("🔄  Refresh",        load,   "#4a5568"),
    ])
    page_footer(win)
    load()