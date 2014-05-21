#!/usr/bin/python

import os, os.path, sqlite3

class DBReader(object):
	def __init__(self, dbPath = None):
		if dbPath is None:
			self.dbPath = _findPath()
		else:
			self.dbPath = dbPath

	def _findPath():
		username = os.popen("whoami").read().strip()
		path = "/home/" + username + "/"
		path += [name for name in os.listdir(path) if name.endswith(".defalt")][0]
		path += "/places.sqlite"
		return path

	@property
	def dbPath(self):
		return self._dbPath

	@dbPath.setter
    def dbPath(self, path):
    	if not os.path.isfile(path):
    		raise 
        self._dbPath = path
        self._db = sqlite3.connect(self._dbPath)
        self._db.row_factory = sqlite3.Row

    @dbPath.deleter
    def dbPath(self): 
    	self.close()

    def close(self):
    	self._db.close()
        del self._dbPath