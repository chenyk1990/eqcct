import os
import pathlib 

def get_sta_loc(staname,stafile=None):
	"""
	get_sta_loc: get lon,lat for a TexNet station
	
	Input
	staname: str or list
	
	Output
	tuple (lon,lat) or a list of tuples (lonlats)
	
	Example 1:
	from eqcct.texnet import get_sta_loc
	(lon,lat)=get_sta_loc('TX.PB07')
	
	Example 2:
	from eqcct.texnet import get_sta_loc
	lonlats=get_sta_loc(['TX.PB07','TX.ALPN'])
	
	Example 3:
	from eqcct.texnet import get_sta_loc
	import matplotlib.pyplot as plt
	stas=['TX.SN08','TX.SN09','TX.SN02','TX.SN03','TX.SN04','TX.MB09','TX.MB10','TX.MB05','TX.POST','TX.SGCY']
	lonlats=get_sta_loc(stas)
	for ii in lonlats:
		plt.plot(float(ii[0]),float(ii[1]),'v',color='r',markersize=15)
	for ii in range(len(stas)):
		plt.text(float(lonlats[ii][0]),float(lonlats[ii][1]),stas[ii],color='r')
	plt.plot(-102.0779,31.9973,'*b',markersize=12);
	plt.text(-102.0779,31.9973,'Midland',color='b',fontsize=14)
	plt.show()
	
	"""
	if stafile is None:
		stafile=os.getenv('HOME')+'/chenyk.data2/various/cyksmall/texnet_stations_2024_0209.csv'
	p = pathlib.Path(stafile)
	stnames = [line.strip().split(',')[0]+'.'+line.strip().split(',')[1] for line in p.read_text().strip().split('\n')[1:]]
	stlons = [line.strip().split(',')[2] for line in p.read_text().strip().split('\n')[1:]]
	stlats = [line.strip().split(',')[3] for line in p.read_text().strip().split('\n')[1:]]
	
	if type(staname) == str:
		i=stnames.index(staname)
		return (stlons[i],stlats[i])
	elif type(staname) == list:
		lonlats=[];
		for ista in range(len(staname)):
			i=stnames.index(staname[ista])
			lonlats.append((stlons[i],stlats[i]))
		return lonlats
		
	else:
		print('Wrong input parameter for get_sta_loc');
		
def get_sta_time(staname,stafile=None):
	"""
	get_sta_time: get start date for a TexNet station (e.g., 9/28/02)
	
	Input
	staname: str or list
	
	Output
	str (utc time) or a list of str (times)
	
	Example 1:
	from eqcct.texnet import get_sta_time
	time=get_sta_time('TX.PB07')

	Example 2:
	from eqcct.texnet import get_sta_time
	times=get_sta_time(['TX.PB08','US.CBKS'])
	"""
	import obspy.core.utcdatetime as utc
	
	if stafile is None:
		stafile=os.getenv('HOME')+'/chenyk.data2/various/cyksmall/texnet_stations_2024_0209_extra.csv'
	p = pathlib.Path(stafile)
	stnames = [line.strip().split(',')[0]+'.'+line.strip().split(',')[1] for line in p.read_text().strip().split('\n')[1:]]
	timestrs = [line.strip().split(',')[-2] for line in p.read_text().strip().split('\n')[1:]]
	
	timesutc=[]
	for ii in range(len(stnames)):
		if "/" in timestrs[ii]:
			year=timestrs[ii].split('/')[-1]
			if int(year)>90:
				year=int('19'+year);
			else:
				year=int('20'+year);
			month=int(timestrs[ii].split('/')[0])
			day=int(timestrs[ii].split('/')[-2])
		elif "-" in timestrs[ii]:
			year=int(timestrs[ii].split('-')[0])
			month=int(timestrs[ii].split('-')[1])
			day=int(timestrs[ii].split('-')[2])
		else:
			TypeError("Date format error")
				
		timesutc.append(utc.UTCDateTime(year, month, day, 00, 00, 00, 000000)+86400) #suppose fully functional the next day
		
	if type(staname) == str:
		i=stnames.index(staname)
		return timesutc[i]
	elif type(staname) == list:
		times=[];
		for ista in range(len(staname)):
			i=stnames.index(staname[ista])
			times.append(timesutc[i])
		return times
		
	else:
		print('Wrong input parameter for get_sta_time');
			 

