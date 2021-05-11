import csv
import tkinter as tk
import random

window = tk.Tk()
window.geometry('600x500')
window.title("Creative respone")
window.config(padx=10, pady=10)

title_label = tk.Label(window, text="Information on Slaves During the 1600's-1950's")
title_label.config(font=("Lobster", 32))
title_label.pack(padx=10, pady=10)

filename = 'toc.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    authors, titles, urls = [], [], []
    summary = {"Title":[], "Author":[], "Url":[]}

    for row in reader:
        author = str(row[1])
        title = str(row[2])
        url = str(row[4])

        authors.append(author)
        titles.append(title)
        urls.append(url)

        summary["Title"].append(title)
        summary["Url"].append(url)
        summary["Author"].append(author)


label_names = tk.Label(window, text=f'{random.choice(titles)}')
label_names.config(font=('Arial', 11))
label_names.pack(pady=10, padx=10)

l = tk.Label(window, text=f'{random.choice(urls)}')
l.config(font=('Arial', 12))
l.pack(padx=10, pady=10)

o = tk.Label(window, text=f'{random.choice(authors)}')
o.config(font=('Arial', 12))
o.pack(padx=10, pady=10)


window.mainloop()
