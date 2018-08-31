# DRY-cleaner

Visually detect [repetition](https://www.youtube.com/watch?v=WQrUCqd41Ww) in your source code
and know which part to [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) out.
Inspired by [SongSim](https://colinmorris.github.io/SongSim).

![Example](https://user-images.githubusercontent.com/7141845/31598759-a8030d52-b24f-11e7-8dc2-109e6ed5b395.png)

## Setup

_Please note that (for now) this only works for Typescript code_

* Install [ANTLR4](https://github.com/antlr/antlr4) and Python 3
* Run `pip3 install -r requirements.txt` to install the Python runtime of ANTLR
* Run `antlr4 -Dlanguage=Python3 Code.g4` to generate the code parser
* Run `python drycleaner.py ~/Projects/some-project/src .ts` to generate some output

