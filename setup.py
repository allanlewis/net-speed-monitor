"""Configuration for setuptools."""
import setuptools

with open("README.md") as readme_file:
    readme = readme_file.read()

setuptools.setup(
    name="net-speed-monitor",
    version="0.1.4",
    author="Allan Lewis",
    author_email="allanlewis99@gmail.com",
    description="A tool for monitoring Internet connection speed",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/allanlewis/net-speed-monitor",
    packages=setuptools.find_packages(),
    py_modules=['net_speed_monitor'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'bitmath == 1.3.*',
        'click == 7.*',
        'humanize == 2.*',
        'python-dateutil == 2.*',
        'tabulate == 0.8.*',
    ],
    entry_points={
        "console_scripts": [
            "net-speed-monitor = net_speed_monitor:main",
        ],
    },
)
