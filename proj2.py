#! python3

from fasttext import FastVector

## Na primeira vez, tenho que usar os vetores que fiz download
## link de download: https://fasttext.cc/docs/en/pretrained-vectors.html

#pt_dictionary = FastVector(vector_file='wiki.pt.vec')
#en_dictionary = FastVector(vector_file='wiki.en.vec')

## e Ajusta-los com estas tranformações, e sarlvar num ficheiro
# pt_dictionary.apply_transform('alignment_matrices/pt.txt')
# en_dictionary.apply_transform('alignment_matrices/en.txt')
# print("Vou escrever os ficheiros:")
# pt_dictionary.export("pt_model.txt")
# print("Acabei 1")
# en_dictionary.export("en_model.txt")
# print("Acabei 2")

## Depois posso dar logo load dos modelos transformados

pt_dictionary = FastVector(vector_file='pt_model.txt')
en_dictionary = FastVector(vector_file='en_model.txt')


while True:
    print("introduza palavra a traduzir para português: ")
    valor = input()
    print("---> ", valor)
    en_vector = en_dictionary[valor]
    print("Tradução: ",pt_dictionary.translate_nearest_neighbour(en_vector))

##pt_vector = pt_dictionary["gato"]
##en_vector = en_dictionary["cat"]

##print(FastVector.cosine_similarity(en_vector, pt_vector))

#print(FastVector.cosine_similarity(pt_dictionary["gato"], en_dictionary["cat"]))

#en_vector = en_dictionary["dog"]
#print("Tradução: ",pt_dictionary.translate_nearest_neighbour(en_vector))
