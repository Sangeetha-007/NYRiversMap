import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
import os
import geodatasets as gd

rivers = gpd.read_file("/Users/sangeetha/Downloads/HydroRIVERS_v10_na_shp/HydroRIVERS_v10_na_shp/HydroRIVERS_v10_na.shp")

# Load a dataset for New York State boundary for context (using Natural Earth for simplicity)


us_states = gpd.read_file("/Users/sangeetha/Downloads/cb_2018_us_state_20m/cb_2018_us_state_20m.shp") 
ny_state = us_states[us_states['NAME'] == "New York"]
print(ny_state)
#print(us_states)


# Ensure both datasets have the same CRS
ny_state = ny_state.to_crs(epsg=3857)  # Web Mercator projection
rivers = rivers.to_crs(epsg=3857)
'''

us_states = us_states.to_crs(epsg=3857)  # Web Mercator projection
rivers = rivers.to_crs(epsg=3857)
'''
# Filter rivers that intersect with New York state
ny_rivers = rivers[rivers.intersects(ny_state.geometry.values[0])]
#us_rivers = rivers[rivers.intersects(us_states.geometry.values[0])]

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 10))

# Set the background color to white
ax.set_facecolor('white')  # Set background to white

# Plot New York State
ny_state.plot(ax=ax, color="none", edgecolor="black", linewidth=2)  # Make the state border thicker
#us_states.plot(ax=ax, color="none", edgecolor="black", linewidth=2)

# Plot only the rivers that intersect New York
ny_rivers.plot(ax=ax, color="#4B9CD3", linewidth=1.0, alpha=0.9)  # Increase line width and use a bright color
##us_rivers.plot(ax=ax, color="deepskyblue", linewidth=2, alpha=0.7)

# Add a basemap using OpenStreetMap
ctx.add_basemap(ax, crs=ny_state.crs, source=ctx.providers.OpenStreetMap.Mapnik, alpha=0.5)  # Set alpha for transparency
#ctx.add_basemap(ax, crs=us_states.crs, source=ctx.providers.OpenStreetMap.Mapnik, alpha=0.5) 


# Set plot title
plt.title("New York Rivers & Tributaries", fontsize=16, fontweight='bold')
plt.xlim(ny_state.total_bounds[[0, 2]])  # Set x limits to New York's bounds
plt.ylim(ny_state.total_bounds[[1, 3]])  # Set y limits to New York's bounds

# Optionally, add grid and background
ax.grid(color='lightgrey', linestyle='--', linewidth=0.5)
ax.set_facecolor('whitesmoke')  # Light background color for better contrast

plt.show()
'''

plt.title("Map of U.S. Rivers", fontsize=20)
plt.xlim(-13000000, -7500000)  # Adjust x limits for U.S.
plt.ylim(2000000, 8000000)  

# Optionally, add grid and background
ax.grid(color='lightgrey', linestyle='--', linewidth=0.5)
ax.set_facecolor('whitesmoke')  # Light background color for better contrast

plt.show()

'''
