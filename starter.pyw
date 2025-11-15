import webview
import os

# Get the absolute path to the directory containing this script
dir_path = os.path.dirname(os.path.realpath(__file__))
html_file = os.path.join(dir_path, 'main.html')

webview.create_window("Smart Flashcards – Neo & 2nT_", html_file)
webview.start()
