from setuptools import setup

setup(
    name = 'booklover',
    version = '0.1.0',
    author = 'zeitgeistf',
    author_email = 'shawnsfeng@gmail.com',
    url = 'https://github.com/zeitgeistf/booklover',
    packages = ['booklover'],
    description = 'A package to help booklovers to manage their read books',
    install_requires = [
        "pandas"
    ]
)
