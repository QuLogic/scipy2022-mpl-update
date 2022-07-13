"""
Feature highlights for Matplotlib 3.5.0.
"""

import io

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from PIL import Image

from mplslide import BULLET, FONT, new_slide, slide_heading, annotate_pr_author


CODE = dict(fontfamily='monospace', fontsize=40, verticalalignment='top',
            alpha=0.7)


def legend_labelcolor():
    """
    Create slide for feature highlight of legend label color.
    """
    plt.rcParams['legend.labelcolor'] = 'linecolor'

    fig = new_slide()
    slide_heading(fig, '3.5 Feature: legend label color rcParam')

    fig.text(0.05, 0.8, "plt.rcParams['legend.labelcolor'] = 'linecolor'",
             **CODE)

    # Make some fake data.
    a = np.arange(0, 3, .02)
    c = np.exp(a)
    d = c[::-1]

    ax = fig.subplots()
    fig.subplots_adjust(top=0.7)
    ax.plot(a, c, 'g--', label='Model length', linewidth=2)
    ax.plot(a, d, 'r:', label='Data length', linewidth=2)

    ax.legend(loc='upper center', fontsize=20)

    annotate_pr_author(fig, 'Carloscerq', pr=20084)

    return fig


def misc():
    """
    Create slide for miscellaneous feature highlights.
    """
    fig = new_slide()
    slide_heading(fig, '3.5 Miscellaneous Features')

    props = dict(fontproperties=FONT, fontsize=48, alpha=0.7,
                 verticalalignment='top')

    fig.text(0.05, 0.7, 'New backends:', **props)
    t = fig.text(0.05, 0.7, f'\n{BULLET} Qt6/PySide6', **props)
    t.set_url('https://github.com/matplotlib/matplotlib/pull/19255')
    t = fig.text(0.05, 0.7, f'\n\n{BULLET} GTK4', **props)
    t.set_url('https://github.com/matplotlib/matplotlib/pull/20321')

    fig.text(0.05, 0.5, 'Improved widgets:', **props)
    t = fig.text(0.05, 0.5, f'\n{BULLET} Nicer Slider widget', **props)
    t.set_url('https://github.com/matplotlib/matplotlib/pull/19265')
    t = fig.text(0.05, 0.5, f'\n\n{BULLET} Draggable *Selector widgets',
                 **props)
    t.set_url('https://github.com/matplotlib/matplotlib/pull/19657')
    t = fig.text(0.05, 0.5, f'\n\n\n{BULLET} Point removal in PolygonSelector',
                 **props)
    t.set_url('https://github.com/matplotlib/matplotlib/pull/19660')

    # Simulate the old and new Sliders.
    ax_old = fig.add_axes([0.4, 0.42, 0.5, 0.01])
    ax_new = fig.add_axes([0.4, 0.4, 0.5, 0.01])
    Slider(ax_new, "New", 0, 1)

    valmin = 0
    valinit = 0.5
    ax_old.set_xlim([0, 1])
    ax_old.axvspan(valmin, valinit, 0, 1)
    ax_old.axvline(valinit, 0, 1, color="r", lw=1)
    ax_old.set_xticks([])
    ax_old.set_yticks([])
    ax_old.text(-0.02, 0.5, "Old", transform=ax_old.transAxes,
                verticalalignment="center", horizontalalignment="right")
    ax_old.text(1.02, 0.5, "0.5", transform=ax_old.transAxes,
                verticalalignment="center", horizontalalignment="left")

    return fig


def slides():
    """
    Return slides for this section.
    """
    return (
        legend_labelcolor(),
        misc(),
    )
