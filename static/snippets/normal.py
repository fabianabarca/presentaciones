import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
from pyscript import display

rv = stats.norm(0, 1)
rv_samples = rv.rvs(size=1000)
fig, ax = plt.hist(rv_samples, bins=30, density=True)
# x = np.linspace(-4, 4, 100)
# plt.plot(x, rv.pdf(x))

display("fig")
