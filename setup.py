from setuptools import setup, find_packages

setup(name="recommenders",
      version="0.0.1",
      author="ms",
      author_email="author@example.com",
      # description="A small example package",
      # long_description=long_description,
      # long_description_content_type="text/markdown",
      # url="https://github.com/pypa/sampleproject",
      # packages=setuptools.find_packages(),
      classifiers=[
          "Programming Language :: Python :: 3",
          "Operating System :: OS Independent",
      ],
      packages=find_packages(exclude=('tests', 'docs', 'build', 'dist', 'notebook')),
      package_data={
          # If any package contains *.txt or *.rst files, include them:
          '': ['*.yml', '*.yaml'],
          # And include any *.msg files found in the 'hello' package, too:
      }
    )
