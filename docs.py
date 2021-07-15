"""
Documentation highlights.
"""

from mplslide import FONT, new_slide, slide_heading


def docs():
    fig = new_slide()

    slide_heading(fig, 'Documentation')

    props = dict(fontproperties=FONT, fontsize=48, alpha=0.7,
                 verticalalignment='top')

    fig.text(0.05, 0.7, "3.4 What's New?", **props)
    t = fig.text(0.07, 0.7,
                 '\nhttps://matplotlib.org/3.4.0/users/whats_new.html',
                 **props)
    t.set_url('https://matplotlib.org/3.4.0/users/whats_new.html')

    fig.text(0.05, 0.5, "Upcoming 3.5 What's New?", **props)
    t = fig.text(0.07, 0.5,
                 '\nhttps://matplotlib.org/devdocs/users/next_whats_new.html',
                 **props)
    t.set_url('https://matplotlib.org/devdocs/users/next_whats_new.html')
    fig.text(0.05, 0.5, '\n\nOnce tagged, will be at:', **props)
    t = fig.text(0.07, 0.5,
                 '\n\n\nhttps://matplotlib.org/3.5.0/users/whats_new.html',
                 **props)
    t.set_url('https://matplotlib.org/3.5.0/users/whats_new.html')

    fig.text(0.05, 0.2, 'Switch to pydata-sphinx-theme', **props)
    t = fig.text(0.07, 0.2,
                 '\nhttps://pydata-sphinx-theme.readthedocs.io/en/latest/',
                 **props)
    t.set_url('https://pydata-sphinx-theme.readthedocs.io/en/latest/')

    return fig


def slides():
    """
    Return slides for this section.
    """
    return (
        docs(),
    )
