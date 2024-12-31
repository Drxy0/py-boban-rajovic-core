from setuptools import setup, find_packages

setup(
    name='boban-rajovic-song-injector',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy'
    ],
    author='Drxy0',
    author_email='/',
    description='A script to inject Boban Rajovic songs into a database using Flask-SQLAlchemy',
    url='https://github.com/Drxy0/py-boban-rajovic-song-injector',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
