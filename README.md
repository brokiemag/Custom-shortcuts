# Custom Shortcuts 

Custom Shortcuts help you to make/use custom shortcuts in any OS.

## Installation

Use the package manager [pip](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) to install -r requirements.txt .

```bash
pip install -r requirements.txt
```

## Usage

```python
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
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Brokiemag](https://brokiemag.me)
