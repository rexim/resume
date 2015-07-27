resume.pdf: resume.tex Makefile
	pdflatex resume.tex

resume.tex: resume.json resume.jinja2 generate_resume.py Makefile
	python ./generate_resume.py > resume.tex

.PHONY: test

test: generate_resume.py generate_resume_test.py
	python generate_resume_test.py
