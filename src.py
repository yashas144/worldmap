import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import mpld3

# Set up the map projection
proj = ccrs.PlateCarree()

# Create figure and axis
fig, ax = plt.subplots(figsize=(14, 10), subplot_kw={"projection": proj})

# Set map extent (global view)
ax.set_extent([-180, 180, -90, 90], crs=ccrs.PlateCarree())

# Add features to the map
ax.add_feature(cfeature.LAND, facecolor="lightgreen", edgecolor="black", linewidth=0.5)
ax.add_feature(cfeature.OCEAN, facecolor="lightblue")
ax.add_feature(cfeature.BORDERS, linestyle="--", edgecolor="gray", linewidth=1)
ax.add_feature(cfeature.COASTLINE, edgecolor="black", linewidth=0.5)

# Add gridlines
gridlines = ax.gridlines(draw_labels=True, linestyle="--", linewidth=0.5, color="gray")
gridlines.top_labels = False
gridlines.right_labels = False
gridlines.xlabel_style = {"size": 10, "color": "black"}
gridlines.ylabel_style = {"size": 10, "color": "black"}

# Add title
ax.set_title("Interactive World Map with Geographic Features", fontsize=16, fontweight="bold")

# Save the plot as an interactive HTML
html_str = mpld3.fig_to_html(fig)
with open("worldmap.html", "w") as f:
    f.write(html_str)

