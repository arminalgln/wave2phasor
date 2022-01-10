from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Wave form to harmonics phasors'
LONG_DESCRIPTION = 'This package get the waveform time series data and returns harmonics phasors time series which' \
                   ' depends on the pre defined window size.'

# Setting up
setup(
    # the name must match the folder name 'w2p'
    name="w2p",
    version=VERSION,
    author="Armin Aligholian",
    author_email="aalig002@ucr.edu",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        'setuptools',
        'markdown',
        'numpy',
        'pandas',
        'matplotlib',
        #'sklearn',
    ],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'wave form', 'harmonics', 'phasor'],
    zip_safe=False
)