from setuptools import setup, find_packages

setup(
    name="payment_processor",
    version="1.0.0",
    packages=find_packages(include=["src", "src.*"]),
    install_requires=[],
    author="Wiktor",
    author_email="wiktor.tokarski@edu.uekat.pl",
    description="Python package for payment processing",
    url="https://github.com/boltzful/Dobre-Praktyki-Programowania",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
