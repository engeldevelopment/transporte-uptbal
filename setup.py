import os
import time
import random
from setuptools import setup


def version():
	if os.environ.get('BUILD_NUMBER'):
		return os.environ.get('BUILD_NUMBER')
	return os.environ.get('GITHUB_ACTION', '1.0.0')


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
