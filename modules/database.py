#!/usr/bin/python

import os, sqlite3

def findPath():
	username = os.popen("whoami").read().strip()
	path = "/home/" + username + "/.mozilla/firefox/"
	path += [name for name in os.listdir(path) if name.endswith(".default")][0]
	path += "/places.sqlite"
	return path

class DBReader(object):
	def __init__(self, dbPath = None):
		if dbPath is None:
			self.dbPath = findPath()
		else:
			self.dbPath = dbPath

	@property
	def dbPath(self):
		return self._dbPath

	@dbPath.setter
	def dbPath(self, path): 
		self._dbPath = path
		if not os.path.isfile(path):
			raise ValueError("Invalid path")

		self._db = sqlite3.connect(self._dbPath)
		self._db.row_factory = sqlite3.Row

	@dbPath.deleter
	def dbPath(self): 
		self.close()

	def close(self):
		self._db.close()
		del self._dbPath

	def __iter__(self):
		query = """
		SELECT title, url, datetime(last_visit_date/1000000, 'unixepoch', 'localtime') as time
		FROM moz_places 
		WHERE last_visit_date IS NOT NULL;
		"""
		try:
			cursor = self._db.execute(query)
		except sqlite3.DatabaseError as e:
			print "Error: " + e.args[0]

		for row in cursor:
			yield dict(row)

def main():
	print findPath()

	rows = [row for row in DBReader()]
	
	for row in rows:
		print row['title']

if __name__ == "__main__" : main()
