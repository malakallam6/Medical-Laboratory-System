import tkinter as tk
from tkinter import messagebox
from db import get_connection
from styles import (BG, NAVY, BLUE, ACCENT, WHITE,
                    page_header, make_form, make_buttons, make_tree, page_footer)

def open_patients():
    win = tk.Toplevel()
    win.title("Patients")
    win.geometry("820x600")
    win.configure(bg=BG)

    page_header(win, "👤", "Patients", "Add, view and remove patient records")

    fields = ["Patient ID", "Name", "Job", "Birth Date (YYYY-MM-DD)",
              "Apartment", "City", "Street", "Phone"]
    entries = make_form(win, fields)

    tree = make_tree(win,
        ("ID","Name","Job","Birth Date","City","Phone"),
        (70, 160, 110, 110, 110, 120))

    def load():
        for r in tree.get_children(): tree.delete(r)
        conn = get_connection(); cur = conn.cursor()
        cur.execute("""
            SELECT p.Patient_ID, p.Patient_Name, p.Job,
                   p.Birth_Date, p.City, pp.Patient_Phone
            FROM Patient p
            LEFT JOIN Patient_Phone pp ON p.Patient_ID = pp.Patient_ID
        """)
        for i, row in enumerate(cur.fetchall()):
            tree.insert("", tk.END, values=row, tags=("alt" if i%2 else "",))
        tree.tag_configure("alt", background="#dce6f7")
        conn.close()

    def add():
        pid  = entries["Patient ID"].get()
        name = entries["Name"].get()
        if not pid or not name:
            messagebox.showwarning("Missing", "Patient ID and Name are required."); return
        conn = get_connection(); cur = conn.cursor()
        cur.execute(
            "INSERT INTO Patient(Patient_ID,Patient_Name,Job,Birth_Date,Apartment,City,Street) VALUES(%s,%s,%s,%s,%s,%s,%s)",
            (pid, name, entries["Job"].get(), entries["Birth Date (YYYY-MM-DD)"].get(),
             entries["Apartment"].get(), entries["City"].get(), entries["Street"].get()))
        ph = entries["Phone"].get()
        if ph:
            cur.execute("INSERT INTO Patient_Phone(Patient_ID,Patient_Phone) VALUES(%s,%s)", (pid, ph))
        conn.commit(); conn.close()
        messagebox.showinfo("Success", "Patient added!"); load()

    def delete():
        sel = tree.selection()
        if not sel: messagebox.showwarning("Select", "Please select a patient."); return
        pid = tree.item(sel[0])["values"][0]
        conn = get_connection(); cur = conn.cursor()
        cur.execute("DELETE FROM Patient_Phone WHERE Patient_ID=%s", (pid,))
        cur.execute("DELETE FROM Patient WHERE Patient_ID=%s", (pid,))
        conn.commit(); conn.close()
        messagebox.showinfo("Deleted", "Patient deleted."); load()

    make_buttons(win, [
        ("➕  Add Patient",     add,    BLUE),
        ("🗑  Delete Selected", delete, "#8b2020"),
        ("🔄  Refresh",        load,   "#4a5568"),
    ])
    page_footer(win)
    load()