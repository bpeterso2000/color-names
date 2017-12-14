from setuptools import setup, find_packages

from io import open

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='color-names',
    version='1.1',
    url='http://github.com/bpetreso2000/color-names',
    keywords=[
        'color', 'colour', 'colors' 'colours', 'names', 'hex', 'css',
        'html', 'themes', 'styles', 'standards', 'ansi', '256', 'truecolor',
    ],

    author='Brian Peterson',
    author_email='bpeterso2000@yahoo.com',

    description='A curated collection of color names to RGB hex code mappings',
    long_description=readme,

    packages=find_packages(include=['color-names']),
    include_package_data=True,
    zipsafe=False,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: Public Domain',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],

    test_requires=['pytest',]
)
