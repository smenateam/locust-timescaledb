from setuptools import setup, find_packages

__version__ = '0.0.1'

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='locust-timescaledb',
    version=__version__,
    url='https://github.com/smenateam/locust-timescaledb',
    license='Apache-2.0',
    author='SMENA',
    author_email='smenateam@smena.space',
    description='Report locust metrics to timescaledb.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    package_data={'': ['LICENSE', 'README.md']},
    package_dir={'locust-timescaledb': 'locust-timescaledb'},
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[
        'locustio>=0.13.5',
        'psycopg2>=2.8.4',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    project_urls={
        'Source': 'https://github.com/smenateam/locust-timescaledb',
    },
)
