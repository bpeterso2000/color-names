from setuptools import setup, find_packages

setup(
    name='color-names',
    version='1.1.2',
    url='http://github.com/bpeterso2000/color-names',
    keywords=[
        'color', 'colour', 'colors' 'colours', 'names', 'hex', 'css',
        'html', 'themes', 'styles', 'standards', 'ansi', '256', 'truecolor',
    ],

    author='Brian Peterson',
    author_email='bpeterso2000@yahoo.com',

    description='A curated collection of color name, style & theme hex codes.',

    packages=find_packages(include=['color-names']),
    include_package_data=True,
    zipsafe=False,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: Public Domain',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],

    test_requires=['pytest'],
)
