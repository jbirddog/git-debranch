from setuptools import setup, find_packages

def contents_of(filename):
    with open(filename) as f:
        return f.read()

setup(
    name = "git-debranch",
    version = "0.1.0",
    description = "Remove git branches",
    long_description = contents_of("README.md"),
    long_description_content_type = "text/markdown",

    license = "lGPLv2",
    author = "Jon Herron",
    author_email = "jon.herron@yahoo.com",

    # uncomment after spiffworkflow 2.0
    #install_requires = contents_of("requirements.txt"),
    python_requires = ">=3.9",

    package_dir = {"": "src"},
    packages = find_packages(where="src"),

    package_data = {
        "git_debranch": [
            "assets/bpmn/**/*.bpmn",
        ],
    },

    entry_points = {
        "console_scripts": ["git-debranch=git_debranch:main"],
    },
    py_modules = ["git-debranch"],
)
