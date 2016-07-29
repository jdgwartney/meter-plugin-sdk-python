from distutils.core import setup
from meterplugin import __version__

setup(
    name='meterplugin',
    version=__version__,
    url="http://github.io/boundary/meter-plugin-sdk-python",
    author='David Gwartney',
    author_email='david_gwartney@bmc.com',
    packages=['meterplugin', ],
    scripts=[
    ],
    package_data={'meterplugin': ['templates/*']},
    license='LICENSE',
    description='TrueSight Pulse Meter Plugin SDK for Python',
    long_description=open('README.txt').read(),
    install_requires=[
        "tinyrpc",
    ],
)
