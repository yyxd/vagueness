# _*_ coding: utf-8 _*_
# @Author: Diane
# @Time  : 2018/12/4 17:06
# @File  : useNltk.py
# @Goal  测试word2vec 寻找personal相似的单词
from gensim.models import word2vec
from word2vec.my_sentences import MySentences
def w2vTrain(f_input,model_output):
    sentences = MySentences(DataDir+f_input)
    w2vmodel = word2vec.Word2Vec(sentences,min_count=MIN_COUNT,workers=CPU_NUM,size=VEC_SIZE,window=CONTEXT_WINDOW)
    w2vmodel.save(ModelDir+model_output)

DataDir = './data/'
ModelDir = './model/'
MIN_COUNT = 4
CPU_NUM = 2
VEC_SIZE = 20
CONTEXT_WINDOW = 5
f_input = 'Privacy_Sentences.txt'
model_output = 'w2v_model'

def main():
    w2vTrain(f_input,model_output)
    w2v_model = word2vec.Word2Vec.load(ModelDir+model_output)
    print(w2v_model.wv.most_similar('personal'))


if __name__ == '__main__':
    main()

