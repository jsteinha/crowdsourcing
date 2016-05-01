default: refdb sfig
	#node figures.js
	pdflatex main
	bibtex main

clean:
	rm main.aux main.log main.out main.bbl main.blg

refdb:
	git clone https://github.com/percyliang/refdb

sfig:
	git clone https://github.com/percyliang/sfig

run:
	go main.pdf
