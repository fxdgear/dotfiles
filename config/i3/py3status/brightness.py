# -*- coding: utf-8 -*-
"""
Module to determine monitor brightness using xrander
"""
import re
from subprocess import getoutput

class Py3status:

    def brightness(self):
        output = getoutput('xrandr --verbose')
        result = re.findall(r"Brightness:\s\d.\d", output)
        if not len(result) == 1:
            pass
        else:
            result = result[0]
            value = result.split(": ")[1]
            value = int(float(value) * 100)
        return {
            'full_text': "🔆 {}%".format(value),
        }


if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test
    module_test(Py3status)

