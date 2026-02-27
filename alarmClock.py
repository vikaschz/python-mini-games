import time
import winsound
from datetime import datetime

# Validate input properly
while True:
    alarm_input = input("Enter alarm time (HH:MM:SS): ")
    try:
        alarm_time = datetime.strptime(alarm_input, "%H:%M:%S").time()
        break
    except ValueError:
        print("Invalid format. Please use HH:MM:SS")

print("Alarm set for", alarm_time.strftime("%H:%M:%S"))

while True:
    now = datetime.now().time()
    print(f"\rCurrent Time: {now.strftime('%H:%M:%S')}", end="", flush=True)

    if now >= alarm_time:
        print("\nWake up!")

        winsound.PlaySound(
            "audio.wav",
            winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC
        )

        input("Press Enter to stop alarm...")
        winsound.PlaySound(None, winsound.SND_PURGE)
        break

    time.sleep(1)