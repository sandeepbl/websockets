import sys
import time,json

# Comment from here to ----------------------------->
# from datetime import datetime
# import threading
# def send_time():
	# while True:
		# time_data = '{"type":"time","time":"' + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + '"}'
		# print time_data
		# sys.stdout.flush()
		# time.sleep(1)
# sendtimer = threading.Thread(target=send_time)	
# sendtimer.start()
# here to remove sending time stamp to websocket <---

while True:
	inputstream = sys.stdin.readline()
	sys.stdin.flush()
	if str(inputstream) != '':
		inputstream_json =  json.loads(sys.stdin.readline())
		for element in inputstream_json:
			print element,inputstream_json[element]
		sys.stdout.flush()