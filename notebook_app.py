"""Notebook demo — cleanroom's ttk.Notebook showcase.

Three real tabs: a welcome, a working counter, and a target reached with
nb.select(2) to prove programmatic switching. On the cleanroom live runner
this renders as a real tab bar on the virtual screen; on a real PC it opens
a normal tkinter window with the same tabs.
"""

import tkinter as tk
from tkinter import ttk


def main():
    root = tk.Tk()
    root.title("Notebook demo")
    root.geometry("430x240")

    nb = ttk.Notebook(root)
    nb.pack(fill="both", expand=True, padx=8, pady=8)

    # tab 1 — welcome
    tab1 = ttk.Frame(nb)
    ttk.Label(tab1, text="ttk.Notebook, on the virtual screen",
              font=("Helvetica", 13, "bold")).pack(pady=10)
    ttk.Label(tab1, text="real tabs, real switching — no socket, no server").pack(pady=4)
    nb.add(tab1, text="welcome")

    # tab 2 — a working counter and a jump button
    tab2 = ttk.Frame(nb)
    count = tk.IntVar(value=0)
    value_label = ttk.Label(tab2, text="clicked 0 times")

    def bump():
        count.set(count.get() + 1)
        value_label.config(text="clicked %d times" % count.get())

    def jump():
        nb.select(2)

    ttk.Button(tab2, text="count up", command=bump).pack(pady=10)
    value_label.pack(pady=2)
    ttk.Button(tab2, text="go to tab 3 (nb.select(2))", command=jump).pack(pady=6)
    nb.add(tab2, text="counter")

    # tab 3 — the jump target
    tab3 = ttk.Frame(nb)
    ttk.Label(tab3, text="you jumped here programmatically — tab switching works").pack(pady=10)
    nb.add(tab3, text="jump target")

    root.mainloop()


if __name__ == "__main__":
    main()
