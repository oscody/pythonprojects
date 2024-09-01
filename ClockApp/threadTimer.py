import threading
import datetime
import pygame

# Initialize pygame mixer for sound
pygame.mixer.init()

def play_alarm_sound(alarm_message):
    print(f"Alarm triggered! {alarm_message}")
    pygame.mixer.music.load("audio/alarm.WAV")
    pygame.mixer.music.play()

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
alarm_time = "03:57"
alarm_message = "Time to wake up!"
alarm_timer = schedule_alarm(alarm_time, alarm_message)
