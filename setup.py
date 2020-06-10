from setuptools import setup, find_packages
with open('README.rts') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name="Simple BlackJack",
    version="0.1.0",
    description="A simple BlackJack game created using Python",
    long_description=readme,
    author="Huy Le",
    author_email="qhuy2301@gmail.com",
    url="https://github.com/qhuy2301/Simple-BlackJack",
    license=license,
    packages=find_packages(exclude=('tests' 'docs'))
)
