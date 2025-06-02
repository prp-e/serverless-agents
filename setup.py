from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='serverless-agents',
    version='0.0.2', 
    author='Muhammadreza Haghiri',
    author_email='<haghiri75@gmail.com>',
    url='https://github.com/prp-e/serverless-agents',
    license='MIT',
    description='Making AI agents with serverless architecture',
    long_description_content_type='text/markdown',
    long_description=long_description,
    packages=find_packages(),
    install_requires=['openai'],
    keywords = ['face detection', 'cv', 'computer-vision'],
    classifiers = ["Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",]
)