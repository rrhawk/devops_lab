from setuptools import setup, find_packages

setup(
    name="snapshot",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "main = snapshot.snapshot:main",
        ],
    },
    install_requires=[
    ],
    version="0.1",
    author="Sergey Kosolapov",
    author_email="sergey_kosolapov@epam.com",
    description="doing some snapshots",
    license="-",
)
