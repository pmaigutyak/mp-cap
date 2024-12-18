
from setuptools import setup, find_packages


version = '4.0.2'
url = 'https://github.com/pmaigutyak/mp-cap'


setup(
    name='django-mp-cap',
    version=version,
    description='Django admin app',
    author='Paul Maigutyak',
    author_email='pmaigutyak@gmail.com',
    url=url,
    download_url='{}/archive/{}.tar.gz'.format(url, version),
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
)
