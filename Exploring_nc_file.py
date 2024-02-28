# This Python script utilizes the netCDF4 library to read and visualize data from NetCDF files. 
# Specifically, it focuses on plotting time-averaged maps of daily accumulated precipitation using the Basemap library. You may adjust accordingly.


###########################################################################################################


# Import necessary libraries
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


# Read data from the first NetCDF file
data1 = Dataset(r'path\to\file\file.nc')

# Display information about the dataset
print(data1)
print(data1.variables)
print(data1.variables.keys())

# Extract latitude, longitude, and precipitation data
lats1 = data1.variables['lat'][:]
lons1 = data1.variables['lon'][:]
ppt1 = data1.variables['precipitation'][:]

# Create a Basemap instance for the first dataset
mp1 = Basemap(projection='merc',
              llcrnrlon=64.556213,
              llcrnrlat=6.9598416,
              urcrnrlon=83.7786865,
              urcrnrlat=20.2731594,
              resolution='i')

# Create a meshgrid for plotting
lon1, lat1 = np.meshgrid(lons1, lats1)
x1, y1 = mp1(lon1, lat1)

# Plot the precipitation data on the map
c_scheme1 = mp1.pcolor(x1, y1, ppt1, cmap='jet')
mp1.drawcoastlines()
mp1.drawstates()
mp1.drawcountries()

# Add colorbar and display the plot
cbar1 = mp1.colorbar(c_scheme1)
plt.show()

# Read data from the second NetCDF file
data2 = Dataset(r'E:\study material\9\g4.timeAvgMap.GPM_3IMERGHH_06_precipitationCal.20000601-20010601.180W_90S_180E_90N.nc')

# Display information about the second dataset
print(data2.variables.keys())

# Extract latitude, longitude, and precipitation data
lats2 = data2.variables['lat'][:]
lons2 = data2.variables['lon'][:]
ppt2 = data2.variables['GPM_3IMERGHH_06_precipitationCal'][:]

# Create a Basemap instance for the second dataset
mp2 = Basemap(projection='merc',
              llcrnrlon=42.8,
              llcrnrlat=-2,
              urcrnrlon=105.32,
              urcrnrlat=38.78,
              resolution='i')

# Create a meshgrid for plotting
lon2, lat2 = np.meshgrid(lons2, lats2)
x2, y2 = mp2(lon2, lat2)

# Plot the precipitation data on the map
c_scheme2 = mp2.pcolor(x2, y2, ppt2, cmap='jet')
mp2.drawcoastlines()
mp2.drawstates()
mp2.drawcountries()

# Add colorbar and display the plot with a title
cbar2 = mp2.colorbar(c_scheme2)
plt.title('Time Averaged Map of Daily accumulated precipitation (combined microwave-IR) estimate - Final Run daily 0')
plt.show()
