
from setuptools import find_packages, setup

setup(
    name='retail_access_man',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    url='https://tjdai@bitbucket.org/retail_in_future/retail_access_man.git',
    license='',
    author='tjdai',
    author_email='tjdai@thoughtworks.com',
    description='qrcode server',
    install_requires=[
        'pyyaml',
        'nose'
    ],
)
