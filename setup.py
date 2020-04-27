import setuptools

#https://python-packaging-tutorial.readthedocs.io/en/latest/setup_py.html
setuptools.setup(
    name="pajamas",  
    version="0.1a0",
    author="Armand Niederberger",
    author_email="pajamas@armandniederberger.com",
    packages=["pajamas"],
    scripts=["bin/pajamas2ipynb", "bin/ipynb2pajamas"],
    url="https://github.com/barceloco/pajamas",
    license="LICENSE",
    description="Package to stip jupyter notebooks of their output and dress back up from these pajamas.",
    long_description=open('README.md').read(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
# Run:
# python setup.py sdist
# python setup.py bdist_wheel
# python -m pip install .
# if it works, upload to pip via: python -m twine upload dist/*
# all-in-one:
#   python setup.py sdist && python setup.py bdist_wheel && python -m twine upload dist/*

# https://dzone.com/articles/executable-package-pip-install
# with open("README.md", "r") as fh:
#     long_description = fh.read()
# setuptools.setup(
#      name='pajamas',  
#      version='0.1a',
#      scripts=['pajamas'] ,
#      author="Armand Niederberger",
#      author_email="pajamas@armandniederberger.com",
#      description="Package to convert jupyter notebooks to the a file without the output (smaller files for committing to repos) and back.",
#      long_description=long_description,
#    long_description_content_type="text/markdown",
#      url="https://github.com/barceloco/pajamas",
#      packages=setuptools.find_packages(),
#      classifiers=[
#          "Programming Language :: Python :: 3",
#          "License :: BSD-3 License",
#          "Operating System :: OS Independent",
#      ],
#  )