from setuptools import setup, find_packages

setup(
    name='html_table_transformer',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'lxml',
        'pandas',
        'numpy'
    ],
    description="HtmlTableTransformer is a library to parse tables of different schemas under html and convert them into machine comprehensible format for LLMs ingestions or jupyter notebook data implementations.",
    author='Quectonic',
    author_email='wycheng@quectonic.com',
    license='MIT',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
)