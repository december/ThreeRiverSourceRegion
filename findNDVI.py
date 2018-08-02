import os
import netCDF4 as nc
import numpy as np
import matplotlib as plt
import sklearn

prefix = 'E:\\NDVI&RAIN\\GIMMS_NDVI3g\\V1\\20170903_2327\\'
suffix = '.nc4'
filename = os.listdir(prefix)
for name in filename:
	if name.endswith('.nc4'):
		ncobj = nc.Dataset(prefix+name)

#ncobj = nc.Dataset(prefix+'ndvi3g_geo_v1_2012_0106'+suffix)

print(ncobj.variables.keys())
#print(ncobj.variables['time'][:])
#print(ncobj.variables['satellites'][:])
print(ncobj.variables['lat'][:12])
print(ncobj.variables['ndvi'].shape) # 12(time) * 2160
