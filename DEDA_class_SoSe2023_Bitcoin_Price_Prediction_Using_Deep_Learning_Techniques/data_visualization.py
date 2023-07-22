import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")
from time_series_analysis import acf_plot, pacf_plot

def exploratory_data_analysis(data, unit, time_series = True):
    plot_series(data, unit)
    
    if unit == "returns":
        plot_returns_statistics(data)
    else:
        plot_statistics_price(data)
    if time_series:
        acf_plot(data, unit)
        pacf_plot(data, unit)


    
def plot_series(data, unit):
    plt.figure(figsize = (16, 8))
    #plt.title("Bitcoin Price History")
    if unit != "returns":
        plt.plot(data["Close"])
    else:
        plt.plot(data)
    plt.xlabel("Date", fontsize = 18)
    plt.ylabel(f"Close {unit.capitalize()} USD ($)", fontsize = 18)
    plt.grid(False)
    if not os.path.exists("plots"):
        os.makedirs("plots")
    plt.savefig('plots/history.png', dpi=300, transparent = True)
    plt.show()

    
def plot_statistics_price(data):
    # Calculate the summary statistics
    mean_return = np.mean(data["Close"])
    std_dev = np.std(data["Close"])
    skewness = pd.Series(data["Close"]).skew()
    kurtosis = pd.Series(data["Close"]).kurtosis()
    min_return = np.min(data["Close"])
    max_return = np.max(data["Close"])
    q1 = np.percentile(data["Close"], 25)
    q2 = np.percentile(data["Close"], 50)
    q3 = np.percentile(data["Close"], 75)
    
    # Plotting the price series with summary statistics
    plt.figure(figsize = (16, 8))
    #plt.title("Bitcoin Price History")
    plt.plot(data["Close"])
    plt.xlabel("Date", fontsize = 18)
    plt.ylabel("Close Price USD ($)", fontsize = 18)
    
    # Add summary statistics to the plot
    summary_text = f"Mean: {mean_return:.6f}\nStd Dev: {std_dev:.6f}\nSkewness: {skewness:.6f}\nKurtosis: {kurtosis:.6f}\nMin: {min_return:.6f}\nMax: {max_return:.6f}\nQ1: {q1:.6f}\nQ2: {q2:.6f}\nQ3: {q3:.6f}"
    plt.text(0.02, 0.95, summary_text, transform=plt.gca().transAxes, fontsize=10, verticalalignment='top')
    
    # Add arrows to highlight specific values
    arrow_properties = dict(facecolor='red', edgecolor='red', arrowstyle='->', linewidth=2.5)
    plt.annotate(f'Max: {max_return:.6f}', xy=(data['Close'].idxmax(), data['Close'].max()), xytext=(20, -50),
                 textcoords='offset points', arrowprops=arrow_properties)
    plt.annotate(f'Min: {min_return:.6f}', xy=(data['Close'].idxmin(), data['Close'].min()), xytext=(-70, 40),
             textcoords='offset points', arrowprops=arrow_properties)

    plt.grid(False)
    plt.savefig('plots/price_statistics.png', dpi=300, transparent = True)
    plt.show()
    
def plot_returns_statistics(returns):
    # Calculate the summary statistics
    mean_return = np.mean(returns)
    std_dev = np.std(returns)
    skewness = pd.Series(returns).skew()
    kurtosis = pd.Series(returns).kurtosis()
    min_return = np.min(returns)
    max_return = np.max(returns)
    q1 = np.percentile(returns, 25)
    q2 = np.percentile(returns, 50)
    q3 = np.percentile(returns, 75)
    
    # Plotting the price series with summary statistics
    plt.figure(figsize = (16, 8))
    #plt.title("Bitcoin Price History")
    plt.plot(returns)
    plt.xlabel("Date", fontsize = 18)
    plt.ylabel("Close Price USD ($)", fontsize = 18)
    
    # Add summary statistics to the plot
    summary_text = f"Mean: {mean_return:.6f}\nStd Dev: {std_dev:.6f}\nSkewness: {skewness:.6f}\nKurtosis: {kurtosis:.6f}\nMin: {min_return:.6f}\nMax: {max_return:.6f}\nQ1: {q1:.6f}\nQ2: {q2:.6f}\nQ3: {q3:.6f}"
    plt.text(0.02, 0.95, summary_text, transform=plt.gca().transAxes, fontsize=10, verticalalignment='top')
    
    # Add arrows to highlight specific values
    arrow_properties = dict(facecolor='red', edgecolor='red', arrowstyle='->', linewidth=2.5)
    plt.annotate(f'Max: {max_return:.6f}', xy=(np.argmax(returns), returns.max()), xytext=(20, -50),
                 textcoords='offset points', arrowprops=arrow_properties)
    plt.annotate(f'Min: {min_return:.6f}', xy=(np.argmin(returns), returns.min()), xytext=(-70, 40),
                 textcoords='offset points', arrowprops=arrow_properties)
    
    plt.grid(False)
    plt.savefig('plots/returns_statistics.png', dpi=300, transparent = True)
    plt.show()