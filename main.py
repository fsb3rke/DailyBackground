import requests
import json
import datetime
import ctypes
import os

def change_last_date(new_date: datetime):
    new_date_formatted = new_date.strftime('%Y-%m-%d')
    last_date_content = open("lastdate.json", "r").read()
    last_date_json = json.loads(last_date_content)
    last_date_json["date"] = new_date_formatted
    last_date_dumps = json.dumps(last_date_json)
    open("lastdate.json", "w").write(last_date_dumps)

def check_is_date_different(current_date: datetime):
    current_date_formatted = current_date.strftime('%Y-%m-%d')
    last_date_content = open("lastdate.json", "r").read()
    last_date_json = json.loads(last_date_content)
    last_date_formatted = last_date_json["date"]
    if current_date_formatted != last_date_formatted:
        return True
    else:
        return False


TOKEN = "" # ACCESS KEY

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
