from time import time
import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name="semi-tensor-product",
    version="0.0.4",
    author="Huanianss",
    author_email="huanianss@qq.com",
    description="STP Toolbox for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/huanianss/semi-tensor-product",
    project_urls={
        "Bug Tracker": "https://github.com/huanianss/semi-tensor-product/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    )