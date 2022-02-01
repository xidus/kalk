import os
from setuptools import (
    setup,
    find_packages,
)

with open(os.path.join('src', 'kalk', 'version.py')) as f:
    exec(f.read())


setup(
    name="kalk",
    version=__version__,
    description="Kalkulator for your sums, substractions and multiplications.",
    url="https://github.com/xidus/kalk",
    author="Joachim Mortensen",
    author_email="xidus@github.com",
    license="BSD-3",

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    # entry_points={
    #     'console_scripts': [
    #         'diveg = diveg.cli:main',
    #     ],
    # },
)
