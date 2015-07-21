resume.pdf: resume.tex
	pdflatex resume.tex

resume.tex: resume.json resume.tt generate_resume.pl
	./generate_resume.pl
