from setuptools import setup
from setuptools import find_packages

setup(name='gravity_fastgae',
      description='Gravity + FastGAE',
      author='Floyd, based on two of Deezers Research',
      install_requires=['networkx==2.2',
                        'numpy',
                        'scikit-learn',
                        'scipy',
                        'tensorflow==1.*'],
      package_data={'gravity_fastgae': ['README.md']},
      packages=find_packages())