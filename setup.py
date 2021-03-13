from setuptools import setup,find_packages

with open("README.md",'r') as fh:
    long_description = fh.read()
setup(
    name='darn',
    version='0.1.1',    
    description='Easy remote and local code execution',
    url='https://github.com/AmitSrourDev/darn',
    py_modulkels=["darn"],
    package_dir={'':'app'},
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Amit Srour',
    author_email='amitsrourdev@gmail.com',
    license='BSD 2-clause',
    # packages=['pyexample'],s
    # install_requires=['mpi4py>=2.0',
    #                   'numpy',                     
    #                   ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.8',
        "Topic :: Software Development",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Software Distribution",
        "Topic :: System :: Systems Administration",
    ],
    python_requires=">=3.8.5",
)
