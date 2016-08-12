import webbrowser 
import time 
import sys 

total_windows = 4 
count = 0 

while (count < total_windows): 
    time.sleep(4) 
    webbrowser.open('https://www.youtube.com/watch?v=03SGZtSUAZE') 
    count += 1 
    
sys.exit()