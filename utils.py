"""
Author:       Roberto Chiosa
Copyright:    Roberto Chiosa, © 2024
Email:        roberto.chiosa@pinvision.it

Created:      01/07/24
Script Name:  utils.py
Path:         

Script Description:


Notes:
"""

import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt


def plot_dynamic(data: pd.DataFrame) -> px:
    """
    This function creates a dynamic plotly visualization
    :param data: data to plot
    :return: plotly figure
    """
    fig = px.line(data)
    return fig


def plot_static(data: pd.DataFrame) -> plt:
    """
    This function creates a static matplotlib visualization
    :param data: data to plot
    :return: matplotlib figure
    """
    # create a simple matplotlib visualization
    plt.figure(figsize=(10, 6))
    plt.plot(data)
    plt.title('Simple plot')
    plt.xlabel('x')
    return plt
