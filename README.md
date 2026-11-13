# notebook-demo

A three-tab `ttk.Notebook` app — the smallest honest demonstration that the
cleanroom live runner's virtual tkinter renders real, switchable tabs:

1. **welcome** — what you are looking at
2. **counter** — a button that counts, a label bound to an `IntVar`
3. **jump target** — reached with `nb.select(2)`, proving programmatic switching

Run it anywhere Python runs:

```
python notebook_app.py
```

In [cleanroom](https://amanvicky.github.io/cleanroom/), paste this repo's URL
and click **run notebook_app.py** — the tab bar is rendered by the page's
virtual tkinter (a subset of the tkinter API as real HTML widgets), and the
terminal stays live while the window is open. Nothing is installed and
nothing is left behind.
