#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Use in i3wm with:
Save as screeshot.py somewhere into your PATH
bindsym --release Print exec --no-startup-id screenshot.py
"""

import os
import shutil
from subprocess import Popen, PIPE
from tempfile import NamedTemporaryFile

SCREENSHOT_UTILITY = "/usr/bin/scrot -s -o"  # /usr/bin/import


def feed_xclipboard(filename):
    pipe = Popen("xclip -sel clip", shell=True, stdin=PIPE).stdin
    pipe.write(bytes(filename, "utf-8"))
    pipe.close()


def import_screenshot():
    filename = NamedTemporaryFile(
        suffix=".png",
        prefix="screenshot_",
        dir=os.path.expanduser("~/tmp"),
        delete=False,
    ).name
    p = Popen(SCREENSHOT_UTILITY + " " + filename, shell=True)
    sts = os.waitpid(p.pid, 0)[1]
    try:
        return copytokeybase(filename)
    except Exception:
        return filename


def copytokeybase(filename):
    screenshot_path = "/keybase/public/fxdgear/screenshots"
    shutil.copy2(filename, screenshot_path)
    screenshot_url = os.path.join(
        "https://fxdgear.keybase.pub/screenshots", os.path.split(filename)[-1]
    )
    return screenshot_url


if __name__ == "__main__":
    screenshot = import_screenshot()
    feed_xclipboard(screenshot)
