# -*- coding: utf-8 -*-

from __future__ import division

__copyright__ = "Copyright (C) 2014 Andreas Kloeckner"

__license__ = """
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from course.page.base import (
        PageBase, AnswerFeedback, PageContext,
        markup_to_html)
from course.page.static import Page
from course.page.text import TextQuestion
from course.page.choice import ChoiceQuestion
from course.page.code import (
        PythonCodeQuestion, PythonCodeQuestionWithHumanTextFeedback)
from course.page.upload import FileUploadQuestion

__all__ = (
        "PageBase", "AnswerFeedback", "PageContext",
        "markup_to_html"
        "Page",
        "TextQuestion", "ChoiceQuestion",
        "PythonCodeQuestion", "PythonCodeQuestionWithHumanTextFeedback",
        "FileUploadQuestion",
        )

__doc__ = """

.. autoclass:: PageBase
.. autoclass:: AnswerFeedback
.. autoclass:: PageContext

"""
