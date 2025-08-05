import tkinter as tk
from tkinter import messagebox
from auth import register_user, authenticate_user
from gui.dashboard_gui import launch_dashboard

class LoginWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login - Inventory Pro")
        self.root.geometry("480x500")
        self.root.configure(bg="#1e1e2f")
        self.root.resizable(False, False)

        self._build_ui()
        self.root.mainloop()

    def _build_ui(self):
        # Branding header
        header = tk.Label(self.root, text="Inventory Pro", font=("Poppins", 24, "bold"), fg="#ffffff",
                          bg="#1e1e2f")
        header.pack(pady=(40, 10))

        subtitle = tk.Label(self.root, text="Sign in to manage stock like a boss",
                            font=("Lato", 12), fg="#bbbbbb", bg="#1e1e2f")
        subtitle.pack(pady=(0, 20))

        # Login form container
        form = tk.Frame(self.root, bg="#29293d", bd=0)
        form.pack(pady=10, padx=30, fill="both")

        def make_label(text):
            return tk.Label(form, text=text, font=("Lato", 11), bg="#29293d", fg="#cccccc", anchor="w")

        def make_entry(show=None):
            return tk.Entry(form, font=("Lato", 12), width=28, bg="#1e1e2f", fg="#eeeeee", relief="flat",
                            insertbackground="#ffffff", show=show)

        # Username field
        make_label("Username").pack(anchor="w", pady=(10, 2))
        self.username = make_entry()
        self.username.pack(pady=(0, 10))

        # Password field
        make_label("Password").pack(anchor="w", pady=(10, 2))
        self.password = make_entry(show="*")
        self.password.pack(pady=(0, 10))

        # Login Button
        login_btn = tk.Button(self.root, text="Login", font=("Lato", 12, "bold"), bg="#00adb5", fg="#ffffff",
                              width=25, pady=10, bd=0, activebackground="#00959c", command=self.login)
        login_btn.pack(pady=(20, 10))

        # Register Button
        register_btn = tk.Button(self.root, text="Create New Account", font=("Lato", 11), bg="#eeeeee",
                                 fg="#222222", width=25, pady=8, bd=0, activebackground="#dddddd",
                                 command=self.register)
        register_btn.pack(pady=(0, 30))

    def login(self):
        user = self.username.get()
        pw = self.password.get()
        if authenticate_user(user, pw):
            self.root.destroy()
            launch_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")

    def register(self):
        user = self.username.get()
        pw = self.password.get()
        success, msg = register_user(user, pw)
        if success:
            messagebox.showinfo("Success", msg)
        else:
            messagebox.showerror("Error", msg)
