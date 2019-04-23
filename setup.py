from setuptools import setup
import os
import io

with io.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='fuzzy_matcher',
    version='0.1.0',
    author='Nathan Zylbersztejn',
    description="A super simple MIT licensed fuzzy matching library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['editdistance', ],
    licence='MIT',
    url='https://mrbot.ai',
    author_email='human@mrbot.ai',
    packages=['fuzzy_matcher']
)
