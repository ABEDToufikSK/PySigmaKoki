from setuptools import setup, find_packages

setup(
    name='SIGMA KOKI',
    version='1.0.0',
    description='Control Sigma Koki Motorized Stages',
    url='https://github.com/',
    author='ABED TOUFIK',
    author_email='t.abed@sigma-koki.com',
    license='MIT',
    install_requires=['pyserial'],
    packages=find_packages()
)