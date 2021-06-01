import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 2)


x = np.linspace(norm.ppf(0.01), norm.ppf(0.99), 100)
ax[0].plot(x, norm.pdf(x), 'r-', lw=5, alpha=0.6, label='norm pdf')
ax[1].plot(x, norm.cdf(x), 'r-', lw=5, alpha=0.6, label='norm pdf')
plt.show()
