"""
ASCII Animation: Guy Putting on Glasses
Author: Tristan Becker
Company: Chief AI Advisors
"""

import time

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

# Animate frames
for frame in frames:
    print(frame)
    time.sleep(1.5)  # 1.5 second pause between frames

print("\nAnimation complete!")
