from setuptools import setup, find_packages

setup(name='goit_homework_7',
      version='1',
      description='Example package',
      author='Mykhailo Iereshchenko',
      url='https://github.com/m1hanch',
      license='MIT',
      packages=find_packages(),
      entry_points={'console_scripts':'hw7 = clean_folder.clean:sorting'})