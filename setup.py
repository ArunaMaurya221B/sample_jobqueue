import os
from setuptools import setup

def read(fname):
	return open(os.path.join(os.path.dirname(__file__)).read()
setup(
	name = "sample job_queue implementation",
	version = "0.0.1dev",
	author = "Aruna Maurya",
	author_email = "aruna.maurya12@gmail.com",
	description = ("Implementation of a sample job queue"),
	)
