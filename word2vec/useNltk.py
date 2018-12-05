# _*_ coding: utf-8 _*_
# @Author: Diane
# @Time  : 2018/12/4 17:06
# @File  : useNltk.py
# @Goal  使用nltk去掉停用词等
from nltk.corpus import stopwords
from gensim.models import word2vec
from word2vec.my_sentences import MySentences

DataDir = './data/'
ModelDir = './model/'
MIN_COUNT = 4
CPU_NUM = 2
VEC_SIZE = 20
CONTEXT_WINDOW = 5
f_input = 'Privacy_Sentences.txt'
model_output = 'w2v_model'

StopWords = stopwords.words('english')

#去除停用词
def w2vTrain_removeStopWords(f_input, model_output):
    sentences = list(MySentences(DataDir + f_input))
    for idx, sentence in enumerate(sentences):
        sentence = [w for w in sentence if w not in StopWords]
        sentences[idx] = sentence
    w2v_model = word2vec.Word2Vec(sentences, min_count=MIN_COUNT, workers=CPU_NUM, size=VEC_SIZE)
    w2v_model.save(ModelDir + model_output)


def main():
    w2vTrain_removeStopWords(f_input, model_output)
    w2v_model = word2vec.Word2Vec.load(ModelDir + model_output)
    print(w2v_model.wv.most_similar('information'))


if __name__ == '__main__':
    main()
