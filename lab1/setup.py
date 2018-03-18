from setuptools import setup

setup(name='Exchange course analyzer',
      author='Vadim Scherbina, Ilya Telefus',
      packages=['bank_analyzer'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'], install_requires=['requests', 'lxml', 'coverage'],)