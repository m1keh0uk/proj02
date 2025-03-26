import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import json

# Meteorite data
with open('meteorites.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df = df[df['reclat'].notna() & df['reclong'].notna()]
df['reclat'] = df['reclat'].astype(float)
df['reclong'] = df['reclong'].astype(float)
fig = plt.figure(figsize=(12, 6))
ax = plt.axes(projection=ccrs.PlateCarree())


ax.add_feature(cfeature.LAND, facecolor='green')
ax.add_feature(cfeature.OCEAN, facecolor='blue')
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.COASTLINE)

gl = ax.gridlines(draw_labels=True, linestyle='--', alpha=0.5)
gl.top_labels = False
gl.right_labels = False

ax.scatter(
    df['reclong'], df['reclat'],
    color='red', s=5, alpha=0.7,
    transform=ccrs.PlateCarree()
)


plt.title("Meteorite Landings", fontsize=14)

plt.savefig("meteorites_map_axes.png", dpi=300, bbox_inches='tight')
plt.show()