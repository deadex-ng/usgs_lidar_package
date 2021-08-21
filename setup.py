from setuptools import setup

setup(
    name='py3deppack',
    version='0.1.0',    
    description='A USGS Python package',
    url='https://github.com/deadex-ng/usgs_lidar_package',
    author='Fumbani Banda',
    author_email='thisisfumba@outlook.com',
    license='BSD 2-clause',
    packages=['py3deppack'],
    install_requires=[
                      'numpy',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)