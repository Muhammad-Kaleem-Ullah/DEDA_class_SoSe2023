from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tools.sm_exceptions import ValueWarning, HessianInversionWarning, ConvergenceWarning
import matplotlib.pyplot as plt

def acf_plot(data, unit):
    plot_acf(data)
    plt.grid(False)
    plt.savefig(f"plots/ACF_{unit}.png", dpi = 300, transparent = True)
    plt.show()

def pacf_plot(data, unit):
    plot_pacf(data)
    plt.grid(False)
    plt.savefig(f"plots/PACF_{unit}.png", dpi = 300, transparent = True)
    plt.show()