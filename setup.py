import setuptools

with open("README.md" , "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "TextSummarizer" #name of repo at github.com
AUTHOR_USER_NAME = "tajallshafqat"
SRC_REPO = "TextSummarizer"  #name of source repo on your computer
AUTHOR_EMAIL = "tajallshafqat@gmail.com"
 

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for nlp app named text summarizer.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    projects_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
        "Source Code": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    },
    package_dir={"" : "src"},
    packages=setuptools.find_packages(where="src")
)