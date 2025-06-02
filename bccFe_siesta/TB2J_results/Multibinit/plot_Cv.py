#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


def plot_Cv(fname, save_path="Cv_vs_T.pdf"):
    """
    Plot the heat capacity Cv as a function of temperature T.

    Parameters:
    Cv (array-like): Heat capacity values.
    T (array-like): Temperature values.
    save_path (str, optional): Path to save the plot. If None, the plot will be shown.
    """
    data = np.loadtxt(fname, skiprows=1)
    T = data[:-1, 0]  # Temperature values
    Cv = data[:-1, 1]  # Heat capacity values
    chi = data[:-1, 2]  # magnetic susceptibility values
    M = data[:-1, 4]  # magnetic susceptibility values
    fig, axes = plt.subplots(3, 1, sharex=True)

    axes[0].plot(T, Cv, marker='o', linestyle='-', color='b')
    axes[0].set_ylabel('Specific heat')

    axes[1].plot(T, chi, marker='o', linestyle='-', color='r')
    axes[1].set_ylabel('Magnetic susceptibility')

    axes[2].plot(T, M, marker='o', linestyle='-', color='g')
    axes[2].set_ylabel('Magnetization')

    axes[2].set_xlabel('Temperature (K)')
    
    if save_path:
        plt.savefig(save_path)
        print(f"Plot saved to {save_path}")
    plt.show()


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python plot_Cv.py <data_file> [<save_path>]")
        sys.exit(1)
    
    data_file = sys.argv[1]
    save_path = sys.argv[2] if len(sys.argv) > 2 else "Cv_vs_T.pdf"
    plot_Cv(data_file, save_path)
