from setuptools import setup, find_packages

setup(
    name="snapshot",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "snapshot = snapshot.snapshot:main",
        ],
    },
    install_requires=[
        #   'argparse',
        'psutil'
    ],
    version="0.1",
    author="Sergey Kosolapov",
    author_email="sergey_kosolapov@epam.com",
    description="doing some snapshots",
    license="-",
)
