import tkinter as tk
from patients import open_patients
from laboratorians import open_laboratorians
from components import open_components
from tests import open_tests
from results import open_results
from reports import open_reports

BG      = "#f4f6fb"
NAVY    = "#1b2a4a"
BLUE    = "#3d5a99"
LBLUE   = "#6b85c2"
ACCENT  = "#5b8dee"
WHITE   = "#ffffff"
SUBTEXT = "#6b7c99"

window = tk.Tk()
window.title("Medical Laboratory System")
window.state("zoomed")
window.configure(bg=BG)
header = tk.Frame(window, bg=NAVY, height=70)
header.pack(fill="x")
header.pack_propagate(False)
tk.Label(header, text="🧪  Medical Laboratory System",
         font=("Georgia", 16, "bold"), bg=NAVY, fg=WHITE
         ).place(relx=0.5, rely=0.5, anchor="center")
tk.Frame(window, bg=ACCENT, height=4).pack(fill="x")

tk.Label(window, text="Select a module to get started",
         font=("Georgia", 10, "italic"), bg=BG, fg=SUBTEXT).pack(pady=(16, 6))

tiles_data = [
    ("👤", "Patients",          "View & manage patients",    open_patients),
    ("🔬", "Laboratorians",     "Staff directory",           open_laboratorians),
    ("🧴", "Components",        "Inventory & stock",         open_components),
    ("🧫", "Medical Tests",     "Test catalogue",            open_tests),
    ("📋", "Test Results",      "Results & records",         open_results),
    ("📊", "Reports",           "Queries & analytics",       open_reports),
]

grid_frame = tk.Frame(window, bg=BG)
grid_frame.pack(padx=28, pady=8, fill="both", expand=True)

for i, (icon, label, sub, cmd) in enumerate(tiles_data):
    row, col = divmod(i, 3)

    tile = tk.Frame(grid_frame, bg=BLUE, cursor="hand2", width=190, height=140)
    tile.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
    tile.pack_propagate(False)

    top_bar = tk.Frame(tile, bg=ACCENT, height=5)
    top_bar.pack(fill="x")

    icon_frame = tk.Frame(tile, bg=WHITE, width=48, height=48)
    icon_frame.pack(pady=(12, 0))
    icon_frame.pack_propagate(False)
    tk.Label(icon_frame, text=icon, font=("Segoe UI Emoji", 20),
             bg=WHITE, fg=NAVY).place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(tile, text=label, font=("Georgia", 11, "bold"),
             bg=BLUE, fg=WHITE).pack(pady=(6, 0))
    tk.Label(tile, text=sub, font=("Georgia", 8, "italic"),
             bg=BLUE, fg="#b0c4f0").pack()

    def make_click(c, f=tile, tb=top_bar, ic=icon_frame):
        def on_enter(e):
            f.configure(bg=LBLUE)
            tb.configure(bg=WHITE)
            for w in f.winfo_children():
                if w not in (tb, ic):
                    try: w.configure(bg=LBLUE)
                    except: pass
        def on_leave(e):
            f.configure(bg=BLUE)
            tb.configure(bg=ACCENT)
            for w in f.winfo_children():
                if w not in (tb, ic):
                    try: w.configure(bg=BLUE)
                    except: pass
        for widget in [f] + list(f.winfo_children()):
            widget.bind("<Button-1>", lambda e, c=c: c())
            widget.bind("<Enter>", on_enter)
            widget.bind("<Leave>", on_leave)
        for child in ic.winfo_children():
            child.bind("<Button-1>", lambda e, c=c: c())
            child.bind("<Enter>", on_enter)
            child.bind("<Leave>", on_leave)
    make_click(cmd)

    grid_frame.columnconfigure(col, weight=1)
    grid_frame.rowconfigure(row, weight=1)

footer = tk.Frame(window, bg=NAVY, height=36)
footer.pack(fill="x", side="bottom")
footer.pack_propagate(False)
tk.Label(footer, text="© 2024 Medical Laboratory System  |  All rights reserved",
         font=("Georgia", 8), bg=NAVY, fg="#8fa3cc"
         ).place(relx=0.5, rely=0.5, anchor="center")

window.mainloop()