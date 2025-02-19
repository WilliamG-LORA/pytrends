import io
import os

from setuptools import setup

dir = os.path.dirname(__file__)

with io.open(os.path.join(dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pytrends',
    version='4.7.5',
    description='Pseudo API for Google Trends. This is a fork that uses ScraperAPI',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/WilliamG-LORA/pytrends.git',
    author=['John Hogue', 'Burton DeWilde', 'William Gazeley'],
    author_email='william.gazeley@loratechai.com',
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License'
    ],
    install_requires=['requests>=2.0', 'pandas>=0.25', 'lxml'],
    keywords='google trends api search',
    packages=['pytrends'],
)
