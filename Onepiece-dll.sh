#!/bin/bash

echo Quel Chapitre Télécharger ?
read numero

python3 CreaScan.py $numero

dir="/home/abdelhakim/Bureau/One-Piece/chapitre"


pdf=".pdf"
cd "${dir}/${numero}"
nom_pdf="$numero$pdf"

img2pdf *.jpg -o $nom_pdf
rm *.jpg

echo Done

ls -l
git pull One-PieceGithub
git add *
git commit -m "new chapter ${numero}"
git push --set-upstream One-PieceGithub


