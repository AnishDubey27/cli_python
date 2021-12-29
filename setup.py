from setuptools import setup
setup(
    name = 'cli_python',
    version = '0.1.0',
    packages = ['cli_python'],
    entry_points = {
        'console_scripts': [
            'cli_python = cli_python.__main__:main'
        ]
    })