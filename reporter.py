#!/usr/bin/python

from jinja2 import Template

class HTMLreporter(object):
	def __init__(self, templateFileName = "templates/report.htm"):
		templateFile = open(templateFileName)
		self._template = Template(templateFile.read())
		templateFile.close()
		
	def report(self, rows, reportFileName = "output.html"):
		reportFile = open(reportFileName, "wt")
		reportFile.write(self._template.render(rows = rows).encode("utf-8"))
		reportFile.close()
