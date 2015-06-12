import os
import sys
from setuptools import setup

if sys.version_info < (3, 2):
    print("Sorry, django-taggit-helpers currently requires Python 3.2+.")
    sys.exit(1)

# From: https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requires = [
    'django>=1.7,<1.8',
    'django-taggit>=0.12.0',
]

setup(
    name='django-taggit-helpers',
    version='0.1.1',
    packages=['taggit_helpers'],
    include_package_data=True,
    license='BSD License',
    keywords='tags tagging taggit django-taggit',
    description='Django admin helper classes for django-taggit tags',
    long_description=(read('README.rst') + '\n\n' +
                      read('CHANGELOG.rst')),
    url='https://github.com/mfcovington/django-taggit-helpers',
    author='Michael F. Covington',
    author_email='mfcovington@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3 :: Only',
    ],
    install_requires=install_requires,
)
