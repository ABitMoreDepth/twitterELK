from io import open

from setuptools import find_packages, setup

with open('ingress/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip(' \'"')
            break
    else:
        version = '0.0.1'

with open('README.rst', 'r', encoding='utf-8') as f:
    README = f.read()

REQUIRES = []

setup(
    name='ingress',
    version=version,
    description='',
    long_description=README,
    author='Sam Martin',
    author_email='nivekkas@gmail.com',
    maintainer='Sam Martin',
    maintainer_email='nivekkas@gmail.com',
    url='https://github.com/_/ingress',
    license='MIT',
    keywords=[
        '',
    ],
    entry_points={
        'console_scripts': ['ingress = ingress.main:main'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    install_requires=REQUIRES,
    tests_require=[
        'coverage',
        'pytest',
    ],
    packages=find_packages(),
)
