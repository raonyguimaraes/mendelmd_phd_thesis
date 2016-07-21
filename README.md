This is the git repository of my phd-thesis in Bioinformatics.

Mendel,MD: Desenvolvimento e validação de uma ferramenta online para análise de exomas humanos e investigação de doenças Mendelianas

Requirements
************

On Ubuntu
=========

apt-get install texlive-publishers texlive-lang-portuguese texlive-latex-extra texlive-fonts-recommended lmodern texlive-fonts-extra

On Arch Linux
=============

pacman -S texlive-latexextra texlive-fontsextra
yaourt -S abntex2 latex-enumitem minted

Add to build with pdflatex the flag "--shell-escape" in order to build it correctly!
Kile -> Settings -> Build -> PDFLATEX
-interaction=nonstopmode --shell-escape '%source'

Always run pdflatex twice to update the indexes.
