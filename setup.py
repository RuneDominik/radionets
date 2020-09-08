from setuptools import setup, find_packages

setup(
    name="radionets",
    version="0.1.0",
    description="Imaging radio interferometric data with neural networks",
    url="https://github.com/Kevin2/radionets",
    author="Kevin Schmidt, Felix Geyer, Kevin Laudamus",
    author_email="kevin3.schmidt@tu-dortmund.de",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "torch==1.5",
        "torchvision==0.6",
        "numpy==1.17.3",
        "astropy==3.2.3",
        "tqdm==4.36.1",
        "click==7.1.2",
        "geos",
        "shapely==1.6.4",
        "proj",
        "cartopy==0.17.0",
        "ipython==7.9.0",
        "jupyter==1.0.0",
        "jupytext==1.2.4",
        "h5py==2.9.0",
        "scikit-image==0.16.2",
        "pandas==0.25.3",
        "requests",
        "toml",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "radionets_simulations = simulations.scripts.simulate_images:main",
            "radionets_training = dl_training.scripts.start_training:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
)
