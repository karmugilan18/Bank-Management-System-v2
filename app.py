import tkinter as tk
from tkinter import messagebox


# ── Colour & Font constants (easy to change later) ──────────
BG_COLOR     = "#1e1e2e"   # dark background
CARD_COLOR   = "#2a2a3e"   # slightly lighter card
ACCENT_COLOR = "#7c6af7"   # purple accent
TEXT_COLOR   = "#ffffff"   # white text
MUTED_COLOR  = "#9090a0"   # grey muted text
ERROR_COLOR  = "#f38ba8"   # red for errors

FONT_TITLE   = ("Segoe UI", 22, "bold")
FONT_LABEL   = ("Segoe UI", 11)
FONT_INPUT   = ("Segoe UI", 11)
FONT_BUTTON  = ("Segoe UI", 11, "bold")
FONT_SMALL   = ("Segoe UI", 9)


# ── Helper: create a styled Entry (input box) ───────────────
def make_entry(parent, show=None):
    entry = tk.Entry(
        parent,
        font=FONT_INPUT,
        bg="#3a3a50",
        fg=TEXT_COLOR,
        insertbackground=TEXT_COLOR,   # cursor colour
        relief="flat",
        bd=0,
        show=show                      # used for password: show="*"
    )
    return entry


# ── Helper: create a styled Button ──────────────────────────
def make_button(parent, text, command, color=ACCENT_COLOR):
    btn = tk.Button(
        parent,
        text=text,
        command=command,
        font=FONT_BUTTON,
        bg=color,
        fg=TEXT_COLOR,
        activebackground=color,
        activeforeground=TEXT_COLOR,
        relief="flat",
        bd=0,
        cursor="hand2",               # pointer cursor on hover
        padx=10,
        pady=8
    )
    return btn


# ════════════════════════════════════════════════════════════
#  LOGIN SCREEN
# ════════════════════════════════════════════════════════════
class LoginScreen(tk.Frame):

    def __init__(self, parent, on_login_success):
        super().__init__(parent, bg=BG_COLOR)
        self.on_login_success = on_login_success  # function to call on success
        self.build_ui()

    def build_ui(self):
        # ── Centre card ─────────────────────────────────────
        card = tk.Frame(self, bg=CARD_COLOR, padx=40, pady=40)
        card.place(relx=0.5, rely=0.5, anchor="center")

        # Title
        tk.Label(card, text="🏦 Bank Management",
                 font=FONT_TITLE, bg=CARD_COLOR,
                 fg=TEXT_COLOR).grid(row=0, column=0, columnspan=2, pady=(0, 6))

        tk.Label(card, text="Sign in to your account",
                 font=FONT_SMALL, bg=CARD_COLOR,
                 fg=MUTED_COLOR).grid(row=1, column=0, columnspan=2, pady=(0, 24))

        # Username
        tk.Label(card, text="Username", font=FONT_LABEL,
                 bg=CARD_COLOR, fg=TEXT_COLOR).grid(
                 row=2, column=0, sticky="w", pady=(0, 4))

        self.username_entry = make_entry(card)
        self.username_entry.grid(row=3, column=0, columnspan=2,
                                 sticky="ew", ipady=8, pady=(0, 16))

        # Password
        tk.Label(card, text="Password", font=FONT_LABEL,
                 bg=CARD_COLOR, fg=TEXT_COLOR).grid(
                 row=4, column=0, sticky="w", pady=(0, 4))

        self.password_entry = make_entry(card, show="*")
        self.password_entry.grid(row=5, column=0, columnspan=2,
                                 sticky="ew", ipady=8, pady=(0, 24))

        # Login button
        btn = make_button(card, "Login", self.handle_login)
        btn.grid(row=6, column=0, columnspan=2, sticky="ew", pady=(0, 12))

        # Error label (hidden until needed)
        self.error_label = tk.Label(card, text="", font=FONT_SMALL,
                                    bg=CARD_COLOR, fg=ERROR_COLOR)
        self.error_label.grid(row=7, column=0, columnspan=2)

        # Hint
        tk.Label(card, text="Default: admin / admin123",
                 font=FONT_SMALL, bg=CARD_COLOR,
                 fg=MUTED_COLOR).grid(row=8, column=0, columnspan=2, pady=(16, 0))

        # Allow pressing Enter to login
        self.password_entry.bind("<Return>", lambda e: self.handle_login())

    def handle_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        # Simple hardcoded credentials for now (Lesson 12 will use DB)
        if username == "admin" and password == "admin123":
            self.error_label.config(text="")
            self.on_login_success()
        else:
            self.error_label.config(text="❌ Invalid username or password.")
            self.password_entry.delete(0, tk.END)


# ════════════════════════════════════════════════════════════
#  DASHBOARD SCREEN (placeholder for now)
# ════════════════════════════════════════════════════════════
class DashboardScreen(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent, bg=BG_COLOR)
        self.build_ui()

    def build_ui(self):
        tk.Label(self, text="🏦 Welcome to Bank Management System",
                 font=FONT_TITLE, bg=BG_COLOR,
                 fg=TEXT_COLOR).pack(pady=40)

        tk.Label(self, text="Dashboard coming in Lesson 8!",
                 font=FONT_LABEL, bg=BG_COLOR,
                 fg=MUTED_COLOR).pack()


# ════════════════════════════════════════════════════════════
#  MAIN APP — manages all screens
# ════════════════════════════════════════════════════════════
class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Bank Management System v2")
        self.geometry("900x600")
        self.configure(bg=BG_COLOR)
        self.resizable(False, False)

        # Centre the window on screen
        self.update_idletasks()
        x = (self.winfo_screenwidth()  // 2) - 450
        y = (self.winfo_screenheight() // 2) - 300
        self.geometry(f"900x600+{x}+{y}")

        self.show_login()

    def show_login(self):
        self.clear_screen()
        LoginScreen(self, on_login_success=self.show_dashboard).pack(
            fill="both", expand=True)

    def show_dashboard(self):
        self.clear_screen()
        DashboardScreen(self).pack(fill="both", expand=True)

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()


# ── Entry point ─────────────────────────────────────────────
if __name__ == "__main__":
    app = App()
    app.mainloop()