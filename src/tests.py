import tkinter as tk
from tkinter import messagebox
from db import get_connection
from styles import (BG, NAVY, BLUE, ACCENT, WHITE,
                    page_header, make_form, make_buttons, make_tree, page_footer)

def open_tests():
    win = tk.Toplevel()
    win.title("Medical Tests")
    win.geometry("720x540")
    win.configure(bg=BG)

    page_header(win, "🧫", "Medical Tests", "Browse and manage the test catalogue")

    fields = ["Test ID", "Test Name", "Related Components", "Price", "Laboratorian ID"]
    entries = make_form(win, fields)

    tree = make_tree(win,
        ("ID","Name","Components","Price","Lab ID"),
        (60, 170, 160, 80, 80))

    def load():
        for r in tree.get_children(): tree.delete(r)
        conn = get_connection(); cur = conn.cursor()
        cur.execute("SELECT Test_ID, Name_Of_Medical_Test, Related_components, Price, Laboratorian_ID FROM MEDICAL_TEST")
        for i, row in enumerate(cur.fetchall()):
            tree.insert("", tk.END, values=row, tags=("alt" if i%2 else "",))
        tree.tag_configure("alt", background="#dce6f7")
        conn.close()

    def add():
        tid  = entries["Test ID"].get()
        name = entries["Test Name"].get()
        if not tid or not name:
            messagebox.showwarning("Missing", "Test ID and Name required."); return
        conn = get_connection(); cur = conn.cursor()
        cur.execute(
            "INSERT INTO MEDICAL_TEST(Test_ID,Name_Of_Medical_Test,Related_components,Price,Laboratorian_ID) VALUES(%s,%s,%s,%s,%s)",
            (tid, name, entries["Related Components"].get(),
             entries["Price"].get(), entries["Laboratorian ID"].get()))
        conn.commit(); conn.close()
        messagebox.showinfo("Success", "Test added!"); load()

    def delete():
        sel = tree.selection()
        if not sel: messagebox.showwarning("Select", "Please select a row."); return
        tid = tree.item(sel[0])["values"][0]
        conn = get_connection(); cur = conn.cursor()
        cur.execute("DELETE FROM MEDICAL_TEST WHERE Test_ID=%s", (tid,))
        conn.commit(); conn.close(); load()

    make_buttons(win, [
        ("➕  Add",             add,    BLUE),
        ("🗑  Delete Selected", delete, "#8b2020"),
        ("🔄  Refresh",        load,   "#4a5568"),
    ])
    page_footer(win)
    load()