"""
General news.
"""

from functools import partial

from mplslide import BULLET, FONT, new_slide, slide_heading


def bullet_level1(fig, y, text):
    """
    Create a level 1 list item.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        A slide figure.
    y : float
        The vertical position for the list item, in 0-1 figure space.
    text : str
        The text to place in the list item.
    """
    return fig.text(0.05, y, text,
                    fontproperties=FONT, fontsize=48, alpha=0.7,
                    verticalalignment='top')


def bullet_level2(fig, y, text):
    """
    Create a level 2 list item.

    This is roughly the same as level 1, but not bolded, and indented more.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        A slide figure.
    y : float
        The vertical position for the list item, in 0-1 figure space.
    text : str
        The text to place in the list item.
    """
    return fig.text(0.1, y, text,
                    fontproperties=FONT, fontsize=48, fontweight='normal',
                    alpha=0.7, verticalalignment='top')


def slides():
    """
    Create slide for general community news.
    """
    fig = new_slide()

    slide_heading(fig, 'Community News')

    level1 = partial(bullet_level1, fig)
    level2 = partial(bullet_level2, fig)

    t = level1(
        0.8,
        f'{BULLET} Chan Zuckerberg Initiative grant \N{EM dash} EOSS cycle 4')
    t.set_url('https://matplotlib.org/matplotblog/posts/matplotlib-rsef/')

    level2(0.8,
           '\nThomas Caswell, Elliott Sales de Andrade')

    t = level1(0.675, f'{BULLET} NASA ROSES-OSTFL 2020')
    t.set_url('https://discourse.matplotlib.org/t/'
              'maplotlib-selected-for-nasa-roses-ostfl-2020')
    level1(0.675,
           '\n    \N{EM dash} Revamping Matplotlib for Modern Data Structures')
    level2(0.675, '\n\nKyle Sunden')

    t = level1(0.475, f'{BULLET} Contributor Experience Leads')
    t.set_url(
        'https://chanzuckerberg.com/eoss/proposals/'
        'advancing-an-inclusive-culture-in-the-scientific-python-ecosystem/')

    level2(0.475, '\nMelissa Mendonça and Noa Tamir')

    t = level1(
        0.35,
        f'{BULLET} New Contributors Meeting (first Tuesday of month)')
    t.set_url('https://hackmd.io/@matplotlib/SJ3oc8oqq')

    level1(0.275,
           f'{BULLET} Moved documentation from GitHub Pages to DigitalOcean')

    level1(0.2, f'{BULLET} Third-party packages')

    t = level2(0.2, '\nPyPI classifier: Framework :: Matplotlib')
    t.set_url('https://pypi.org/search/?c=Framework+%3A%3A+Matplotlib')

    t = level2(0.2, '\n\nhttps://matplotlib.org/mpl-third-party/')
    t.set_url('https://matplotlib.org/mpl-third-party/')

    return fig
