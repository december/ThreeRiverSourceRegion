import os
import netCDF4 as nc
import matplotlib as plt

prefix1 = '../TRR_Data/north/'
prefix2 = '../TRR_Data/east/'
suffix = '.nc'

ncobj = nc.Dataset(prefix1+'1979'+suffix)
print(ncobj.variables['longitude'][:])
print(ncobj.variables['latitude'][:])
