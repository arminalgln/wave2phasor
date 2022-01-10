import numpy as np
from scipy.fft import fft, fftfreq, fftn
import pandas as pd
import matplotlib.pyplot as plt

class WaveToHarmonics:
    """
    initiate an instant to transform the wave form to its harmonics phasor with defined reporting rate
    """
    def __init__(self):
        super(WaveToHarmonics, self).__init__()


    def transform(self, data, sampling_rate, reporting_rate, base_freq, harmonics):
        """

        :param data: wave form data, numpy array (event_num, wave_timesteps, features_num)
        :param sampling_rate: time difference between each sample in sec
        :param reporting_rate: transformed phasor reporting rate such as 120 (per second)
        :param harmonics: a list of harmonics, such as [1, 3, 5]
        :param base_freq: it shows the main frequency of the system
        :return: harmonics phasor of each event (event_num, phasor_timesteps, features_num)
        """

        reporting_rate = reporting_rate #normally 60 or 120HZ, or 2 readings per cycle

        event_num, sample_num, features_num = data.shape

        N = sample_num #predefine the window size for fft
        #find the minimum sample # to have the basic freq in the fft freq
        freq_coeff = 1
        indic = True
        while indic:
            if np.ceil(freq_coeff / (sampling_rate * base_freq)) == int(freq_coeff/ (sampling_rate * base_freq)):
                N = int(freq_coeff / (sampling_rate * base_freq))
                indic = False
            else:
                freq_coeff += 1

        #samples per cycle
        sample_per_cycle_num = int(1/base_freq/sampling_rate)
        window_shift = int(sample_per_cycle_num/(reporting_rate/base_freq))
        phasor_sample_num = int((sample_num - N)/window_shift)

        har_freqs = fftfreq(N, sampling_rate)[:N // 2]
        selected_harmonics = [base_freq*i for i in harmonics]
        har_indexes = [list(har_freqs).index(i) for i in selected_harmonics]
        print(har_indexes,selected_harmonics)
        all_harmonics_data = {'mag' : {}, 'angle' : {}}
        for h in harmonics:
            for k in all_harmonics_data:
                all_harmonics_data[k][h] = np.zeros((event_num, phasor_sample_num, features_num))

        # print(N,har_indexes, sample_per_cycle_num,window_shift,phasor_sample_num)
        for ev in range(event_num):
            start = 0
            end = N
            print(ev)
            for sh in range(phasor_sample_num):
                y = data[ev][start:end, :]
                yf = fftn(y, axes=(0))
                # print(yf.shape)
                # print(start, end)
                phasor_mags_temp = (np.abs(yf[har_indexes, :]) * np.sqrt(2) / N).reshape(len(har_indexes), 1,
                                                                                         features_num)
                phasor_angles_temp = (np.angle(yf[har_indexes, :]) * 180 / (np.pi)).reshape(len(har_indexes), 1,
                                                                                           features_num)
                if sh == 0:
                    phasor_mags = np.copy(phasor_mags_temp)
                    phasor_angles = np.copy(phasor_angles_temp)
                else:
                    phasor_mags = np.concatenate((phasor_mags, phasor_mags_temp),axis=1)
                    phasor_angles= np.concatenate((phasor_angles, phasor_angles_temp),axis=1)

                start += window_shift
                end += window_shift
            for idx, h in enumerate(harmonics):
                all_harmonics_data['mag'][h][ev] = phasor_mags[idx]
                all_harmonics_data['angle'][h][ev] = phasor_angles[idx]

        return all_harmonics_data