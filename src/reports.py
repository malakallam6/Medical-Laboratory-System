import tkinter as tk
from db import get_connection
from styles import (BG, NAVY, BLUE, LBLUE, ACCENT, WHITE,
                    page_header, make_tree, page_footer)

def open_reports():
    win = tk.Toplevel()
    win.title("Reports & Queries")
    win.geometry("860x520")
    win.configure(bg=BG)

    page_header(win, "📊", "Reports & Queries", "Analytical queries & database design notes")

    btn_frame = tk.Frame(win, bg=BG)
    btn_frame.pack(padx=20, pady=(10,4), fill="x")

    tree = make_tree(win, ("Result",), (700,))

    def run(fn):
        cols, rows = fn()
        tree.delete(*tree.get_children())
        tree["columns"] = cols
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=max(120, 700 // len(cols)))
        for i, row in enumerate(rows):
            tree.insert("", tk.END, values=row, tags=("alt" if i % 2 else "",))
        tree.tag_configure("alt", background="#dce6f7")

    queries = [
        ("📋  Tests by Patient 12527\n(Past Year)",   q1_data, BLUE),
        ("⚠️  Components\nBelow Minimum",              q2_data, "#8b2020"),
    ]

    for i, (label, fn, color) in enumerate(queries):
        tk.Button(btn_frame, text=label, command=lambda f=fn: run(f),
                  bg=color, fg=WHITE, font=("Georgia", 10, "bold"),
                  relief="flat", bd=0, cursor="hand2",
                  activebackground=LBLUE, activeforeground=WHITE,
                  width=22, height=3, wraplength=160
                  ).grid(row=0, column=i, padx=6, pady=4, sticky="ew")
        btn_frame.columnconfigure(i, weight=1)

    page_footer(win)


def q1_data():
    conn = get_connection(); cur = conn.cursor()
    cur.execute("""
        SELECT mt.Name_Of_Medical_Test, tr.TS_Date, l.Name AS Laboratorian_Name
        FROM TEST_RESULT tr
        JOIN MEDICAL_TEST mt ON tr.Test_ID = mt.Test_ID
        JOIN Laboratorian l  ON tr.Laboratorian_ID = l.Laboratorian_ID
        WHERE tr.Patient_ID = 12527
        AND tr.TS_Date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
    """)
    rows = cur.fetchall(); conn.close()
    return ("Test Name", "Date", "Laboratorian"), rows

def q2_data():
    conn = get_connection(); cur = conn.cursor()
    cur.execute("""
        SELECT Component_ID, Name_Of_Component, Available_quantity, Minimum_quantity
        FROM COMPONENT
        WHERE Available_quantity < Minimum_quantity
    """)
    rows = cur.fetchall(); conn.close()
    return ("Component ID", "Component Name", "Available Qty", "Minimum Qty"), rows