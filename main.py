import requests
import json
import datetime

TOKEN = "" # ACCESS KEY

today = datetime.datetime.today()
now_time = datetime.datetime.now()

while now_time.hour == 00:
    a = requests.get(f"https://api.unsplash.com/photos/random?count=1&client_id={TOKEN}")
    m_a = json.loads(str(json.dumps(a.json()[0])))

    photo_description = m_a["description"]
    photo_url = m_a["urls"]["raw"]

    img_blob = requests.get(photo_url).content
    strToday = today.strftime("%Y-%m-%d")
    with open(f"images/{strToday}.jpg", "wb") as img_file:
        img_file.write(img_blob)
        