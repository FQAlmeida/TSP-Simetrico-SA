from load_data import load
from matplotlib import pyplot

data = load(f"../output.txt")

fig, axs = pyplot.subplots(2, 1)

xs = list(map(lambda d: d.iteraction, data))
ys_dist = list(map(lambda d: d.distance, data))
ys_temp = list(map(lambda d: d.temperature, data))

axs[0].plot(xs, ys_dist)
axs[0].set_xlabel("Iteraction")
axs[0].set_ylabel("Distance")

axs[1].plot(xs, ys_temp)
axs[1].set_xlabel("Iteraction")
axs[1].set_ylabel("Temperature")

fig.tight_layout()

# pyplot.show()
pyplot.savefig(f"../data/conv_exp.png")
