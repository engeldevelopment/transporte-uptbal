import os
import time
import random
from setuptools import setup


def version():
	if os.environ.get('GITHUB_ACTION'):
		return os.environ.get('GITHUB_ACTION')
	random.seed(time.time())
	return random.random()


def url():
    return "https:/github.com/{0}".format(os.environ.get("GITHUB_REPOSITORY"))


setup(
	name='transporte-uptbal',
	author='Engel J. Pinto R.',
	author_email='engeljavierpinto@gmail.com',
	description='Una prueba con github actions',
	version=version(),
	packages=['transporte'],
	url=url()
)
