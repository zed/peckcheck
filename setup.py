from distutils.core import setup
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1.v2.6'

sys.path.insert(0, here)
import peckcheck
peckcheck_doc = 'Description\n===========\n' + peckcheck.__doc__

setup(name='peckcheck',
      version=version,
      description="Randomized testing library for Python; like a subset of Haskell's QuickCheck.",
      long_description=README + '\n\n' + NEWS + '\n\n' + peckcheck_doc,
      classifiers="""Development Status :: 7 - Inactive
Intended Audience :: Developers
License :: OSI Approved :: Python Software Foundation License
Operating System :: OS Independent
Programming Language :: Python :: 2.6
Topic :: Software Development :: Testing""".split('\n'),
      keywords='quickcheck testing',
      author='Darius Bacon',
      author_email='darius@wry.me',
      url='http://accesscom.com/~darius/software/clickcheck.html',
      license='PSF License',
      py_modules=['peckcheck'])
