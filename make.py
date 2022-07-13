#!/usr/bin/env python3

"""
Generate slides for the presentation.

Usage: ./make.py /path/to/matplotlib/checkout

You must make a clone of the Matplotlib git repository available, and should
have the Carlito and/or Calibri font installed.
"""

import shutil
import subprocess
import sys

from matplotlib.backends.backend_pdf import PdfPages

from mplslide import check_requirements
# This must be called before importing other files to make the font available.
check_requirements()  # noqa: F402

from title import create_icon_axes, slides as title_slides
from news import slides as news_slides
from timeline import slides as history_slides
from feature35 import slides as feature35_slides
# from feature36 import slides as feature36_slides
from docs import slides as docs_slides
from plan import slides as plan_slides
from end import slides as end_slides


METADATA = {
    'Author': 'Elliott Sales de Andrade',
    'Title': 'Matplotlib Project Update for SciPy 2022',
}
MPL_PATH = sys.argv[1]
PAGES = [
    # Tuple of function + any arguments.
    (title_slides, ),
    (news_slides, ),
    (history_slides, MPL_PATH, ),
    (feature35_slides, ),
    # (feature36_slides, ),
    (docs_slides, ),
    (plan_slides, ),
    (end_slides, ),
]

with PdfPages('slides.pdf', metadata=METADATA) as pdf:
    for page, *args in PAGES:
        figs = page(*args)
        if not isinstance(figs, (tuple, list)):
            figs = (figs, )
        for fig in figs:
            if not fig.mplslide_props['plain']:
                create_icon_axes(fig, (0.825, 0.825, 0.2, 0.15),
                                 0.3, 0.3, 0.3, [5])
            pdf.savefig(fig)

# Linearize the PDF if qpdf is available.
if shutil.which('qpdf') is not None:
    subprocess.run(['qpdf', 'slides.pdf', '--object-streams=generate',
                    '--linearize', 'scipy2022-mpl-update.pdf'])
else:
    shutil.copy('slides.pdf', 'scipy2022-mpl-update.pdf')
