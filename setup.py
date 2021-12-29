from setuptools import setup
setup(
    name = 'cli_python',
    version = '0.1.0',
    packages = ['cli-python'],
    entry_points = {
        'console_scripts': [
            'cli-python = cli-python.__main__:main'
        ]
    })