#down:
#	curl -o entirel https://raw.githubusercontent.com/AROM98/ipln1/master/entirel
#	chmod 755 entirel

#bin:
#	sudo mv entirel /usr/local/bin/

install:
	pip3 install transvec
	pip install --upgrade gensim
#	pip3 install -U spacy
#	python3 -m spacy download pt_core_news_sm
#	python3 -m spacy download en_core_web_sm

#entirel-install: down bin install

#entirel-remove:
#	sudo rm /usr/local/bin/entirel