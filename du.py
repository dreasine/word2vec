import jieba
import codecs
from gensim.corpora import WikiCorpus
from collections import defaultdict
import operator
default_dict = defaultdict(int)
output = codecs.open('wiki_words.text', 'w',encoding='utf-8')
lists = []
stopwords = ['你','我']
with open('wiki_result.txt', 'r', encoding='utf-8') as text:
    for word in text:
        word = word.split('\t')
        #print (word[1])
        if int(word[1]) >= 300000 :
            stopwords.append(word[0])

s = ''
jieba.set_dictionary('dict.txt.big.txt')
# wiki = WikiCorpus('zhwiki-20171103-pages-articles.xml.bz2', lemmatize=False, dictionary={})
#print (wiki)
#print (wiki.get_texts())
# for text in wiki.get_texts():
with open('wiki.zh.text.fan', 'r', encoding='utf-8') as text:
    for word in text:
        seg_list = jieba.cut("".join(word), cut_all = False)
        for item in seg_list:
            if (item in stopwords):
                continue
            else:
                if item >= u'\u4e00' and item <= u'\u9fa5':
                    default_dict[item] += 1
                    output.write(" ".join(item) + '\n')

# sentences = wiki.get_texts()
    #print text
# ci = ' '.join(sentences)
# seg_list = jieba.cut(sentences, cut_all=False)
# output.write(" ".join(seg_list))
# r = " ".join(seg_list)
# print("this", seg_list)
# for word in seg_list:
#     # if (word >= u'\u0021' and word <= u'\u002F'):
#     default_dict[word] += 1
#     print(word)
    # print(r)
    # for word in r:
    #     if(word >= u'\u0021' and word <= u'\u002F'):
    #         default_dict[word] += 1
    #         print(word)
print ('ok')
a = sorted(default_dict.items(), key=operator.itemgetter(1), reverse=True)
# with open('wiki_result.txt', 'w', encoding='utf-8') as wf:
#     for i, j in a:
#         wf.write(i+'\t'+str(j)+'\n')
print('ok')
print(a[:100])
