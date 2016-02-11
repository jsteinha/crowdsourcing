default:
	pdflatex icml2016.tex
	bibtex icml2016
	pdflatex icml2016.tex
	bibtex icml2016
	pdflatex icml2016.tex
run:
	evince icml2016.pdf
clean:
	rm *.aux
	rm *.log
	rm *.out
