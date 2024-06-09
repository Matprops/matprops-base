from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name='matprops-base',
    version='1.0.0',
    packages=find_packages(where="resources"),
    package_dir={'': 'resources'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    keywords="Support files for matprops",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "numpy >= 1.22.0",
        "pandas >= 1.3.5",
        "matplotlib >= 3.5.1"
    ],
    extras_require={
        "dev": [
            "pytest >= 6.2.5"
        ]
    },
    url='https://github.com/Matprops/matprops-base',
    author='Mohammed Shammeer',
    author_email='mohammedshammeer.s@gmail.com',
    description='Python library written on top of matplotlib library for customizable charts'
)
