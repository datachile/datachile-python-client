from setuptools import setup

setup(
    name='opendata',
    version='0.0.1',
    description='Python client to manage Datawheel APIs, inspired in Mondrian Rest PY by @jazzido',
    url='http://github.com/Datawheel/opendata',
    author='Carlos Navarrete',
    author_email='cnavarreteliz@gmail.com',
    license='MIT',
    packages=['opendata'],
    install_requires=[
        'mondrian_rest==0.1',
        'numpy',
        'requests',
        'pandas'
    ],
    dependency_links=[
        "git+https://github.com/jazzido/py-mondrian-rest.git#egg=mondrian_rest-0.1"
    ],
    zip_safe=True
)