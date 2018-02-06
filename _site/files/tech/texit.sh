#!/bin/bash

# Remove filename extension
export file=${1%%.*}

# If argument is present
if [ ! -z $file ] ; then

    # Compile latex file
	pdflatex $file.tex
	bibtex $file
	pdflatex $file.tex
	pdflatex $file

    # Remove annoying excess files
    rm $file.out $file\Notes.bib $file.log $file.blg $file.bbl $file.aux
    rm $file.brf texput.log
else
	echo "Usage: texit <tex file>"
fi

