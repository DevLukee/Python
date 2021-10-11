from pypresence import Presence
import psutil
import os
import time



rpc = Presence("895051738476867704")
rpc.connect()
while True:
    time.sleep(1)
    rpc.update(state=f"CPU: {psutil.cpu_percent()}%", details=f"RAM: {psutil.virtual_memory().percent}%")