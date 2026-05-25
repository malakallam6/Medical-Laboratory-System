import tkinter as tk
from tkinter import messagebox
from db import get_connection
from styles import (BG, NAVY, BLUE, ACCENT, WHITE,
                    page_header, make_form, make_buttons, make_tree, page_footer)

def open_results():
    win = tk.Toplevel()
    win.title("Test Results")
    win.geometry("820x580")
    win.configure(bg=BG)

    page_header(win, "📋", "Test Results", "Record and review patient test outcomes")

    fields = ["Result", "Laboratorian ID", "Patient ID",
              "Date (YYYY-MM-DD)", "Test ID"]
    entries = make_form(win, fields)

    tree = make_tree(win,
        ("Result ID","Result","Lab ID","Patient ID","Date","Test ID"),
        (80, 120, 70, 80, 110, 70))

    def load():
        for r in tree.get_children(): tree.delete(r)
        conn = get_connection(); cur = conn.cursor()
        cur.execute("SELECT Test_Result_ID, Result, Laboratorian_ID, Patient_ID, TS_Date, Test_ID FROM TEST_RESULT")
        for i, row in enumerate(cur.fetchall()):
            tree.insert("", tk.END, values=row, tags=("alt" if i%2 else "",))
        tree.tag_configure("alt", background="#dce6f7")
        conn.close()

    def add():
        vals = [entries[f].get() for f in ["Result", "Laboratorian ID", "Patient ID",
                                             "Date (YYYY-MM-DD)", "Test ID"]]
        if not all(vals):
            messagebox.showwarning("Missing", "All fields are required."); return
        conn = get_connection(); cur = conn.cursor()
        cur.execute(
            "INSERT INTO TEST_RESULT(Result,Laboratorian_ID,Patient_ID,TS_Date,Test_ID) VALUES(%s,%s,%s,%s,%s)",
            vals)
        conn.commit(); conn.close()
        messagebox.showinfo("Success", "Result added!"); load()

    def delete():
        sel = tree.selection()
        if not sel: messagebox.showwarning("Select", "Please select a row."); return
        rid = tree.item(sel[0])["values"][0]
        conn = get_connection(); cur = conn.cursor()
        cur.execute("DELETE FROM TEST_RESULT WHERE Test_Result_ID=%s", (rid,))
        conn.commit(); conn.close(); load()

    make_buttons(win, [
        ("➕  Add Result",      add,    BLUE),
        ("🗑  Delete Selected", delete, "#8b2020"),
        ("🔄  Refresh",        load,   "#4a5568"),
    ])
    page_footer(win)
    load()