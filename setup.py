import io
import os
import re

from setuptools import setup, find_packages

module_path = os.path.dirname(__file__)

with io.open(os.path.join(module_path, "invoice/__init__.py"), "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = \"(.*?)\"", f.read()).group(1)

# with io.open(os.path.join(module_path, "./README.rst"), "rt", encoding="utf8") as f:
#     LONG_DESCRIPTION = f.read()


setup(
    name="Invoice",
    version=version,
    project_url={},
    author="Rafael S. Müller",
    author_email="rafa.molitoris@gmail.ocm",
    description="",
    long_description_context_type="text/x-rst",
    packages=find_packages(),
)