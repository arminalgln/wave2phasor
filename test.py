import numpy as np
import matplotlib.pyplot as plt
from w2p import WaveToHarmonics
import pickle

with open('sample_data/features.pickle', 'rb') as handle:
    features = pickle.load(handle)
data = np.load('sample_data/sample_wave' + '.npy')
labels = np.load('sample_data/sample_labels' + '.npy')

wtp = WaveToHarmonics()
all_h = wtp.transform(data, 0.001, 120, 60, [1, 3, 5])

#%%
ev = 2
har = 1
pmu = 0
fig, (fig1, fig2, fig3) = plt.subplots(3, 1)	# subplots(row, columns)


fig1.plot(all_h['mag'][har][ev][:,0+ 6*pmu])
fig1.plot(all_h['mag'][har][ev][:,1+ 6*pmu])
fig1.plot(all_h['mag'][har][ev][:,2+ 6*pmu])
fig1.set_ylabel('Voltage magnitude')

fig2.plot(all_h['mag'][har][ev][:,3+ 6*pmu])
fig2.plot(all_h['mag'][har][ev][:,4+ 6*pmu])
fig2.plot(all_h['mag'][har][ev][:,5+ 6*pmu])
fig2.set_ylabel('Current magnitude')

fig3.plot(np.cos(np.radians(all_h['angle'][har][ev][:,0+ 6*pmu] - all_h['angle'][har][ev][:,3+ 6*pmu])))
fig3.plot(np.cos(np.radians(all_h['angle'][har][ev][:,1+ 6*pmu] - all_h['angle'][har][ev][:,4+ 6*pmu])))
fig3.plot(np.cos(np.radians(all_h['angle'][har][ev][:,2+ 6*pmu] - all_h['angle'][har][ev][:,5+ 6*pmu])))

fig2.set_ylabel('')



fig1.set_title('phasor harmonic for event #{}, pmu #{} and harmonic #{}'.format(ev,pmu,har))
plt.show()
