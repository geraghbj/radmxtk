import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='radmxtk',  
     version='0.1',
     scripts=['radmxtk'] ,
     author="Benjamin Geraghty",
     author_email="geraghbj@gmail.com",
     description="A PyRadiomics utility package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/geraghbj/radmxtk",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )