from gensim.models import word2vec
class Mysentences(object):
    def __init__(self,fname):
        self.fname = fname
    def __iter__(self):
        for line in open(self.fname,'r'):
            yield line.split()

def w2vTrain(f_input,model_output):
    sentences = Mysentences(DataDir+f_input)
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

