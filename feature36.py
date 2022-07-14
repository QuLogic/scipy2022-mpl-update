"""
Feature highlights for Matplotlib 3.6.0.
"""

import io

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from PIL import Image

from mplslide import new_slide, slide_heading, annotate_pr_author


CODE = dict(fontfamily='monospace', fontsize=40, verticalalignment='top',
            alpha=0.7)


def better3d():
    """
    Create slide for 3D improvement highlights.
    """
    fig = new_slide()
    slide_heading(fig, '3.6: 3D Improvements')

    X, Y, Z = axes3d.get_test_data(0.05)

    axs = fig.subplots(1, 2, subplot_kw={'projection': '3d'})

    # Show focal length feature.
    axs[0].plot_wireframe(X, Y, Z, rstride=10, cstride=10)
    axs[0].set_proj_type('persp', focal_length=0.1)
    axs[0].set_title('focal_length = 0.1', fontsize=20)

    axs[1].plot_wireframe(X, Y, Z, rstride=10, cstride=10)
    axs[1].view_init(elev=0, azim=0, roll=30)
    axs[1].set_title('roll=30', fontsize=20)

    return fig


def font_fallback():
    """
    Create slide for font fallback highlight.
    """

    # We can't show this directly because font fallback is only in Agg
    # backends, not the PDF backend.
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100)
    for y, family in [
            (0.7, ['WenQuanYi Zen Hei']),
            (0.55, ['Noto Sans CJK JP']),
            (0.3, ['DejaVu Sans', 'Noto Sans CJK JP']),
            (0.15, ['DejaVu Sans', 'WenQuanYi Zen Hei'])]:
        fig.text(0.05, y, f'There are 几个汉字 in between!\n{family}',
                 family=family, fontsize=48)

    data = io.BytesIO()
    fig.savefig(data, dpi=300)
    img = Image.open(data)

    fig = new_slide()
    slide_heading(fig, '3.6: Font Fallback')

    # Now embed the Agg produced image in the PDF.
    ax = fig.add_axes([0.05, 0.1, 0.9, .75])
    ax.imshow(img)
    ax.set_frame_on(False)
    ax.tick_params(labelleft=False, left=False,
                   labelbottom=False, bottom=False)

    annotate_pr_author(fig, 'aitikgupta', 'tacaswell', pr=20740)

    return fig


def slides():
    """
    Return slides for this section.
    """
    return (
        better3d(),
        font_fallback(),
    )
