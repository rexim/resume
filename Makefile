resume.pdf: resume.tex Makefile
	pdflatex resume.tex

resume.tex: resume.json resume.jinja2 generate_resume.py Makefile
	./generate_resume.py > resume.tex
