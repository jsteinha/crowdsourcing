default: refdb sfig
	#node figures.js
	pdflatex main
	#bibtex main
	bibtex m
	bibtex a

clean:
	rm main.aux main.log main.out main.bbl main.blg

refdb:
	git clone https://github.com/percyliang/refdb

sfig:
	git clone https://github.com/percyliang/sfig

run:
	evince main.pdf

push:
	scp main.pdf jsteinhardt@jamie.stanford.edu:~/www/nips2016crowdsourcing.pdf
