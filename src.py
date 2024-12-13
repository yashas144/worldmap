'''import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
from cartopy.io.shapereader import natural_earth, Reader
from adjustText import adjust_text
import mpld3

# Set up the map projection
proj = ccrs.PlateCarree()

# Create figure and axis
fig, ax = plt.subplots(figsize=(16, 12), subplot_kw={"projection": proj})

# Set map extent (global view)
ax.set_extent([-180, 180, -90, 90], crs=ccrs.PlateCarree())

# Add features to the map
ax.add_feature(cfeature.LAND, facecolor="lightgreen", edgecolor="black", linewidth=0.5)
ax.add_feature(cfeature.OCEAN, facecolor="lightblue")
ax.add_feature(cfeature.BORDERS, linestyle="--", edgecolor="gray", linewidth=0.8)
ax.add_feature(cfeature.COASTLINE, edgecolor="black", linewidth=0.8)

# Load country geometries from Natural Earth
shpfilename = natural_earth(resolution='110m', category='cultural', name='admin_0_countries')
countries = Reader(shpfilename).records()

# Collect country names and coordinates
texts = []
for country in countries:
    country_name = country.attributes['NAME']
    # Calculate the centroid of the country geometry
    centroid = country.geometry.centroid
    lon, lat = centroid.x, centroid.y
    # Add text labels for country names
    texts.append(ax.text(lon, lat, country_name, fontsize=6, transform=ccrs.PlateCarree()))

# Dynamically adjust text labels to minimize overlaps
adjust_text(
    texts,
    arrowprops=dict(arrowstyle="->", color="gray", lw=0.5),
    force_text=0.5,  # Adjust label force
    force_points=0.2,
    expand_text=(1.5, 1.5),
    only_move={'points': 'xy', 'text': 'xy'},  # Allow movement in both x and y
)

# Add gridlines
gridlines = ax.gridlines(draw_labels=True, linestyle="--", linewidth=0.5, color="gray")
gridlines.top_labels = False
gridlines.right_labels = False
gridlines.xlabel_style = {"size": 10, "color": "black"}
gridlines.ylabel_style = {"size": 10, "color": "black"}

# Add title
ax.set_title("Optimized Interactive World Map with Country Names", fontsize=18, fontweight="bold")

# Save the plot as an interactive HTML
html_str = mpld3.fig_to_html(fig)
with open("optimized_worldmap.html", "w") as f:
    f.write(html_str)

# Optionally display the map (for testing purposes)
plt.show()'''

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
from cartopy.io.shapereader import natural_earth, Reader
from adjustText import adjust_text
import mpld3

# Set up the map projection
proj = ccrs.PlateCarree()

# Create figure and axis
fig, ax = plt.subplots(figsize=(20, 12), subplot_kw={"projection": proj})

# Set map extent (global view)
ax.set_extent([-180, 180, -90, 90], crs=ccrs.PlateCarree())

# Add map features
ax.add_feature(cfeature.LAND, facecolor="lightgreen", edgecolor="black", linewidth=0.5)
ax.add_feature(cfeature.OCEAN, facecolor="lightblue")
ax.add_feature(cfeature.BORDERS, linestyle="--", edgecolor="gray", linewidth=1)
ax.add_feature(cfeature.COASTLINE, edgecolor="black", linewidth=0.8)
ax.add_feature(cfeature.LAKES, facecolor="aqua", edgecolor="blue", linewidth=0.5)
ax.add_feature(cfeature.RIVERS, edgecolor="blue", linewidth=0.5)

# Load country geometries from Natural Earth
shpfilename = natural_earth(resolution='110m', category='cultural', name='admin_0_countries')
countries = Reader(shpfilename).records()

# Dynamically place country labels
texts = []
for country in countries:
    country_name = country.attributes['NAME']
    centroid = country.geometry.centroid
    lon, lat = centroid.x, centroid.y

    # Skip countries with unusual geometries
    if not (-180 <= lon <= 180 and -90 <= lat <= 90):
        continue

    # Add country names as labels
    texts.append(ax.text(lon, lat, country_name, fontsize=8, transform=ccrs.PlateCarree(), color="black"))

# Adjust text positions dynamically to avoid overlaps
adjust_text(
    texts,
    arrowprops=dict(arrowstyle="->", color="gray", lw=0.5),
    force_text=1.0,
    expand_text=(1.2, 1.5),
    only_move={'points': 'xy', 'text': 'xy'},
    force_points=0.3,
)

# Add interactive gridlines
gridlines = ax.gridlines(draw_labels=True, linestyle="--", linewidth=0.5, color="gray")
gridlines.top_labels = False
gridlines.right_labels = False
gridlines.xlabel_style = {"size": 12, "color": "black"}
gridlines.ylabel_style = {"size": 12, "color": "black"}

# Add a masterpiece title
ax.set_title(
    "Interactive World Map With Geographical Features and Country Names",
    fontsize=20,
    fontweight="bold",
    pad=20,
)

# Save the masterpiece as an interactive HTML file
html_str = mpld3.fig_to_html(fig)
with open("masterpiece_worldmap.html", "w") as f:
    f.write(html_str)

# Optionally display the map for quick preview
plt.show()






