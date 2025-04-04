import os
from setuptools import setup, find_packages

setup(
    name="MathAnalyzer",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["numpy", "pandas", "matplotlib"],
    author="Kağan Ünal",
    author_email="kaganunal.15@gmail.com",
    description="Matematiksel hesaplamalar ve veri analizi için bir Python kütüphanesi",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/kagan-u/MathAnalyzer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
