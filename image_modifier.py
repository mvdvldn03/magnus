from PIL import Image, ImageDraw, ImageFont
import datetime
import random
from subprocess import Popen, PIPE

def send_image():
    d = str(datetime.date.today() + datetime.timedelta(days=1))
    d_arr = d.split("-")
    month_dict = {'01':'January', '02':'February','03':'March','04':'April','05':'May','06':'June',
                  '07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}
    d_str = f"{month_dict[d_arr[1]]} {d_arr[2]}, {d_arr[0]}"

    rand_time = f"7:{random.randint(10,20)}:{random.randint(10,59)}"

    img = Image.open("~/Documents/template.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Helvetica.ttc", 72)

    w1, h1 = draw.textsize(f"{d_str}",font=font)
    draw.text(((720-w1)/2, 715),f"{d_str}",(74, 73, 73),font=font)

    w2, h2 = draw.textsize(f"0{rand_time}",font=font)
    draw.text(((720-w2)/2, 805),f"0{rand_time}",(74, 73, 73),font=font)
    img.save("~/Documents/magnus_app.png")

    scpt = f'''
            set filePath to POSIX file "~/Documents/magnus_app.png"
            
            tell application "Messages"
                set targetService to 1st account whose service type = iMessage
                set targetBuddy to participant "PHONE_NUMBER" of targetService
                send file filePath to targetBuddy
            end tell
            '''

    p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    stdout, stderr = p.communicate(scpt)

if __name__ == "__main__":
    x = 0
    while(x < 70):
        if datetime.datetime.today().weekday() != 4 and datetime.datetime.today().weekday() != 5:
            if int(datetime.datetime.now().hour) > 20 and x % 2 == 0:
                send_image()
                x += 1
                print(x)
            if int(datetime.datetime.now().hour) < 12 and x % 2 == 1:
                x += 1
                print(x)
