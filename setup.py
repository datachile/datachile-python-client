from setuptools import setup

setup(
    name='opendata_rest',
    version='0.0.1',
    description='Python client to manage Datawheel APIs, inspired in Mondrian Rest PY by @jazzido',
    url='http://github.com/cnavarreteliz/opendata',
    download_url='https://github.com/cnavarreteliz/opendata/archive/0.0.1.tar.gz',
    author='Carlos Navarrete',
    author_email='cnavarreteliz@gmail.com',
    license='MIT',
    packages=['opendata_rest'],
    install_requires=[
        'mondrian_rest==0.1',
        'numpy',
        'requests',
        'pandas',
        'intertools'
    ],
    dependency_links=[
        "git+https://github.com/jazzido/py-mondrian-rest.git#egg=mondrian_rest-0.1"
    ],
    keywords = ['python', 'mondrian', 'olap', 'api'],
    zip_safe=True
)