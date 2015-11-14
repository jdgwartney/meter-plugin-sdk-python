from distutils.core import setup

setup(
    name='meter-plugin-sdk',
    version='0.1.0',
    url="http://github.io/boundary/meter-plugin-sdk-python",
    author='David Gwartney',
    author_email='david_gwartney@bmc.com',
    packages=['meterpluginsdk', ],
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
