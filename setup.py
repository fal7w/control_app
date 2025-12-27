from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in control_app/__init__.py
from control_app import __version__ as version

setup(
	name="control_app",
	version=version,
	description="managing soft feedback and test case ",
	author="fintechsys",
	author_email="m.nozili@fintechsys.net",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
