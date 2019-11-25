from setuptools import setup, find_packages

setup(
    name='radionets',
    version='0.0.1',
    description='Imaging radio interferometric data with neural networks',
    url='https://github.com/Kevin2/radionets',
    author='Kevin Schmidt, Felix Geyer',
    author_email='kevin3.schmidt@tu-dortmund.de, felix.geyer@tu-dortmund.de',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'torch==1.3.1',
        'torchvision==0.4.2',
        'numpy==1.17.3',
        'astropy==3.2.3',
        'tqdm==4.36.1',
        'click==7.0',
        'geos',
        'shapely==1.6.4',
        'proj',
        'cartopy==0.17.0',
        'ipython==7.9.0',
        'jupyter==1.0.0',
        'jupytext==1.2.4',
        'obspy==1.1.1',
        'h5py==2.9.0',
        'scikit-image==0.16.2',
        'pandas==0.25.3'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    zip_safe=False,
    classifiers=[
         'Development Status :: 2 - Pre-Alpha',
         'Intended Audience :: Science/Research',
         'License :: OSI Approved :: MIT License',
         'Natural Language :: English',
         'Operating System :: OS Independent',
         'Programming Language :: Python',
         'Programming Language :: Python :: 3.7',
         'Programming Language :: Python :: 3 :: Only',
         'Topic :: Scientific/Engineering :: Astronomy',
         'Topic :: Scientific/Engineering :: Physics',
    ],
)
