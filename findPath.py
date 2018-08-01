import os
import netCDF4 as nc
import numpy as np
import matplotlib as plt

prefix1 = '../TRR_Data/north/'
prefix2 = '../TRR_Data/east/'
suffix = '.nc'

data = list()

for i in range(8):
	temp = list()
	for j in range(15):
		temp.append([])
	data.append(temp)

def analyze(ncobj):


for i in range(1979, 2018):
	if i == 2017 or i == 2010:
		name = prefix1 + '2010&2017/'
		ncobj = []
		for j in range(1, 13):
			if j < 10:
				name += str(i) + '.0' + str(j) + suffix
			else:
				name += str(i) + '.' + str(j) + suffix
			ncobj.extend(nc.Dataset(name))

		continue
	name = prefix1 + str(i) + suffix
	ncobj = nc.Dataset(name)

ncobj = nc.Dataset(prefix1+'1979'+suffix)
print(ncobj.variables['longitude'][:])
print(ncobj.variables['latitude'][:])
