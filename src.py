import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
from cartopy.io.shapereader import natural_earth, Reader
from adjustText import adjust_text

# Set up map projection
proj = ccrs.PlateCarree()

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 10), subplot_kw={"projection": proj})

# Set map extent (global view)
ax.set_extent([-180, 180, -90, 90], crs=ccrs.PlateCarree())

# Add map features
ax.add_feature(cfeature.LAND, facecolor="lightgreen", edgecolor="black", linewidth=0.5)
ax.add_feature(cfeature.OCEAN, facecolor="lightblue")
ax.add_feature(cfeature.BORDERS, linestyle="--", edgecolor="gray", linewidth=1)
ax.add_feature(cfeature.COASTLINE, edgecolor="black", linewidth=0.5)

# Add country labels
shpfilename = natural_earth(resolution="110m", category="cultural", name="admin_0_countries")
countries = Reader(shpfilename).records()

texts = []
for country in countries:
    country_name = country.attributes['NAME']
    x, y = country.geometry.centroid.xy
    # Adjust font size for dense regions
    font_size = 8 if country_name in ['India', 'China', 'Russia', 'USA', 'Brazil', 'Australia'] else 6
    texts.append(ax.text(x[0], y[0], country_name, fontsize=font_size, transform=ccrs.PlateCarree()))

# Adjust text to avoid overlaps
adjust_text(texts, ax=ax, arrowprops=dict(arrowstyle="-", color="gray", lw=0.5))

# Add gridlines
gridlines = ax.gridlines(draw_labels=True, linestyle="--", linewidth=0.5, color="gray")
gridlines.top_labels = False
gridlines.right_labels = False
gridlines.xlabel_style = {"size": 10, "color": "black"}
gridlines.ylabel_style = {"size": 10, "color": "black"}

# Add title
ax.set_title("World Map with Geographical Features and Country Names", fontsize=16, fontweight="bold")

# Show map
plt.show()
