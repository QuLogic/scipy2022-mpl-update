"""
Feature highlights for Matplotlib 3.5.0.
"""

import io

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from mplslide import FONT, new_slide, slide_heading, annotate_pr_author


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


def cvdsim():
    """
    Create slide for feature highlight of CVD cimulation.
    """

    fig = new_slide()
    slide_heading(fig, '3.5 Feature: Color simulations')
    fig.text(0.05, 0.75, 'Simulate various color vision deficiencies',
             fontproperties=FONT, fontsize=48, alpha=0.7)

    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)

    filters = [None, 'greyscale', 'deuteranopia', 'tritanopia']
    axs = fig.subplots(1, len(filters))
    fig.subplots_adjust(top=0.7)

    for real_ax, filt in zip(axs, filters):
        pie, ax = plt.subplots(figsize=(4, 4))
        ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
               shadow=True, startangle=90)
        ax.axis('equal')
        pie.set_agg_filter(filt)
        img = io.BytesIO()
        pie.savefig(img, format='png', dpi=300)

        pie = Image.open(img)
        real_ax.set_title(filt.title() if filt else 'Unaltered', fontsize=20)
        real_ax.imshow(pie)
        real_ax.set(xticks=[], yticks=[])

    annotate_pr_author(fig, 'QuLogic', pr=20649)

    return fig


def slides():
    """
    Return slides for this section.
    """
    return (
        legend_labelcolor(),
        cvdsim(),
    )
