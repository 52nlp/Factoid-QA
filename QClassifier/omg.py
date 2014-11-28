#!/usr/bin/python

import nltk
import jieba.analyse
import re
from xml.etree import ElementTree
import sys
stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr
reload(sys) 
sys.setdefaultencoding('utf8')
sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde
print sys.getdefaultencoding()
#encoding=utf8

#������ȡ����
def gender_features(word):
    return {'word': word}
#��ȡѵ�����ݣ���jieba�ؼ�����ȡ��topK=5�������޸ģ�ָ��ǰ5���ؼ���
tree = ElementTree.parse(r"D:\Program Files\Python\train.xml") 
root = tree.getroot()
featureset = []    
for Q in tree.iter('Q'):
      tags = jieba.analyse.extract_tags(Q.getchildren ()[0].text, topK=5)
      keys=" ".join(tags)
      keys.decode('utf8')
##      print keys
      types= Q.getchildren ()[1].text
      types.decode('utf8')

      featureset = featureset+[(keys,types)]
      ff = [(gender_features(n), g) for (n,g) in featureset]

##      print ff
#��ѵ������ѵ��������
classifier = nltk.NaiveBayesClassifier.train(ff)




#��ȡ�������� 
testtree = ElementTree.parse(r"D:\Program Files\Python\Sample.xml") 
testroot = tree.getroot()

#buildroot������xml��ʽ�����������stage2��ʽ�������ĵ� 
buildroot = ElementTree.Element("buildroot") 

i=0
for question in testtree.iter('question'):

      testtags = jieba.analyse.extract_tags(question.getchildren ()[0].text, topK=5)
      testkeys=" ".join(testtags)
##      print testkeys
      testtype= classifier.classify(gender_features(testkeys))
##      print testtype
  
  
#��buildroot�����ӽڵ�testquestion
      testquestion = ElementTree.SubElement(buildroot, "testquestion")  
#����testquestion�ĸ�������
      testquestion_id = ElementTree.SubElement(testquestion, "id")  
      testquestion_id.text = str(i)
      print testquestion_id.text
      testquestion_q = ElementTree.SubElement(testquestion, "q")  
      testquestion_q.text = str(question.getchildren ()[0].text.decode('utf8'))
 
      print testquestion_q.text
      testquestion_category = ElementTree.SubElement(testquestion, "category")  
      testquestion_category.text = str(testtype)
      print testquestion_category.text 
      testquestion_query = ElementTree.SubElement(testquestion, "query")  
      testquestion_query.text = str(testkeys.decode('utf8'))
      print testquestion_query.text
      testquestion_query.text = str(testkeys.encode('utf8'))
      print testquestion_query.text      
      i=i+1


#������ĵ�д��uu.xml
buildtree = ElementTree.ElementTree(buildroot)  
buildtree.write("uu.xml") 






