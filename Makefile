resume.pdf: resume.tex generate_resume.py Makefile
	pdflatex resume.tex

resume.tex: resume.yaml templates/*.jinja2 generate_resume.py Makefile
	python ./generate_resume.py java > resume.tex

.PHONY: test

test: generate_resume.py generate_resume_test.py templates/test.jinja2 Makefile
	python generate_resume_test.py
