resume.pdf: resume.tex Makefile
	pdflatex resume.tex

resume.tex: resume.json resume.tt generate_resume.pl Makefile
	./generate_resume.pl
