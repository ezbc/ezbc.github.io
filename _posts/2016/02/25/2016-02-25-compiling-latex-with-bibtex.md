---
author: Elijah Bernstein-Cooper
category:
- professional
- tech
comments: true
date: 2016-02-25 00:00
excerpt: I outline the methods needed to compile references using Bibtex in a Latex
  document.
layout: post
redirect_from: /tech-project/2016/02/25/compiling-latex-with-bibtex
tags:
- bash
title: Script for Compiling Latex with Bibtex
use_math: true
---

# Download

Below you can download a script to automatically compile a tex document with
Bibtex references.

<div align="center">
  <a href="/files/tech/texit.sh">
    <button type="button" class="btn btn-default">
      Download script
    </button>
  </a>
</div>

# Compiling

Bibtex provides an easy way to manage references in latex. A great
[tutorial](http://www.latex-tutorial.com/tutorials/beginners/lesson-7/) can get
one started with Bibtex quickly. The compilation of a tex document with the
correct cross-referencing with bibtex includes several steps.

In order to compile a tex document with the cross-referencing, run the bash
script ``texit.sh`` as follows

~~~ bash
./texit.sh <filename>
~~~

This requires the `pdflatex` and `bibtex` software, both included in the
[`texlive`](http://www.tug.org/texlive/) package. An explanation of what this
bash script does is below.

# Explanation of Compilation

The tex document needs to be compiled a total of four times in the following
manner

~~~ bash
pdflatex <filename_base>.tex
bibtex <filename_base>
pdflatex <filename_base>.tex
pdflatex <filename_base>
~~~

The first ``pdflatex`` command tells bibtex what literature we cited in our paper. The ``bibtex`` command creates a ``.bib`` file which will be translated into the references section. The next two steps merge the reference section with the latex document and then assigns successive numbers in the last step.