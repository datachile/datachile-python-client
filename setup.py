from setuptools import setup

setup(
    name='datachile',
    version='0.0.7',
    description='Python client for manage DataChile API',
    url='http://github.com/datachile/datachile-python-client',
    download_url='https://github.com/datachile/datachile-python-client/archive/0.0.7.tar.gz',
    author='Carlos Navarrete - Datawheel LLC',
    author_email='cnavarreteliz@gmail.com',
    license='MIT',
    packages=['datachile'],
    install_requires=[
        'mondrian-rest',
        'numpy',
        'requests'
    ],
    keywords = ['python', 'mondrian', 'olap', 'api'],
    zip_safe=True
)