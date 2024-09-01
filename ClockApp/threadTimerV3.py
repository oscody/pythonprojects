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

def play_alarm_sound(alarm_message, duration=30):
    print(f"Alarm triggered! {alarm_message}")
    try:
        file_path = "audio/alarm.WAV"
        if os.path.exists(file_path):
            end_time = time.time() + duration
            while time.time() < end_time:
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play()
                time.sleep(5)  # Sleep for the duration of one play, adjust as necessary
        else:
            print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error playing sound: {e}")

def schedule_alarm(alarm_time, alarm_message, duration=30):
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
    alarm_timer = threading.Timer(delay, play_alarm_sound, [alarm_message, duration])
    alarm_timer.start()
    
    return alarm_timer

# Schedule an alarm
alarm_time = "04:07"
alarm_message = "Time to wake up!"
alarm_timer = schedule_alarm(alarm_time, alarm_message, duration=30)  # Plays for 30 seconds
