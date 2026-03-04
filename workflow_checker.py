"""
ASCII Animation: Guy Putting on Glasses
Author: Tristan Becker
Company: Chief AI Advisors
"""

import time
import os

# Simple ASCII frames
frames = [
    """
    O
   /|\\
   / \\
""",
    """
   O
  /|\\
  / \\
Glasses coming...
""",
    """
   O-O
  /|\\
  / \\
Looks sharp!
"""
]

def clear_screen():
    # Clear terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def animate(frames, delay=1.0):
    for frame in frames:
        clear_screen()
        print(frame)
        time.sleep(delay)
    print("\nAnimation complete!")

if __name__ == "__main__":
    animate(frames, delay=1.5)
