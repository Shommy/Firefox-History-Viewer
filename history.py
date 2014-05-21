#!/usr/bin/python

import sqlite3
from reporter import HTMLreporter

def main():
	db = sqlite3.connect("places.sqlite")
	db.row_factory = sqlite3.Row
	cursor = db.execute("select title, url, datetime(last_visit_date/1000000, 'unixepoch', 'localtime') as time from moz_places where last_visit_date is not NULL and title is not NULL;")
	rows = [row for row in cursor]
	db.close()

	htmlReporter = HTMLreporter()
	htmlReporter.report(rows)
	

if __name__ == "__main__" : main()