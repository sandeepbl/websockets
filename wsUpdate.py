import sys
import time,json
import sqlite3
import threading

def send_inputs():
	conn1 = sqlite3.connect('twaData.db')
	c1 = conn1.cursor()
	counter = 0
	while True:		
		inputList = c1.execute('select * from userInput')
		for input in inputList:
			print {"section":input[0],"userName":input[1],"twaAgendaID":input[1],"type":"userInput"}
			sys.stdout.flush()
		notesList = c1.execute('select * from twaNotes')
		for notes in notesList:
			print {"noteSection" : notes[0], "notes" : notes[1], "userName" : notes[2], "twaAgendaID" : notes[3],"type":"notes"}
			sys.stdout.flush()		
		if counter == 3:
			c1.execute('delete from userInput')
			conn1.commit()
			counter = 0
		else:
			counter += 1
		time.sleep(1)
			
# Comment from here to ----------------------------->
# from datetime import datetime
# def send_time():
	# while True:
		# time_data = '{"type":"time","time":"' + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + '"}'
		# print time_data
		# sys.stdout.flush()
		# time.sleep(1)
# sendtimer = threading.Thread(target=send_time)	
# sendtimer.start()
# here to remove sending time stamp to websocket <---
conn = sqlite3.connect('twaData.db')
c = conn.cursor()
c.execute('delete from userInput')
conn.close()
sendInputs = threading.Thread(target=send_inputs)	
sendInputs.start()

while True:
	try:
		
		inputstream = sys.stdin.readline()
		sys.stdin.flush()
		if str(inputstream) != '':
			inputstream_json =  json.loads(sys.stdin.readline())
			if inputstream_json['type'] == 'userInput':
				conn = sqlite3.connect('twaData.db')
				c = conn.cursor()
				c.execute('INSERT OR REPLACE INTO userInput(section, userName, twaAgendaID) VALUES("'+inputstream_json['section']+'","'+inputstream_json['userName']+'","'+inputstream_json['twaAgendaID']+'")')
				conn.commit()
				conn.close()
			print str(inputstream_json)
			sys.stdout.flush()
			if inputstream_json['type'] == 'notes':
				conn = sqlite3.connect('twaData.db')
				c = conn.cursor()
				c.execute('INSERT OR REPLACE INTO twaNotes(noteSection, notes, userName, twaAgendaID, notesID) VALUES("'+inputstream_json['noteSection']+'","'+inputstream_json['notes']+'","'+inputstream_json['userName']+'","'+inputstream_json['twaAgendaID']+'","'+inputstream_json['noteSection']+'_'+inputstream_json['twaAgendaID']+'")')
				conn.commit()
				conn.close()
	except KeyboardInterrupt:
		sys.exit(0)