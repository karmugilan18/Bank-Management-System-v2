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

    
