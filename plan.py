"""
Future plans.
"""

from mplslide import BULLET, FONT, new_slide, slide_heading


def slides():
    """
    Create slide for future plans.
    """
    fig = new_slide()

    slide_heading(fig, 'Future Plans')

    props = dict(fontproperties=FONT, fontsize=56, alpha=0.7,
                 verticalalignment='top')

    fig.text(0.05, 0.8, 'Next feature release: 3.5', **props)
    fig.text(0.1, 0.7, f'{BULLET} September 2021', **props)
    fig.text(0.1, 0.6,
             f'{BULLET} Dropping support for NumPy 1.16',
             **props)
    fig.text(0.1, 0.5,
             f'{BULLET} Adding PyPy wheels for all platforms',
             **props)

    fig.text(0.05, 0.2, 'Check out our blog!', **props)
    t = fig.text(0.1, 0.2, '\nhttps://matplotlib.org/matplotblog/',
                 **props)
    t.set_url('https://matplotlib.org/matplotblog/')

    return fig
