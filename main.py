import requests
import json
import datetime
import ctypes
import os
import time
from win10toast import ToastNotifier

def time_format(seconds: int):
    if seconds is not None:
        seconds = int(seconds)
        d = seconds // (3600 * 24)
        h = seconds // 3600 % 24
        m = seconds % 3600 // 60
        s = seconds % 3600 % 60
        if d > 0:
            return '{:02d}D {:02d}H {:02d}m {:02d}s'.format(d, h, m, s)
        elif h > 0:
            return '{:02d}H {:02d}m {:02d}s'.format(h, m, s)
        elif m > 0:
            return '{:02d}m {:02d}s'.format(m, s)
        elif s > 0:
            return '{:02d}s'.format(s)
    return '-'

def send_notification(notification_title: str, notification_body: str, duration: int, icon_path: str, threaded: bool):
    toast = ToastNotifier()
    toast.show_toast(notification_title, notification_body, duration=duration, icon_path=icon_path, threaded=threaded)

def calculate_remaining_time(date: datetime):
    date_formatted = date.strftime("%H-%M-%S")
    date_splitted = date_formatted.split("-")
    date_dict = {"hour": int(date_splitted[0]), "minute": int(date_splitted[1]), "second": int(date_splitted[2])}

    totalMin = 1440 - 60 * date_dict["hour"] - date_dict["minute"]
    hoursRemaining = totalMin // 60
    minRemaining = totalMin % 60

    totalSec = (hoursRemaining*3600)+(minRemaining*60)+date_dict["second"]
    return totalSec

def change_last_date(new_date: datetime):
    new_date_formatted = new_date.strftime('%Y-%m-%d')
    with open("lastdate.json", "r") as f:
        last_date_content = f.read()
    last_date_json = json.loads(last_date_content)
    last_date_json["date"] = new_date_formatted
    last_date_dumps = json.dumps(last_date_json)
    with open("lastdate.json", "w") as f:
        f.write(last_date_dumps)

def check_is_date_different(current_date: datetime):
    current_date_formatted = current_date.strftime('%Y-%m-%d')
    with open("lastdate.json", "r") as f:
        last_date_content = f.read()
    last_date_json = json.loads(last_date_content)
    last_date_formatted = last_date_json["date"]
    if current_date_formatted != last_date_formatted:
        return True
    else:
        return False


TOKEN = "unsplash-api-access-key" # ACCESS KEY

today = datetime.datetime.today()
while True:
    if check_is_date_different(today):
        a = requests.get(f"https://api.unsplash.com/photos/random?count=1&client_id={TOKEN}")
        m_a = json.loads(str(json.dumps(a.json()[0])))

        photo_description = m_a["description"]
        photo_url = m_a["urls"]["raw"]

        img_blob = requests.get(photo_url).content
        strToday = today.strftime("%Y-%m-%d")
        with open(f"images/{strToday}.jpg", "wb") as img_file:
            img_file.write(img_blob)

        ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{os.getcwd()}\\images\\{strToday}.jpg", 0)
        change_last_date(today)
        today = datetime.datetime.today()

        send_notification("Daily Background", f"Background has been updated!\n\nYour background is will be change after\n{time_format(calculate_remaining_time(today))}", 15, "bin/icon.ico", True)

    time.sleep(calculate_remaining_time(today))
