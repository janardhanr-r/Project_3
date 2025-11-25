import sys
import pandas as pd
import matplotlib.pyplot as plt

# readin the data 
# assuming file has 3 collumns x, y, count
df = pd.read_csv(sys.stdin, sep="\t", header=None, names=["x", "y", "count"])

# making the figure with 2 rows 
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))

# --- First Garph (Top) ---
# ploting dots
# cmap is color 
plot1 = ax1.scatter(df.x, df.y, c=df.count, cmap="BuPu", s=1)

# setting limits
ax1.set_xlim(-500, 500)
ax1.set_ylim(0, 200)

# adding color bar on side
fig.colorbar(plot1, ax=ax1)

# --- Second Graph (Bottom) ---
# ploting again
plot2 = ax2.scatter(df.x, df.y, c=df.count, cmap="BuPu", s=1)

# samller limits here
ax2.set_xlim(-200, 200)
ax2.set_ylim(0, 200)

# label for count
fig.colorbar(plot2, ax=ax2, label="Count")

# labels for whole pic
fig.text(0.5, 0.02, "Distance", ha="center")
fig.text(0.02, 0.5, "Fragment Length", va="center", rotation="vertical")

# saveing file
plt.savefig("output.png", dpi=600)
print("Saved output.png")