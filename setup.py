from setuptools import setup, find_namespace_packages

with open('README.md', 'r', encoding='utf-8') as readme:
    long_description = readme.read()


setup(
    name='clean',
    version='1.0.0',
    description='The script sorts files into folders',
    long_description=long_description,
    url='https://github.com/YevhenKoss/goit-python/tree/main/clean_folder',
    author='Yevhen',
    author_email='kossik89@gmail.com',
    classifiers=[
        'Python version :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Windows'
    ],
    packages=find_namespace_packages(),
    python_requires='>=3.8',
    entry_points={'console_scripts': ['clean = clean_folder.clean:main']}
)