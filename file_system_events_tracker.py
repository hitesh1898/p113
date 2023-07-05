import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/Kuttimma/Downloads"

# Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):


    #1_on_created
    def on_created(self,event):
        print(f"Hey, {"C:/Users/samsung/Downloads/"} has been created")
    #2_on_deleted
    def on_deletd(self,event):
        print(f"OOps!,Someone deleted {"C:/Users/samsung/Downloads/"} ")
    #3_on_modified
    def on_modified(self,event):
        print(f"Hey there!, {"C:/Users/samsung/Downloads/"} has been modified")
    #4_on_moved
def on_moved(self,event):
        print(f"Someone moved {"C:/Users/samsung/Downloads/"} to{"C:\Users\samsung\Desktop\downloded_files"}")
        


# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


#5_Write a exception for keyboardInterrupt



try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()




