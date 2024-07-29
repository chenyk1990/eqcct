## Example for applying scalodeep to a random input data




import obspy.core.utcdatetime as utc
from obspy.clients.fdsn import Client
from eqcct.stream import *
import numpy as np


## download data
# cl=Client('http://rtserve.beg.utexas.edu')
# st = cl.get_waveforms('TX', 'ALPN', '00', '*', utc.UTCDateTime(2022, 12, 16, 23, 35, 27, 000000), utc.UTCDateTime(2022, 12, 16, 23, 37, 27, 000000))
# st = cl.get_waveforms('TX', 'MB07', '00', '*', utc.UTCDateTime(2022, 12, 16, 23, 33, 27, 000000), utc.UTCDateTime(2022, 12, 16, 23, 37, 27, 000000))
# st[0].data=st[0].data/100;
# st[1].data=st[1].data/100;
# st[2].data=st[2].data/100;
# st.plot()


cl=Client('http://rtserve.beg.utexas.edu')
st = cl.get_waveforms('TX', 'ALPN', '00', '*', utc.UTCDateTime(2022, 12, 16, 23, 35, 27, 000000), utc.UTCDateTime(2022, 12, 16, 23, 37, 27, 000000))



from pylib.plot.waveforms import plot_traces
#plot_traces(st,axoff=1,titleoff=1);


# from pylib.pickers import eqcct
import os


mseed_predictor(input_modelP=r'/Users/chenyk/chenyk.data2/various/cyksmall/EQCCTPS/ModelPS/test_trainer_024.h5',
         input_modelS=r'/Users/chenyk/chenyk.data2/various/cyksmall/EQCCTPS/ModelPS/test_trainer_021.h5',
         stinput = st,
         output_dir='detections_ALPN',
         P_threshold=0.1,
         S_threshold=0.1, 
         number_of_plots=10,
         normalization_mode='std',
         batch_size=1,
         overlap=0.8,
         gpuid=None,
         gpu_limit=None) 

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data = pd.read_csv('detections_ALPN/ALPN_outputs/X_prediction_results.csv', low_memory=False)
data.p_arrival_time

pat=[ii for ii in list(data.p_arrival_time) if type(ii) is str]; #P arrival time
sat=[ii for ii in list(data.s_arrival_time) if type(ii) is str]; #S arrival time

import obspy
plot_traces(st,axoff=1,titleoff=1,ptime= [obspy.UTCDateTime(pat[0]),obspy.UTCDateTime(pat[0]),obspy.UTCDateTime(pat[0])],stime=[obspy.UTCDateTime(sat[0]),obspy.UTCDateTime(sat[0]),obspy.UTCDateTime(sat[0])],figname='test_eqcct.png',dpi=500);


# ## another station
# cl=Client('http://rtserve.beg.utexas.edu')
# st = cl.get_waveforms('TX', 'MB07', '00', '*', utc.UTCDateTime(2022, 12, 16, 23, 33, 27, 000000), utc.UTCDateTime(2022, 12, 16, 23, 37, 27, 000000))
# 
# 
# from pylib.plot.waveforms import plot_traces
# #plot_traces(st,axoff=1,titleoff=1);
# 
# 
# from pylib.pickers import eqcct
# import os
# 
# 
# eqcct.mseed_predictor(input_modelP=r'/Users/chenyk/chenyk.data2/various/cyksmall/EQCCTPS/ModelPS/test_trainer_024.h5',
#          input_modelS=r'/Users/chenyk/chenyk.data2/various/cyksmall/EQCCTPS/ModelPS/test_trainer_021.h5',
#          stinput = st,
#          output_dir='detections_MB07',
#          P_threshold=0.1,
#          S_threshold=0.1, 
#          number_of_plots=10,
#          normalization_mode='std',
#          batch_size=1,
#          overlap=0.8,
#          gpuid=None,
#          gpu_limit=None) 
# 
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# data = pd.read_csv('detections_MB07/MB07_outputs/X_prediction_results.csv', low_memory=False)
# data.p_arrival_time
# 
# pat=[ii for ii in list(data.p_arrival_time) if type(ii) is str]; #P arrival time
# sat=[ii for ii in list(data.s_arrival_time) if type(ii) is str]; #S arrival time
# 
# import obspy
# plot_traces(st,axoff=1,titleoff=1,ptime= [obspy.UTCDateTime(pat[0]),obspy.UTCDateTime(pat[0]),obspy.UTCDateTime(pat[0])],stime=[obspy.UTCDateTime(sat[0]),obspy.UTCDateTime(sat[0]),obspy.UTCDateTime(sat[0])],figname='test_eqcct.png',dpi=500);
# 
# 
