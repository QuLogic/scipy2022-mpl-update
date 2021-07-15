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


def identify_axes(ax_dict):
    """
    Mark Axes using their name passed to ``subplot_mosaic``.
    """
    kw = dict(ha='center', va='center', fontsize=48, color='darkgrey')
    for k, ax in ax_dict.items():
        ax.text(0.5, 0.5, k, transform=ax.transAxes, **kw)


def mosaic():
    """
    Create slide for feature highlight of subplot_mosaic shortcut.
    """

    example1 = """
    '''
    AB
    CC
    '''"""
    example2 = "'AB;CC'"

    for text in [example1, example2]:
        fig = new_slide()

        slide_heading(fig, '3.4 Feature: subplot_mosaic shortcut')

        fig.text(0.05, 0.8, f'plt.figure().subplot_mosaic({text})', **CODE)

        ax_dict = fig.subplot_mosaic(eval(text.lstrip()),
                                     # Don't overlay title and code.
                                     gridspec_kw={'left': 0.3, 'top': 0.7,
                                                  'right': 0.97})
        identify_axes(ax_dict)

        annotate_pr_author(fig, 'timhoffm', pr=18763)

        yield fig


def slides():
    """
    Return slides for this section.
    """
    return (
        *subfigure(),
        *mosaic(),
    )
