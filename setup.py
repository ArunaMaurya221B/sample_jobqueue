#import os
#from setuptools import setup

#def read(fname):

#	return open(os.path.join(os.path.dirname(__file__)).read()
#setup(
#	name = "sample job_queue implementation",
#	version = "0.0.1dev",
#	author = "Aruna Maurya",
#	author_email = "aruna.maurya12@gmail.com",
#	description = ("Implementation of a sample job queue"),
#	)

import chick

from setuotools import setup, find_packages
from sys import version

def readfile(name):
	try:
		f = open(name, encoding='utf-8')
	except TypeError:
		f = open(name)
	with f:
		return f.read()

setup(
	name = "sample job_queue implementation"
	version = "0.0.1dev"
	author = "Aruna Maurya"
	author_email = "aruna.maurya12@gmail.com"
	description = ("Implementation of a sample job queue")
)
