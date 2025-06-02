#!/usr/bin/python3
import psutil
from pynotifier import Notification

battery = psutil.sensors_battery()
percentage = battery.percent
print(percentage)

Notification(title = "Battery status", description = f"Battery percentage remaining {percentage}", duration = 10)