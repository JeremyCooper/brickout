# brickout
Simple extendable brickout implementation in Python

Levels can be easily added by adding a function returning an array of brick positioning data. The function name should be of format `leveln`.
Levels can be chosen by changing the function name passed to the initBricks brick construction function.

Dependencies:
Python2.7
pygame

Tested on:
Arch Linux
macOS
