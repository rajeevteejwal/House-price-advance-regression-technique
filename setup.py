import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PROJECT_NAME = "Advance Regression Technique"
REPOSITORY_NAME = "House-price-advance-regression-technique"
USER_NAME = "rajeevteejwal"
setuptools.setup(
    name=f"{REPOSITORY_NAME}-{USER_NAME}",
    version="0.0.1",
    author=USER_NAME,
    author_email="rajeevteejwal@gmail.com",
    description="It's a project of predicting housing price based on 'Boston Housing Dataset.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USER_NAME}/{REPOSITORY_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{REPOSITORY_NAME}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[

    ]
)