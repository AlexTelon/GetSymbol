from setuptools import setup

setup(
    name='GetSymbol',
    version='0.1',
    packages=['getsymbol'],
    entry_points={
        'console_scripts': [
            'getsymbol = getsymbol.main:main'
        ]
    },
    author='Alex Telon',
    author_email='alex.telon@gmail.com',
    description='A tool to get the utf char from freetext english description using AI',
    url='https://github.com/AlexTelon/getsymbol',
    license='MIT'
)
