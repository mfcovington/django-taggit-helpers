import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requires = [
    "django-taggit",
]

setup(
    name='django-taggit-helpers',
    version='0.0.0',
    packages=['taggit_helpers'],
    include_package_data=True,
    license='BSD License',
    description='Django admin helper classes for django-taggit tags',
    long_description=README,
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
