from setuptools import setup

setup(
    name='datachile',
    version='0.0.1',
    description='Python client for manage DataChile API',
    url='http://github.com/cnavarreteliz/datachile-api',
    download_url='https://github.com/cnavarreteliz/datachile-api/archive/0.0.1.tar.gz',
    author='Carlos Navarrete - Datawheel LLC',
    author_email='cnavarreteliz@gmail.com',
    license='MIT',
    packages=['datachile'],
    install_requires=[
        'mondrian_rest==0.1',
        'numpy',
        'requests'
    ],
    dependency_links=[
        "git+https://github.com/jazzido/py-mondrian-rest.git#egg=mondrian_rest-0.1"
    ],
    keywords = ['python', 'mondrian', 'olap', 'api'],
    zip_safe=True
)