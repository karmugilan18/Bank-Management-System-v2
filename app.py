import tktinter as tk
from tkinter import messagebox

# constants 
BG_COLOR      = "#858585"
CARD_COLOR    = "#2a2a3e"
SIDEBAR_COLOR = "#16162a"
ACCENT_COLOR  = "#7c6af7"
HOVER_COLOR   = "#6355d4"
TEXT_COLOR    = "#ffffff"
MUTED_COLOR   = "#9090a0"
ERROR_COLOR   = "#f38ba8"
SUCCESS_COLOR = "#a6e3a1"

#font based 
FONT_TITLE    = ("Segoe UI", 20, "bold")
FONT_SUBTITLE = ("Segoe UI", 13, "bold")
FONT_LABEL    = ("Segoe UI", 11)
FONT_INPUT    = ("Segoe UI", 11)
FONT_BUTTON   = ("Segoe UI", 10, "bold")
FONT_SMALL    = ("Segoe UI", 9)
FONT_SIDEBAR  = ("Segoe UI", 10, "bold")

#reusable widget helpers 

def make_entry (parent , show = None  ,width = 28 ):
    return tk.Entry (parent , font = FONT_INPUT , bg = "#3a3a50" , fg = TEXT_COLOR , insertbackground = TEXT_COLOR , relief = "flat", bd = 0 , show = show , width = width  )

def make_button(parent , text , command , color = ACCENT_COLOR , width =20):
    return tk.Button ( parent  , text = text , command = command , font = FONT_BUTTON , bg = color , fg = TEXT_COLOR , activebackground =HOVER_COLOR , activeforeground = TEXT_COLOR ,relief = "flat",bd =0 , cursor ="hand2", padx = 10 , pady =8 , width = width)

def make_label (parent , text , font = FONT_LABEL , fg = TEXT_COLOR , bg = CARD_COLOR  ):
    return tk.Label(parent , text = text , font = font , fg =fg , bg = bg)

def make_card(parent , padx = 30 , pady = 30 ):
    return tk.Frame (parent , bg = CARD_COLOR , padx = padx ,pady =pady)

#Screen base class - all inherits this make it easy 
 
class BaseScreen (tk.Frame):
    """Every screen inherits from this Provides common bg and reference to app"""

    def __init__(self, parent , app):
        super().__init__(parent , bg =BG_COLOR)
        self.app =app # reference to main App so screens can switch each other

    def show_success(self, label , message):
        label.config(text = f"{message}", fg =SUCCESS_COLOR)

    def show_error(self, label , message):
        label.config(text = f"{message}", fg =ERROR_COLOR)

    def clear_message(self, label):
        label.config(text = "")



# Login 
class LoginScreen(BaseScreen):
    def __init__(self, parent , app):
        super().__init__(parent , app)
        self.build_ui()

    def build_ui(self):
        card = make_card(self, padx=50 , pady= 50)
        card.place(relx= 0.5 , rely = 0.5 , anchor = "center")

        make_label (card,"Bank Managament " , font = FONT_TITLE ).grid(row = 0, column  = 0 , columnspan = 2 , pady = (0,6))
        make_label (card, "sign in to continue" , font = FONT_SMALL, fg =MUTED_COLOR).grid (row = 1, column =0, columnspan = 2 , pady =(0, 28))
        make_label(card, "Username").grid(row=2, column=0, sticky="w", pady=(0, 4))
        self.username_var = tk.StringVar()
        self.username_entry = make_entry(card)
        self.username_entry.grid (row = 3, column = 0 , columnspan = 2 , sticky = "ew" , ipady = 8 , pady =(0, 16))

        make_label(card, "Password").grid(row=4, column=0, sticky="w", pady=(0, 4))
        self.password_entry = make_entry(card, show="*")
        self.password_entry.grid(row=5, column=0, columnspan=2,
                                  sticky="ew", ipady=8, pady=(0, 24))

        make_button (card , "Login" , self.handle_login).grid(row = 6 , column = 0  , columnspan =2 , sticky = "ew")
        

        self.msg = make_label(card, "", font=FONT_SMALL, fg=ERROR_COLOR)
        self.msg.grid(row=7, column=0, columnspan=2, pady=(10, 0))

        make_label(card, "Hint: admin / admin123", font=FONT_SMALL,
                   fg=MUTED_COLOR).grid(row=8, column=0, columnspan=2, pady=(16, 0))
        self.password_entry.bind("<Return>", lambda e: self.handle_login())
        self.username_entry.focus()


    def handle_login(self):
        u = self.username_entry.get().strip()
        p = self.password_entry.get().strip()
        if u == "admin" and p == "admin123":
            self.app.show_main()
        else:
            self.show_error(self.msg, "Invalid username or password.")
            self.password_entry.delete(0, tk.END)