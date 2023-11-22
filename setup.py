from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="pycalendly",
    version="0.1.0",
    author="Hubert Korzeniewski",
    author_email="hubert.korzeniewski@theengineers.tech",
    description="A short description of your package",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    keywords="calendly, calendly api, calendly python, calendly python api",
    install_requires=["requests"],
    packages=["calendly"],
    url="https://github.com/hkorzeniewski/pycalendly",
)
