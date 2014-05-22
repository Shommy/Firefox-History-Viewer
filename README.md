FirefoxHistoryList
==================


Simple history viewer for Mozilla Firefox in Python. 

Requires:
- Linux
- Python 2.7
- sqlite3
- jinja2
- Mozilla Firefox

Usage: 

	history.py [OPTIONS]
	Options:
		-h,  --help :  print this usage
		-p,  --path :  path to places.sqlite file
		               default is the one from current user 
		-o,  --out  :  generated report file
		               default is "output.html" in current folder
