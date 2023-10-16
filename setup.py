from setuptools import setup, find_packages

setup(
    name='PySigmaKoki',
    version='0.0.1',
    description='Control Sigma Koki Controllers/Motorized Stages including SHOT/Hit/FC mode',
    url='https://github.com/ABEDToufikSK/PySigmaKoki.git',
    author='ABEDToufik88',
    author_email='abedtoufik.g@gmail.com',
    license='MIT',
    install_requires=['pyserial','enum','time'],
    packages=find_packages(),
    python_requires='>=3.2',  #  Python versions supported
    packages=find_packages()
)
