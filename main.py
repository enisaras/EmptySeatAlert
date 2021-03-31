import requests
import json
import os, config
newline = "\n"
link = "https://rcos-orca.herokuapp.com/202109/sections?crns=50071&crns=54274&crns=52268&crns=50379&crns=53847&crns=52463&crns=51196"
data = requests.get(link)

json = data.json()

className = []
maxEnrollment = []
currentEnrollment = []
emptySeats = []
classes = {}
for i in range(len(json)):
    className.append(json[i]["course_title"])
    maxEnrollment.append(json[i]["max_enrollments"])
    currentEnrollment.append(json[i]["enrollments"])
    emptySeats.append(maxEnrollment[i] - currentEnrollment[i])
    classes.update({className[i] : emptySeats[i]})

if config.DISCORD_WEBHOOK_URL:
    chat_message = {
        "username": "Empty Seat Alert",
        "content": 
                  f'<@750020267501158502>\n{newline.join(f"Title:{key} Empty Seats:{value}" for key, value in classes.items())}'
                  }
             
    requests.post(config.DISCORD_WEBHOOK_URL, json=chat_message)