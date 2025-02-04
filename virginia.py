#%%

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import libpysal

#%%

# va county map comes already installed from libpysal
data = gpd.read_file(libpysal.examples.get_path("virginia.shp"))

#%%

# load population dataset into dataframe
pop = pd.read_csv('va-pop-data.csv')

# rename fips column to match map file
pop = pop.rename(columns={"fips": "FIPS"})

# %%

# drop three cities that are not currently in the population list
# of 133 counties and independent cities

data = data[~data['NAME'].isin(['Bedford City', 'Clifton Forge', 'South Boston'])]
data['FIPS'] = pd.to_numeric(data['FIPS'])

# %%

# county names do not match exactly but rather than
# manually cleaning, we can join on fips which is the
# unique state + county identifier

data = data.merge(pop, on="FIPS", how="left")

#%%


#%%

# 2020 MAP
fig, ax = plt.subplots(1, 1, figsize=(10, 8))

data.plot(column="pop2020", cmap="OrRd", linewidth=0.8, edgecolor="black",
         legend=True, ax=ax)

ax.set_title("County Population Map", fontsize=15)

plt.show()

# %%

# growth map
fig2, ax2 = plt.subplots(1, 1, figsize=(10, 8))
data.plot(column="growthSince2020", cmap="OrRd", linewidth=0.8, edgecolor="black",
         legend=True, ax=ax2)
ax2.set_title("County Population Map", fontsize=15)
plt.show()
