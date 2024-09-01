import threading
import datetime
import pygame
import time
import os

# Initialize pygame mixer for sound
try:
    pygame.mixer.init()
except pygame.error as e:
    print(f"Pygame mixer initialization failed: {e}")

def play_alarm_sound(alarm_message):
    print(f"Alarm triggered! {alarm_message}")
    try:
        file_path = "audio/alarm.WAV"
        if os.path.exists(file_path):
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            time.sleep(5)  # Wait for 5 seconds to ensure the sound plays
        else:
            print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error playing sound: {e}")

def schedule_alarm(alarm_time, alarm_message):
    # Calculate delay in seconds until alarm time
    print(f"current_time: {datetime.datetime.now()}")
    current_time = datetime.datetime.now()
    alarm_time_obj = datetime.datetime.strptime(alarm_time, "%H:%M")
    alarm_time_obj = alarm_time_obj.replace(year=current_time.year, month=current_time.month, day=current_time.day)
    
    if alarm_time_obj < current_time:
        alarm_time_obj += datetime.timedelta(days=1)
    
    delay = (alarm_time_obj - current_time).total_seconds()
    print(f"delay: {delay}")
    
    # Schedule the alarm using threading.Timer
    alarm_timer = threading.Timer(delay, play_alarm_sound, [alarm_message])
    alarm_timer.start()
    
    return alarm_timer

# Schedule an alarm
alarm_time = "04:01"
alarm_message = "Time to wake up!"
alarm_timer = schedule_alarm(alarm_time, alarm_message)
