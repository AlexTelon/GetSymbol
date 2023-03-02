from setuptools import setup

setup(
    name='getutf',
    version='0.1',
    packages=['getutf'],
    entry_points={
        'console_scripts': [
            'getutf = getutf.main:main'
        ]
    },
    author='Alex Telon',
    author_email='alex.telon@gmail.com',
    description='A tool to get the utf char from freetext english description using AI',
    url='https://github.com/AlexTelon/getutf',
    license='MIT'
)
