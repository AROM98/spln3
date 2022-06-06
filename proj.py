#! python3


import re
import multiprocessing
from tempfile import TemporaryFile

import gensim.downloader
from gensim.models import Word2Vec, KeyedVectors, translation_matrix
from regex import P
from transvec.transformers import TranslationWordVectorizer

file = open("resultado.txt").readlines()
#print(file)

bilingue = list()
pt = list()
en = list()

for line in file:
    line = re.sub(r"\n", "", line)
    line = re.split(r" ", line)
    if (len(line) == 2):
        tuplo = (line[0], line[1])
        pt.append(line[0])
        en.append(line[1])
        bilingue.append(tuplo)

print(bilingue)

# ru_model = gensim.downloader.load("word2vec-ruscorpora-300")
# en_model = gensim.downloader.load("glove-wiki-gigaword-100")

# word_pairs = [("king", "царь_NOUN"), ("tsar", "царь_NOUN"), ("man", "мужчина_NOUN"), ("woman", "женщина_NOUN")]
# model = TranslationWordVectorizer(en_model, ru_model).fit(word_pairs)

# print(model.similar_by_word("king", 1))

# print(model.similar_by_word("царь_NOUN", 1))


# [word for word, score in model.similar_by_word("царь_NOUN")][:3]
print("fase0 - COMPLETA")

pt_model = KeyedVectors.load_word2vec_format('cbow_s50.txt', binary=False)

en_model = gensim.downloader.load("glove-wiki-gigaword-300")

transmat = translation_matrix.TranslationMatrix(pt_model, en_model, word_pairs=bilingue)
print("fase1 - COMPLETA")
transmat.train(bilingue)
print("fase2 - COMPLETA")
print('the shape of translation matrix is:', transmat.translation_matrix.shape)
print("fase3 - COMPLETA")
print(transmat.translate(["cão", "gato"], topn=3, source_lang_vec=pt_model, target_lang_vec=en_model))

with TemporaryFile("model_fileee") as fname:
    transmat.save(fname)




# bilingual_model = TranslationWordVectorizer(pt_model, en_model).fit(bilingue)

# x = pt_model.most_similar(positive=["gato"])
# print(x)

#print(bilingue)
#nomes = re.split(r"\s", nomes)

# cores = multiprocessing.cpu_count()
# w2v_model = Word2Vec(min_count=20,
#                      window=2,
#                      sample=6e-5, 
#                      alpha=0.03, 
#                      min_alpha=0.0007, 
#                      negative=20,
#                      workers=cores-1)

# w2v_model.build_vocab(en, progress_per=25)
# w2v_model.train(en, total_words=len(en), epochs=30, report_delay=1)

# w2v_model.wv.most_similar(positive=["toast"])