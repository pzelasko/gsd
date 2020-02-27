from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='gsd',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    scripts=[s for s in Path('gsd/commands').glob('*') if not s.name.startswith('_')]
)
