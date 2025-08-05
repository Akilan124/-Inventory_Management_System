import tkinter as tk
from tkinter import messagebox, ttk
from inventory import add_product, update_product, delete_product, get_all_products, get_low_stock_products

def launch_dashboard():
    root = tk.Tk()
    root.title("Inventory Pro Dashboard")
    root.geometry("1024x640")
    root.configure(bg="#1a1a2e")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
                    background="#2e2e4d",
                    foreground="#ffffff",
                    rowheight=28,
                    fieldbackground="#2e2e4d",
                    font=("Lato", 10))
    style.map("Treeview", background=[('selected', '#3c8dad')])

    header = tk.Label(root, text="Inventory Management Dashboard", font=("Poppins", 22, "bold"),
                      bg="#1a1a2e", fg="#ffffff")
    header.pack(pady=20)

    frame = tk.Frame(root, bg="#1a1a2e")
    frame.pack(pady=10)

    tree = ttk.Treeview(frame, columns=("ID", "Name", "Desc", "Price", "Qty"), show='headings', height=10)
    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=150)
    tree.pack(side=tk.LEFT)

    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def refresh():
        tree.delete(*tree.get_children())
        for row in get_all_products():
            tree.insert('', tk.END, values=row)

    def make_label(text):
        return tk.Label(form_frame, text=text, bg="#1a1a2e", fg="#dddddd", font=("Lato", 11))

    def make_entry():
        return tk.Entry(form_frame, font=("Lato", 11), width=30, bg="#222244", fg="#ffffff", insertbackground="white",
                        relief="flat")

    form_frame = tk.Frame(root, bg="#1a1a2e")
    form_frame.pack(pady=20)

    make_label("Product Name").grid(row=0, column=0, sticky="w", padx=10, pady=4)
    name_entry = make_entry()
    name_entry.grid(row=0, column=1, padx=10, pady=4)

    make_label("Description").grid(row=1, column=0, sticky="w", padx=10, pady=4)
    desc_entry = make_entry()
    desc_entry.grid(row=1, column=1, padx=10, pady=4)

    make_label("Price").grid(row=2, column=0, sticky="w", padx=10, pady=4)
    price_entry = make_entry()
    price_entry.grid(row=2, column=1, padx=10, pady=4)

    make_label("Quantity").grid(row=3, column=0, sticky="w", padx=10, pady=4)
    qty_entry = make_entry()
    qty_entry.grid(row=3, column=1, padx=10, pady=4)

    def clear_fields():
        name_entry.delete(0, tk.END)
        desc_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
        qty_entry.delete(0, tk.END)

    def add():
        try:
            name = name_entry.get()
            desc = desc_entry.get()
            price = float(price_entry.get())
            qty = int(qty_entry.get())
            ok, msg = add_product(name, desc, price, qty)
            messagebox.showinfo("Info", msg)
            clear_fields()
            refresh()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update():
        selected = tree.selection()
        if selected:
            try:
                item = tree.item(selected[0])['values']
                pid = item[0]
                name = name_entry.get()
                desc = desc_entry.get()
                price = float(price_entry.get())
                qty = int(qty_entry.get())
                ok, msg = update_product(pid, name, desc, price, qty)
                messagebox.showinfo("Info", msg)
                clear_fields()
                refresh()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def delete():
        selected = tree.selection()
        if selected:
            pid = tree.item(selected[0])['values'][0]
            delete_product(pid)
            refresh()

    def report():
        lows = get_low_stock_products()
        if lows:
            message = "Low stock items:\n" + "\n".join([f"{r[1]}: {r[4]} left" for r in lows])
        else:
            message = "All stocks are sufficient."
        messagebox.showinfo("Report", message)

    btn_frame = tk.Frame(root, bg="#1a1a2e")
    btn_frame.pack(pady=10)

    def make_button(text, command, color):
        return tk.Button(btn_frame, text=text, font=("Lato", 11, "bold"), bg=color, fg="white", width=18, height=2,
                         relief="flat", command=command)

    make_button("Add Product", add, "#00adb5").grid(row=0, column=0, padx=10, pady=5)
    make_button("Update Product", update, "#6c5ce7").grid(row=0, column=1, padx=10, pady=5)
    make_button("Delete Product", delete, "#d63031").grid(row=0, column=2, padx=10, pady=5)
    make_button("Low Stock Report", report, "#e1b12c").grid(row=0, column=3, padx=10, pady=5)

    refresh()
    root.mainloop()
