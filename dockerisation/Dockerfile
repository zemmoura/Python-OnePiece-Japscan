FROM python:3.9
WORKDIR /home/abdelhakim/Bureau/One-Piece/
COPY . /home/abdelhakim/Bureau/One-Piece/
RUN apt-get update && apt-get -y install git && apt-get -y install img2pdf
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN git init && git remote add One-PieceGithub git@github.com:zemmoura/Python-OnePiece-Japscan.git
CMD ["./Onepiece-dll.sh"]
