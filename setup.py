from setuptools import setup, find_packages

setup(
    name='SigmaKokiPy',
    version='0.0.3',
    description='Control Sigma Koki Controllers/Motorized Stages including SHOT/Hit/FC mode',
    url='https://github.com/ABEDToufikSK/SigmaKokiPy.git',
    author='ABED Toufik',
    author_email='abedtoufik.g@gmail.com',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    install_requires=['pyserial'],
    python_requires='>=3.2',  #  Python versions supported
    packages=find_packages()
)
