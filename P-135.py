import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('star_data.csv')

star_name=df['Star Name']
distance=df['Distance (ly)']
mass=df['Mass (M☉)']
radius=df['Radius (R☉)']
gravity=df['Surface Gravity (m/s²)']

#MASS
plt.figure()
plt.bar(star_name,mass)
plt.xlabel("Star Name")
plt.ylabel("Mass of Stars")
plt.title("Star Names & their Masses")
plt.xticks(rotation=90)

#RADIUS
plt.figure()
plt.bar(star_name,radius)
plt.xlabel("Star Name")
plt.ylabel("Radius of Stars")
plt.title("Star Names & their Radii")
plt.xticks(rotation=90)

#DISTANCE
plt.figure()
plt.bar(star_name,distance)
plt.xlabel("Star Name")
plt.ylabel("Distance of Stars")
plt.title("Star Names & their Distance")
plt.xticks(rotation=90)

#gravity
plt.figure()
plt.bar(star_name,gravity)
plt.xlabel("Star Name")
plt.ylabel("Gravity of Stars")
plt.title("Star Names & their Gravities")
plt.xticks(rotation=90)

plt.show()