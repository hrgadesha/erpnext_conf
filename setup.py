from setuptools import setup, find_packages
import re, ast

try: # for pip >= 10
	from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
	from pip.req import parse_requirements

# get version from __version__ variable in erpnext_conference/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('erpnext_conference/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

requirements = parse_requirements("requirements.txt", session="")

setup(
	name='erpnext_conference',
	version=version,
	description='Website and Ticketing platform for ERPNext Conference',
	author='Frappe Technologies',
	author_email='developers@frappe.io',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
#	install_requires=[str(ir.req) for ir in requirements],
#	dependency_links=[str(ir._link) for ir in requirements if ir._link]
)
