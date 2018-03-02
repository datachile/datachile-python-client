from setuptools import setup

setup(
    name='datachile',
    version='0.0.3',
    description='Python client for manage DataChile API',
    url='http://github.com/datawheel/datachile-api',
    download_url='https://github.com/datawheel/datachile-api/archive/0.0.3.tar.gz',
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