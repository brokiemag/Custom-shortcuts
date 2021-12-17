# '''PLease click the last key/letter once to work properly'''
import keyboard,os,psutil
from datetime import datetime
from time import sleep

hotkey = "shift + ctrl + g"
edge = "shift + ctrl + e"
process = psutil.Process(os.getpid())
print(f"'{process.memory_info().rss}'bytes is being consumed by this program")

while True:
  if keyboard.is_pressed(hotkey):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Chrome Hotkey detected at {current_time}")
    sleep(0.001)
    os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
  if keyboard.is_pressed(edge):
      now = datetime.now()
      current_time = now.strftime("%H:%M:%S")
      print(f"Edge Hotkey detected at {current_time}")
      sleep(0.001)
      os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
