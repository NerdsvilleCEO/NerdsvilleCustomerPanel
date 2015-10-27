try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from NerdsvilleCustomerPanel import __version__

config = {
  'description': 'NerdsvilleCustomerPanel',
  'author': 'Nerdsville LLC',
  'version': __version__,
  'packages': ['NerdsvilleCustomerPanel'],
  'name': 'NerdsvilleCustomerPanel'
}

setup(**config)
