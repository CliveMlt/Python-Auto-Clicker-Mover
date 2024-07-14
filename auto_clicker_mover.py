import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import random

# Constants for the mouse button and control keys
BUTTON = Button.left
START_STOP_KEY = KeyCode(char=']')
EXIT_KEY = KeyCode(char='[')
MAX_CLICKS = 5000
MOVE_INTERVAL_MIN = 750
MOVE_INTERVAL_MAX = 1000

#____________________________________________________________________________________________________

class ClickMouse(threading.Thread):
    def __init__(self, button):
        super(ClickMouse, self).__init__()
        self.button = button
        self.running = False
        self.program_running = True
        self.click_counter = 0
        self.next_move_click = random.randint(MOVE_INTERVAL_MIN, MOVE_INTERVAL_MAX)
        self.mouse = Controller()

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running and self.click_counter < MAX_CLICKS:
                delay = random.uniform(0.9, 2.1)
                self.mouse.click(self.button)
                self.click_counter += 1

                if self.click_counter >= self.next_move_click:
                    self.move_mouse_randomly()
                    self.next_move_click += random.randint(MOVE_INTERVAL_MIN, MOVE_INTERVAL_MAX)

                print(f"Click #{self.click_counter} - Delay: {delay:.2f} seconds")
                time.sleep(delay)

            if self.click_counter >= MAX_CLICKS:
                self.exit()
            else:
                sleep_time = random.uniform(1.3, 2.3)
                print(f"Paused - Sleep Time: {sleep_time:.2f} seconds")
                time.sleep(sleep_time)

    def move_mouse_randomly(self):
        dx = random.choice([-2, -1, 1, 2])
        dy = random.choice([-2, -1, 1, 2])
        current_position = self.mouse.position
        new_position = (current_position[0] + dx, current_position[1] + dy)
        self.mouse.position = new_position
        print(f"Moved mouse to {new_position}")

def on_press(key):
    if key == START_STOP_KEY:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == EXIT_KEY:
        click_thread.exit()
        listener.stop()

# Initialize and start the clicking thread
click_thread = ClickMouse(BUTTON)
click_thread.start()

#____________________________________________________________________________________________________

# Set up keyboard listener
with Listener(on_press=on_press) as listener:
    listener.join()
