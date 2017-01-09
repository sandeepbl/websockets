from sys import stdout,argv
inputStr = ''
while True:
	try:
		inputStr = input()
	except EOFError:
		print inputStr,str(argv[1])
		stdout.flush()