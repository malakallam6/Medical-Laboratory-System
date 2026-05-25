BG      = "#f4f6fb"
NAVY    = "#1b2a4a"
BLUE    = "#3d5a99"
LBLUE   = "#6b85c2"
ACCENT  = "#5b8dee"
WHITE   = "#ffffff"
SUBTEXT = "#6b7c99"
ENTRY_BG = "#eaf0fb"
ROW_ALT  = "#dce6f7"

def apply_treeview_style():
    from tkinter import ttk
    s = ttk.Style()
    s.theme_use("clam")
    s.configure("Treeview",
        background=WHITE, foreground=NAVY,
        fieldbackground=WHITE, rowheight=30,
        font=("Georgia", 10)
    )
    s.configure("Treeview.Heading",
        background=NAVY, foreground=WHITE,
        font=("Georgia", 10, "bold"), relief="flat"
    )
    s.map("Treeview", background=[("selected", ACCENT)])

def page_header(win, icon, title, subtitle):
    import tkinter as tk
    hdr = tk.Frame(win, bg=NAVY, height=60)
    hdr.pack(fill="x")
    hdr.pack_propagate(False)
    tk.Label(hdr, text=f"{icon}  {title}",
             font=("Georgia", 14, "bold"), bg=NAVY, fg=WHITE
             ).place(relx=0.02, rely=0.5, anchor="w")
    tk.Frame(win, bg=ACCENT, height=4).pack(fill="x")
    tk.Label(win, text=subtitle, font=("Georgia", 9, "italic"),
             bg=BG, fg=SUBTEXT).pack(anchor="w", padx=20, pady=(8, 2))

def make_form(win, fields):
    import tkinter as tk
    form = tk.Frame(win, bg=WHITE, padx=20, pady=14,
                    highlightbackground=ACCENT, highlightthickness=1)
    form.pack(padx=20, pady=6, fill="x")
    entries = {}
    for i, f in enumerate(fields):
        tk.Label(form, text=f, bg=WHITE, fg=SUBTEXT,
                 font=("Georgia", 9), anchor="w").grid(
                     row=i//2, column=(i%2)*2, padx=(0,6), pady=5, sticky="w")
        e = tk.Entry(form, bg=ENTRY_BG, fg=NAVY, insertbackground=NAVY,
                     font=("Georgia", 10), relief="flat", bd=0,
                     highlightthickness=2, highlightbackground=LBLUE,
                     highlightcolor=ACCENT)
        e.grid(row=i//2, column=(i%2)*2+1, padx=(0,18), pady=5, sticky="ew")
        entries[f] = e
    form.columnconfigure(1, weight=1)
    form.columnconfigure(3, weight=1)
    return entries

def make_buttons(win, actions):
    import tkinter as tk
    bf = tk.Frame(win, bg=BG)
    bf.pack(pady=6)
    for text, cmd, color in actions:
        tk.Button(bf, text=text, command=cmd,
                  bg=color, fg=WHITE, font=("Georgia", 10, "bold"),
                  relief="flat", bd=0, cursor="hand2",
                  activebackground=LBLUE, activeforeground=WHITE,
                  padx=14, pady=7).pack(side="left", padx=6)
    return bf

def make_tree(win, cols, widths=None):
    import tkinter as tk
    from tkinter import ttk
    apply_treeview_style()
    tf = tk.Frame(win, bg=BG)
    tf.pack(padx=20, pady=4, fill="both", expand=True)
    tree = ttk.Treeview(tf, columns=cols, show="headings")
    for j, col in enumerate(cols):
        tree.heading(col, text=col)
        tree.column(col, width=(widths[j] if widths else 130))
    sb = ttk.Scrollbar(tf, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=sb.set)
    tree.pack(side="left", fill="both", expand=True)
    sb.pack(side="right", fill="y")
    return tree

def page_footer(win):
    import tkinter as tk
    f = tk.Frame(win, bg=NAVY, height=30)
    f.pack(fill="x", side="bottom")
    f.pack_propagate(False)
    tk.Label(f, text="Medical Laboratory System",
             font=("Georgia", 8), bg=NAVY, fg="#8fa3cc"
             ).place(relx=0.5, rely=0.5, anchor="center")