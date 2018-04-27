from setuptools import setup

setup(
    name='datachile',
    version='0.0.6',
    description='Python client for manage DataChile API',
    url='http://github.com/datachile/datachile-python-client',
    download_url='https://github.com/datachile/datachile-python-client/archive/0.0.6.tar.gz',
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
        "git+https://github.com/datachile/datachile-python-client/tarball/9939446829ce42cbdefdf8c970a21deb9a5a4587#egg=mondrian_rest-0.1"
    ],
    keywords = ['python', 'mondrian', 'olap', 'api'],
    zip_safe=True
)