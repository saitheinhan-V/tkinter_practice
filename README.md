# Tkinter Python

- Some example practice with tkinter python

## Build Window EXE

### pyinstaller

- pip install pyinstaller

### basic command to create exe

- pyinstaller --onefile main.py

### for Tkinter GUI

- pyinstaller --onefile --windowed main.py

### if it includes image file ("file;destination" > for window)

- pyinstaller --onefile --windowed --add-data "profile.png;." main.py
  (when profile.png is directly under project directory)
  (OR)
- pyinstaller --onefile --windowed --add-data "images;images" main.py
  (when profile.png is under images/ folder under project directory)

### to fix the path problem

```
import sys
import os
def resource_path(relative_path):
    try:
        base_path = sys.\_MEIPASS # temp folder (when exe runs)
    except Exception:
        base_path = os.path.abspath(".")

return os.path.join(base_path, relative_path)
```

### use like this:

- image_path = resource_path("profile.png")
  (OR)
- image_path = resource_path("images/profile.png")

### tk image

- profile_image = Image.open(image_path)

### frame (use frame as a container itself)

- content_frame = tk.Frame(self, bg="#0090C9")
- content_frame.grid(row=1, column=0)
