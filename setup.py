from setuptools import setup, find_packages

setup(
    name='PySigmaKoki',
    version='0.0.1',
    description='Control Sigma Koki Controllers/Motorized Stages including SHOT/Hit/FC mode',
    url='https://github.com/ABEDToufikSK/SK_PySigmaKoki.git',
    author='ABED TOUFIK',
    author_email='t.abed@sigma-koki.com''abedtoufik.g@gmail.com',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    install_requires=['pyserial','enum','time'],
    packages=find_packages(),
    python_requires='>=3.2',  #  Python versions supported
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)