# wave2phasor
This package get the waveform time series data and returns harmonics phasors time series which depends on the 
pre defined window size. For any given wave form this packages uses FFT
to get the harmonic phasors in each defined window and returns a time series of phaosr 
magnitude and angle. This package is being developed mainly for power system analysis, however, any type of wave form 
can be transferred to phasor.

#Procedure
First make an instance of `WaveToHarmonics` and then use `transform` method
to get the phasors.

    wtp = WaveToHarmonics()
### Input / Output

    Output = wtp.transform(wave_data, sampling rate, reporting rate
    , base frequency, list of harmonics)
`Wave_data` is the main wavefrom data that needs to be transferred to pahsor.
`sampling rate` is the distance between each input wave data, `reporting rate`
is the final phasor reporting distance in Hz (i.e. 120, or 2 point per cycle).
'base frequency' is 60 Hz in USA, you can change it base on the system frequency.
`list of harmonics` is the list of desired harmonics such as [1, 3, 5].

`Output` is a dict that has two main keys, `mag`, `angle` which are magnitude and angle (degree)
of each phasor. Each element in Output is a dict which list of harmonics as its
keys.


# Setup
Please clone the project and in the command line within the same directory of
project use ``python setup.py sdist bdist_wheel`` to setup the project 
and use the w2p module.

# Sample data
In the `sample_data` folder there are two numpy files which include
sample wave from and their labels (event type). These events are from 
PSCAD simulation of IEEE 34 bus test system. In this project we defined 9 different
types of events in different location of the distribution network and
captured their wave form in each bus. The current sample data include 4 monitored bus
``[806, 824, 834, 846]`` which for simplicity we use ``[0, 1, 2, 3]``. This file contains 20 events
with 1000 samples for each bus voltage and current, in total, `2(V and I)*3(phases)*4(bus)=24` features.
`sample_data.size()=(20,1000,24)`.

You can access each event type from sample_labels.npy file. For sake of simplicity I 
put 20 events, however, the actual simulation has more than 35000 events.
Please contact me via my email (`aalig002 AT ucr DOT edu`) to get more events if you need for your research. 

# Updates
*Wave to phasor based on the list of harmonics, degree.
