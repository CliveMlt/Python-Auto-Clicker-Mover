# Python-Auto-Clicker-Mover
 
This is a Python script for an auto clicker that simulates mouse clicks at random intervals. The script also includes functionality to start and stop clicking with keyboard controls and stops automatically after 1000 clicks. Additionally, the mouse moves randomly by 1 or 2 pixels once every 750 to 1000 clicks when clicking is active.

## Features

- Clicks the left mouse button at random intervals, the default values are between 0.9 and 2.1 seconds.
- Moves the mouse by 1 or 2 pixels in a random direction once every 750 to 1000 clicks when clicking is active.
- Customizable parameters:
  - Choose the mouse button (`BUTTON`) and control keys (`START_STOP_KEY`, `EXIT_KEY`).
  - Set the maximum number of clicks (`MAX_CLICKS`) before the script stops.
  - Adjust the range (`MOVE_INTERVAL_MIN` to `MOVE_INTERVAL_MAX`) for mouse movement frequency.
- Starts and stops clicking with keyboard keys (`START_STOP_KEY` to start/stop).
- Exits the program with `EXIT_KEY`.

## Requirements

- Python 3.x
- `pynput` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/CliveMlt/Python-Auto-Clicker-Mover.git
    cd auto-clicker-script
    ```

2. Install the required Python packages:

    ```bash
    pip install pynput
    ```

## Usage

1. Modify the script parameters if needed:
    - Open `auto_clicker_mover.py` in a text editor.
    - Change the values of the following constants based on your preferences:
      ```python
      BUTTON = Button.left
      START_STOP_KEY = KeyCode(char=']')
      EXIT_KEY = KeyCode(char='[')
      MAX_CLICKS = 5000
      MOVE_INTERVAL_MIN = 750
      MOVE_INTERVAL_MAX = 1000
      ```

2. Run the script:

    ```bash
    python auto_clicker_mover.py
    ```

3. Control the clicker with the following keys:
    - `]` to start/stop clicking
    - `[` to exit the program

## Example Output
    ```bash
    python .\auto_clicker_mover.py
    Paused - Sleep Time: 1.71 seconds
    Paused - Sleep Time: 2.03 seconds
    Click #1 - Delay: 1.73 seconds
    Click #2 - Delay: 1.93 seconds
    Click #3 - Delay: 1.06 seconds
    Click #4 - Delay: 1.30 seconds
    Click #5 - Delay: 1.67 seconds
    Paused - Sleep Time: 1.84 seconds
    ```


## License
This project is licensed under the MIT License. See the LICENSE file for details.