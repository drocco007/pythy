from setuptools import setup

setup(
	name='PyPing',
	version='0.1dev',
	packages=['pyping', ],
    scripts=['pyp.py'],
    entry_points = {
	    'console_scripts': [ 'pyp = pyp:main' ]
    },
    install_requires=[],
	license='Creative Commons Attribution-Noncommercial-Share Alike license',
	long_description=open('README.rst').read(),
	url='http://is.gd/pythy',

    author='Daniel J. Rocco',
    author_email='drocco@gmail.com'
)
