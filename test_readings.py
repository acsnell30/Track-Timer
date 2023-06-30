from MCP3008 import MCP3008
import time

adc = MCP3008()


while True:
    start_line_sensor = adc.read(channel = 0)
    finish_line_sensor = adc.read(channel = 1)
    print("start line: ",  start_line_sensor)
    print("finish line: ", finish_line_sensor)
    print("\n")
    time.sleep(1)
