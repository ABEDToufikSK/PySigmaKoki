from setuptools import setup, find_packages

setup(
    name='SigmaKokiPy',
    version='0.0.1',
    description='Control Sigma Koki Controllers/Motorized Stages including SHOT/Hit/FC mode',
    url='https://github.com/ABEDToufikSK/SigmaKokiPy.git',
    author='ABED Toufik',
    author_email='abedtoufik.g@gmail.com',
    license='MIT',
    install_requires=['pyserial','enum','time'],
    python_requires='>=3.2',  #  Python versions supported
    packages=find_packages()
)
