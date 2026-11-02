"""Check whether the mouse wheel scrolls your quiz page, and whether the agent can measure it.

Open the quiz, run this, and switch to the quiz within 5 seconds. It turns the wheel one notch,
then presses Page Down, then puts the page back, and saves scroll_before.jpg, scroll_after_wheel.jpg
and scroll_after_pagedown.jpg next to this file. Nothing is clicked.
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import mss
import pyautogui

import mcq_agent


def changed(before, after):
    """Share of the screen that differs between two screenshots, from small grey thumbnails."""
    a, b = mcq_agent.thumbnail(before), mcq_agent.thumbnail(after)
    return sum(abs(x - y) > 24 for x, y in zip(a, b)) / len(a)


def report(label, before, after):
    print(f"{label}: {changed(before, after):.0%} of the screen changed; measured shift {mcq_agent.measure_shift(before, after)} px")


print("Switch to the quiz. Starting in 5 seconds. Do not touch the mouse or keyboard.")
time.sleep(5)
with mss.MSS() as sct:
    monitor = next((m for m in sct.monitors[1:] if m.get("is_primary")), sct.monitors[1])
    x = monitor["left"] + monitor["width"] // 2
    y = monitor["top"] + monitor["height"] // 2
    pyautogui.moveTo(x, y)
    time.sleep(0.5)
    print(f"Monitor {monitor['width']}x{monitor['height']}, mouse at {pyautogui.position()}")

    before = mcq_agent.capture(sct, monitor)
    before.save("scroll_before.jpg", quality=85)
    pyautogui.scroll(-mcq_agent.WHEEL_NOTCH)
    time.sleep(1.5)
    after_wheel = mcq_agent.capture(sct, monitor)
    after_wheel.save("scroll_after_wheel.jpg", quality=85)
    report("One wheel notch", before, after_wheel)

    pyautogui.press("pagedown")
    time.sleep(1.5)
    after_key = mcq_agent.capture(sct, monitor)
    after_key.save("scroll_after_pagedown.jpg", quality=85)
    report("Page Down key", after_wheel, after_key)

    pyautogui.press("pageup")
    time.sleep(0.5)
    pyautogui.scroll(mcq_agent.WHEEL_NOTCH)
    print("Put the page back. Pictures saved next to this script.")
