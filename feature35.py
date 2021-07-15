"""
Feature highlights for Matplotlib 3.5.0.
"""

import numpy as np
import matplotlib.pyplot as plt

from mplslide import new_slide, slide_heading, annotate_pr_author


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


def slides():
    """
    Return slides for this section.
    """
    return (
        legend_labelcolor(),
    )
