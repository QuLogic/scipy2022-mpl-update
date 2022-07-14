"""
Future plans.
"""

from mplslide import FONT, new_slide, slide_heading


def slides():
    """
    Create slide for future plans.
    """
    fig = new_slide()

    slide_heading(fig, 'Future Plans')

    props = dict(fontproperties=FONT, alpha=0.7, verticalalignment='top')

    url = 'https://matplotlib.org/devdocs/users/next_whats_new.html'
    fig.text(0.05, 0.7, "Upcoming 3.6 What's New?", fontsize=56, **props)
    t = fig.text(0.07, 0.7, f'\n\n{url}', fontsize=32, **props)
    t.set_url(url)
    url = ('https://matplotlib.org/3.6.0/users/prev_whats_new/'
           'whats_new_3.6.0.html')
    fig.text(0.05, 0.5, 'Once tagged, will be at:', fontsize=56, **props)
    t = fig.text(0.07, 0.5, f'\n\n{url}', fontsize=32, **props)
    t.set_url(url)

    fig.text(0.05, 0.3, 'Your Contribution?', fontsize=56, **props)

    return fig
