from func.SpeakOffline import Speak
import webbrowser
import time

# Open Google Chrome
webbrowser.open('chrome.exe')

# Wait for Chrome to open
time.sleep(2)

# Search for Salman Khan
search_query = "Salman Khan"
webbrowser.open(f'https://www.google.com/search?q={search_query}')