build:
	pdflatex doc.tex

clean:
	rm -rf doc.aux doc.log doc.out doc.pdf

requirements:
	apt-get install texlive-latex-extra texlive-fonts-recommended
