import os
import netCDF4 as nc
import numpy as np
import matplotlib as plt

prefix1 = '../TRR_Data/north/'
prefix2 = '../TRR_Data/east/'
suffix = '.nc'
lat = 8 #from 31 to 38
lon = 15 #from 89 to 103

data = list()

for i in range(lat):
	temp = list()
	for j in range(lon):
		temp.append([])
	data.append(temp)

def analyze_total(ncobj):
	time = len(ncobj)
	for i in range(time):
		for j in range(lat):
			for k in range(lon):
				data[j][k].append(ncobj[i][j][k])
		


def analyze_sep(ncobj):	
	print(len(ncobj))


for i in range(1979, 2018):
	if i == 2017 or i == 2010:
		#ncobj = []
		for j in range(1, 13):
			name = prefix1 + '2010&2017/'
			if j < 10:
				name += str(i) + '.0' + str(j) + suffix
			else:
				name += str(i) + '.' + str(j) + suffix
			ncobj = nc.Dataset(name)

		continue
	name = prefix1 + str(i) + suffix
	ncobj = nc.Dataset(name)
	analyze_total(ncobj.variables['p72.162'][:])

#ncobj = nc.Dataset(prefix1+'1979'+suffix)
#print(ncobj.variables['longitude'][:])
#print(ncobj.variables['latitude'][:])
#print(ncobj.variables['time'][:])
#print(ncobj.variables['p72.162'][:])

