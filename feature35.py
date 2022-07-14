"""
Feature highlights for Matplotlib 3.5.0.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

from mplslide import (
    BULLET, FONT, new_slide, slide_heading, slide_subfig_heading,
    annotate_pr_author)


CODE = dict(fontfamily='monospace', fontsize=40, verticalalignment='top',
            alpha=0.7)


def mosaic_sharing():
    """
    Create slide for mosaic Axes sharing highlight.
    """
    fig = new_slide(constrained_layout=True)
    top, middle, bottom = fig.subfigures(3, 1, height_ratios=[1, 2, 3])
    slide_subfig_heading(top, '3.5: subplot_mosaic Axes sharing')
    top.set_facecolor('none')

    middle.text(0.05, 1, '''mosaic = [['A', [['B', 'C'], ['D', 'E']]],
          ['F', 'G']]
ax_dict = fig.subplot_mosaic(mosaic, sharex=True,
                             sharey=True)
ax_dict['A'].set(xscale='log', yscale='symlog',
                 ylim=(-1, 10))
    ''', **CODE)
    middle.set_facecolor('none')

    mosaic = [
        ['A', [['B', 'C'],
               ['D', 'E']]],
        ['F', 'G'],
    ]
    with plt.rc_context({'xtick.labelsize': 20, 'ytick.labelsize': 20}):
        ax_dict = bottom.subplot_mosaic(mosaic, sharex=True, sharey=True)
        ax_dict['A'].set(xscale='log', yscale='symlog', ylim=(-1, 10))

    annotate_pr_author(fig, 'anntzer', pr=20107)

    return fig


def image_antialiasing():
    """
    Create slide for image antialiasing feature highlight.
    """

    N = 450
    x = np.arange(N) / N - 0.5
    y = np.arange(N) / N - 0.5
    aa = np.ones((N, N))
    aa[::2, :] = -1

    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2 + Y**2)
    f0 = 5
    k = 100
    a = np.sin(np.pi * 2 * (f0 * R + k * R**2 / 2))
    # make the left hand side of this
    a[:int(N / 2), :][R[:int(N / 2), :] < 0.4] = -1
    a[:int(N / 2), :][R[:int(N / 2), :] < 0.3] = 1
    aa[:, int(N / 3):] = a[:, int(N / 3):]
    a = aa

    fig = new_slide(constrained_layout=True)
    top, bottom = fig.subfigures(2, 1, height_ratios=[1, 5])
    slide_subfig_heading(top, '3.5: RGBA image interpolation')
    top.set_facecolor('none')

    axs = bottom.subplots(2, 3)

    for col, interp, space in zip(axs.T,
                                  ['nearest', 'antialiased', 'antialiased'],
                                  ['data', 'data', 'rgba']):
        for ax in col:
            ax.imshow(a, interpolation=interp, interpolation_stage=space,
                      cmap='RdBu_r')
            ax.tick_params(labelbottom=False, labelleft=False)

        # Zoomed Axes on top.
        col[0].set_xlim(100, 200)
        col[0].set_ylim(275, 175)
        # Title in between.
        col[1].set_title(f"interpolation='{interp}'\n"
                         f"interpolation_space='{space}'",
                         fontsize=20)

        # With inset Axes indicator between rows.
        frame, connectors = col[1].indicate_inset_zoom(col[0], linewidth=3)
        for conn in connectors:
            conn.set_in_layout(False)
            conn.set_linewidth(3)

    annotate_pr_author(fig, 'jklymak', pr=18782)

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

    url = ('https://matplotlib.org/3.5.0/users/prev_whats_new/'
           'whats_new_3.5.0.html')
    fig.text(0.05, 0.225, "3.5 What's New?", **props)
    t = fig.text(0.07, 0.225, f'\n\n{url}', **{**props, 'fontsize': 32})
    t.set_url(url)

    return fig


def slides():
    """
    Return slides for this section.
    """
    return (
        mosaic_sharing(),
        image_antialiasing(),
        misc(),
    )
