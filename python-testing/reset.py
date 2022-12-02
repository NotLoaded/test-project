import os
import shutil


filepath = "./result.txt"
history_directory = "./history/"
shutil.rmtree(history_directory)
os.remove(filepath)

