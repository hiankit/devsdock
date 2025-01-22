from setuptools import setup, find_packages
import os

setup(
    name="your-package-name",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # 在这里列出您的依赖项
        # 例如：
        # "flask>=2.0.0",
        # "requests>=2.25.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A short description of your project",
    long_description=open("README.md").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/your-repo",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
) 