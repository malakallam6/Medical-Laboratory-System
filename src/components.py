import tkinter as tk
from tkinter import messagebox
from db import get_connection
from styles import (BG, NAVY, BLUE, ACCENT, WHITE,
                    page_header, make_form, make_buttons, make_tree, page_footer)

def open_components():
    win = tk.Toplevel()
    win.title("Components")
    win.geometry("680x540")
    win.configure(bg=BG)

    page_header(win, "🧴", "Components", "Track inventory components and stock levels")

    fields = ["Component ID", "Name", "Available Quantity", "Minimum Quantity"]
    entries = make_form(win, fields)

    tree = make_tree(win,
        ("ID","Name","Available","Minimum"),
        (80, 200, 140, 140))

    def load():
        for r in tree.get_children(): tree.delete(r)
        conn = get_connection(); cur = conn.cursor()
        cur.execute("SELECT Component_ID,Name_Of_Component,Available_quantity,Minimum_quantity FROM COMPONENT")
        for i, row in enumerate(cur.fetchall()):
            tag = "alt" if i%2 else ""
            low = row[2] < row[3]
            tree.insert("", tk.END, values=row, tags=("low" if low else tag,))
        tree.tag_configure("alt", background="#dce6f7")
        tree.tag_configure("low", background="#f7dcdc", foreground="#8b2020")
        conn.close()

    def add():
        cid = entries["Component ID"].get(); name = entries["Name"].get()
        if not cid or not name:
            messagebox.showwarning("Missing","ID and Name required."); return
        conn = get_connection(); cur = conn.cursor()
        cur.execute("INSERT INTO COMPONENT(Component_ID,Name_Of_Component,Available_quantity,Minimum_quantity) VALUES(%s,%s,%s,%s)",
                    (cid, name, entries["Available Quantity"].get(), entries["Minimum Quantity"].get()))
        conn.commit(); conn.close()
        messagebox.showinfo("Success","Component added!"); load()

    def delete():
        sel = tree.selection()
        if not sel: messagebox.showwarning("Select","Please select a row."); return
        cid = tree.item(sel[0])["values"][0]
        conn = get_connection(); cur = conn.cursor()
        cur.execute("DELETE FROM COMPONENT WHERE Component_ID=%s",(cid,))
        conn.commit(); conn.close(); load()

    make_buttons(win, [
        ("➕  Add",            add,    BLUE),
        ("🗑  Delete Selected", delete, "#8b2020"),
        ("🔄  Refresh",        load,   "#4a5568"),
    ])
    page_footer(win)
    load()