from db import initialize_db
from gui.login_gui import LoginWindow

if __name__ == '__main__':
    initialize_db()
    LoginWindow()
