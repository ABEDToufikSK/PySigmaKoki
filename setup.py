from setuptools import setup, find_packages

setup(
    name='PySigmaKoki',
    version='0.0.1',
    description='Control Sigma Koki Motorized Stages SHOT/Hit/FC',
    url='https://github.com/',
    author='ABED TOUFIK',
    author_email='t.abed@sigma-koki.com',
    license='MIT',
    install_requires=['pyserial'],
    packages=find_packages()
)