import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

from utils.time_utils import timeit

fig, ax = plt.subplots(1, 2)


@timeit
def main(**kwargs):
    x = np.linspace(norm.ppf(0.00001), norm.ppf(0.99999), 10000)
    pdf_x = norm.pdf(x)
    cdf_x = norm.cdf(x)

    # ax[0].plot(x, pdf_x, 'r-', lw=5, alpha=0.6, label='norm pdf')
    # ax[1].plot(x, cdf_x, 'r-', lw=5, alpha=0.6, label='norm pdf')
    # plt.show()


if __name__ == '__main__':
    main(timed=True)
