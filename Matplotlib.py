import matplotlib.pyplot as plt
import numpy as np
np.random.seed(444)
# fig,_ = plt.subplots()

# print(type(fig))

# one_tick = fig.axes[0].yaxis.get_major_ticks()[0]

# print(type(one_tick))

# fig, ax = plt.subplots()

rng = np.arange(50)
rnd = np.random.randint(0, 10, size=(3, rng.size))
yrs = 1950 + rng







rng = np.arange(50)
rnd = np.random.randint(0, 10, size=(3, rng.size))
yrs = 1950 + rng
fig, ax = plt.subplots(figsize=(5, 3))
ax.stackplot(yrs, rng + rnd, labels=['Eastasia', 'Eurasia', 'Oceania'])
ax.set_title('Combined debt growth over time')
ax.legend(loc='upper left')
ax.set_ylabel('Total debt')
ax.set_xlim(xmin=yrs[0], xmax=yrs[-1])
fig.tight_layout()
plt.show()