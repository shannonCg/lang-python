import webbrowser
import time

"""
    open youtube video after 5 seconds and repeat it three times
"""

count = 0
print("This program started on ", time.ctime())
while count < 3:
    time.sleep(5)
    webbrowser.open('https://www.youtube.com/watch?v=kK1MaJ6xX-s')
    count += 1
