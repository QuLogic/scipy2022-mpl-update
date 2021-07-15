"""
Feature highlights for Matplotlib 3.4.0.
"""

from mplslide import FONT, new_slide, slide_heading, annotate_pr_author


CODE = dict(fontfamily='monospace', fontsize=40, verticalalignment='top',
            alpha=0.7)


def subfigure():
    """
    Create slide for feature highlight of subfigures.
    """

    subfigure_code = """\
fig = plt.figure()
subfigs = fig.subfigures(1, 2)

axsLeft = subfigs[0].subplots(1, 2)
for ax in axsLeft:
    ax.plot([1, 2, 3])

axsRight = subfigs[1].subplots(3, 1)
for ax in axsRight:
    ax.plot([5, 4, 3])
"""

    fig = new_slide()
    slide_heading(fig, '3.4 Feature: SubFigures')
    fig.text(0.05, 0.75,
             'Nestable subdivisions of your figure that act like a figure',
             fontproperties=FONT, fontsize=48, alpha=0.7)
    fig.text(0.05, 0.7, subfigure_code, **CODE)
    annotate_pr_author(fig, 'jklymak', pr=18356)

    yield fig

    fig = new_slide()
    slide_heading(fig, '3.4 Feature: SubFigures')
    fig.subplots_adjust(top=0.8)

    subfigs = fig.subfigures(1, 2)
    left = subfigs[0].subplots(1, 2)
    for ax in left:
        ax.plot([1, 2, 3])
    right = subfigs[1].subplots(3, 1)
    for ax in right:
        ax.plot([5, 4, 3])
    for subfig in subfigs:
        subfig.set_facecolor('none')

    annotate_pr_author(fig, 'jklymak', pr=18356)
    yield fig


def slides():
    """
    Return slides for this section.
    """
    return (
        *subfigure(),
    )
