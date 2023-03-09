"""
    Create a python package on PyPI (need to register)

    run```
        pip install twine
        twine upload dist/*
    ```
"""
import setuptools   # Support for building and installing modules

# Open readme file in context manager
with open("README.md", 'r') as file:
    long_description = file.read()

setuptools.setup(
    name="smallgrad",
    version="1.0.0",
    author="Ramon Lins",
    author_email="rmnaslrn@gmail.com",
    description="A tiny autograd engine with a small PyTorch-like neural network library on top.",
    long_description=long_description,
    long_description_content_type="text/markdown", # Will be display on python project index
    url="https://github.com/ramon-lins/deep-learning/autograd",
    packages=setuptools.find_packages(),    # Search for all python packages in the current directory
                                            # and return a list of their names. Here as e.g: ['autograd']
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        #"Private :: Do Not Upload"
    ],
    python_requires='>=3.6'

)
