calculus-linear-maps.pdf: Appendices/*.tex Chapters/*.tex Prependices/*.tex book.tex custom_environments.tex
	texi2pdf -q -c book.tex --output=calculus-linear-maps.pdf
	open calculus-linear-maps.pdf

functions_wrapper: Wrappers/wrap_Functions.tex Chapters/Functions.tex custom_environments.tex
	mkdir -p previews
	texi2pdf -q -c Wrappers/wrap_Functions.tex --output=previews/functions_preview.pdf
	open previews/functions_preview.pdf

clean:
	if [ -e "book.log" ]; then rm book.log; fi
	if [ -e "calculus-linear-maps.pdf" ]; then rm calculus-linear-maps.pdf; fi
