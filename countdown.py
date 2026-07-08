#Countdown Alert

import time

total_seconds = 10

for seconds_left in range(total_seconds, 0, -1):
    print(f"\b\b{seconds_left}", end="", flush=True)
    time.sleep(1)
print(f"\bTimes up")