from setuptools import setup, find_packages

def contents_of(filename):
    with open(filename) as f:
        return f.read()

setup(
    name = "git-debranch",
    version = contents_of("VERSION"),
    description = "Remove git branches",
    long_description = contents_of("README.md"),
    long_description_content_type = "text/markdown",

    license = "lGPLv2",
    author = "Jon Herron",
    author_email = "jon.herron@yahoo.com",

    install_requires = contents_of("requirements.txt"),
    python_requires = ">=3.9",

    package_dir = {"": "src"},
    packages = find_packages(where="src"),

    package_data = {
        "git_debranch": [
            "bpmn/**/*.bpmn",
            "bpmn/**/*.json",
        ],
    },

    entry_points = {
        "console_scripts": ["git-debranch=git_debranch.console_scripts:main"],
    },
    py_modules = ["git-debranch"],

    package_urls = {
        "GitHub": "https://github.com/jbirddog/git-debranch",
        "CHANGELOG": "https://github.com/jbirddog/git-debranch/blob/main/CHANGELOG.md",
    },
)
