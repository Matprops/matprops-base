from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name='matprops-base',
    version='1.0.2',
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
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
    url='https://github.com/Matprops/matprops-base',
    author='Mohammed Shammeer',
    author_email='mohammedshammeer.s@gmail.com',
    description='Python library written on top of matplotlib library for customizable charts'
)
