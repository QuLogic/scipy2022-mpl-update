"""
Documentation highlights.
"""

from mplslide import FONT, new_slide, slide_heading


def docs():
    fig = new_slide()

    slide_heading(fig, 'Documentation')

    props = dict(fontproperties=FONT, alpha=0.7, verticalalignment='top')

    url = ('https://matplotlib.org/3.5.0/users/prev_whats_new/'
           'whats_new_3.5.0.html')
    fig.text(0.05, 0.7, "3.5 What's New?", fontsize=48, **props)
    t = fig.text(0.07, 0.7, f'\n\n{url}', fontsize=32, **props)
    t.set_url(url)

    fig.text(0.05, 0.55, 'Switch to pydata-sphinx-theme', fontsize=48, **props)
    t = fig.text(0.07, 0.55,
                 '\n\nhttps://pydata-sphinx-theme.readthedocs.io/en/latest/',
                 fontsize=32, **props)
    t.set_url('https://pydata-sphinx-theme.readthedocs.io/en/latest/')

    url = 'https://matplotlib.org/devdocs/users/next_whats_new.html'
    fig.text(0.05, 0.4, "Upcoming 3.6 What's New?", fontsize=48, **props)
    t = fig.text(0.07, 0.4, f'\n\n{url}', fontsize=32, **props)
    t.set_url(url)
    url = ('https://matplotlib.org/3.6.0/users/prev_whats_new/'
           'whats_new_3.6.0.html')
    fig.text(0.05, 0.25, 'Once tagged, will be at:', fontsize=48, **props)
    t = fig.text(0.07, 0.25, f'\n\n{url}', fontsize=32, **props)
    t.set_url(url)

    return fig


def slides():
    """
    Return slides for this section.
    """
    return (
        docs(),
    )
