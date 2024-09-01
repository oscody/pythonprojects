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

# Global flag to control the alarm sound
alarm_running = False

def play_alarm_sound():
    global alarm_running
    file_path = "audio/alarm.WAV"
    
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    
    while alarm_running:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        time.sleep(5)  # Adjust sleep time according to the length of the sound

def start_alarm():
    global alarm_running
    alarm_running = True
    alarm_thread = threading.Thread(target=play_alarm_sound)
    alarm_thread.start()

def stop_alarm():
    global alarm_running
    alarm_running = False
    pygame.mixer.music.stop()

def main():
    while True:
        user_input = input("Enter 'play' to start the alarm, 'stop' to stop it, or 'quit' to exit:\n").strip().lower()
        
        if user_input == "play":
            if not alarm_running:
                print("Starting alarm...")
                start_alarm()
            else:
                print("Alarm is already running.")
        
        elif user_input == "stop":
            if alarm_running:
                print("Stopping alarm...")
                stop_alarm()
            else:
                print("No alarm is currently running.")
        
        elif user_input == "quit":
            print("Exiting...")
            if alarm_running:
                stop_alarm()
            break
        
        else:
            print("Invalid input. Please enter 'play', 'stop', or 'quit'.")

if __name__ == "__main__":
    main()
