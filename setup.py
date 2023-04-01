from setuptools import setup, find_packages

setup(
    name="pyquotegen",
    version="0.0.1",
    author="Arman Idrisi",
    author_email="idrisiarman19@gmail.com",
    description="A Random Quote Generator Python Package",
    long_description="This Is A package which can ve used for generating the random quotes in diffrent categories for example: motivation, technology etc.",


    url="https://github.com/Armanidrisi/pyquotegen",
    project_urls={
        "Bug Tracker": "https://github.com/Armanidrisi/pyquotegen/issues",
        "Documentation": "https://github.com/Armanidrisi/pyquotegen/blob/main/README.md",
        "Source Code": "https://github.com/Armanidrisi/pyquotegen",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.0",
)
