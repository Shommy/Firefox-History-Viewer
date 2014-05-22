#!/usr/bin/python

from modules.reporter import HTMLreporter
from modules.database import DBReader

import sys, getopt

def main(argv):
	dbPath = None
	reportPath = None

	usage = """
	Usage: history.py [OPTIONS]

	Options:
		-h,  --help :  print this usage
		-p,  --path :  path to places.sqlite file
		               default is the one from current user 
		-o,  --out  :  generated report file
	"""
	if len(argv):
		try:
			opts, args = getopt.getopt(argv[1:], "hp:o:", ["help", "path=", "out="])
		except getopt.GetoptError:
			print usage
			sys.exit(1)
		else:
			for opt, arg in opts:
				if opt in ("-h", "--help"):
					print usage
					sys.exit(0)
				elif opt in ("-p", "--path"):
					dbPath = arg
				elif opt in ("-o", "--out"):
					reportPath = arg
				else:
					assert False, "Unhandled option"
	try:
		db = DBReader(dbPath)
		htmlReporter = HTMLreporter()
		htmlReporter.report([row for row in db], reportPath)
		db.close()
	except ValueError as e:
		print "Error: %s" % e.args[0]
		print usage
	except:
		print "Unknown error"
		print usage
	

if __name__ == "__main__" : main(sys.argv)
