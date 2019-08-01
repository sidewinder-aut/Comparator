#!/usr/bin/python

import SC_Suite, sys
SC = SC_Suite

class SC_Log():
	
	#
	#	Class for copying stdout output to a logfile
	#
	
	def __init__(self):
		self.terminal = sys.stdout
		self.log = open('SC_Suite_log.dat', 'a')
		
	def write(self, message):
		self.terminal.write(message)
		self.log.write(message)
		self.log.flush()
		self.terminal.flush()
		
#	def flush(self):
		
		
sys.stdout = SC_Log()