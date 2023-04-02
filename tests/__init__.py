from setuptools import setup

setup(
    name = 'booklover',
    version = '1.0.0',
    author = 'zeitgeistf',
    author_email = 'shawnsfeng@gmail.com',
    packages = ['src/booklover'],
    description = 'A package helps booklover to manage their read books',
    install_requires = [
        "pandas"
    ],
)
