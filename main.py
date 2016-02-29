#!/usr/bin/python
from __future__ import division
import xml.dom.minidom
import nltk
from collections import Counter
from sklearn import svm
from sklearn import neighbors
import math

def context_vector():
    dom = xml.dom.minidom.parse('data/English-train.xml')
    root = dom.documentElement
    lexelt = dom.getElementsByTagName('lexelt')
    VECtor = []
    sense_ID = []
    for S in lexelt:
           Sen = []
           sen = []
           dic = {}
           senseid = []
           Vector = []
           instance = S.getElementsByTagName('context')
           Instance = S.getElementsByTagName('instance')
           for Ins in Instance:
                  answers = Ins.getElementsByTagName('answer')
                  sense = str((answers[0]).getAttribute('senseid'))
                  senseid.append(sense)
           sense_ID.append(senseid)
           for i in xrange(0, len(instance)):
                  s1 = []
                  s2 = []
                  context = instance[i]
                  line1 = nltk.word_tokenize(str(context.firstChild.data))
                  line2 = nltk.word_tokenize(str(context.lastChild.data))
                  if len(line1) >= 10:
                         bound1 = len(line1) - 11
                  if len(line1) < 10:
                         bound1 = -1
                  if len(line2) >= 10:
                         bound2 = 10
                  if len(line2) < 10:
                         bound2 = len(line2)
                  for j in xrange(len(line1) - 1, bound1, -1):
                         s1.append(line1[j])
                  for j in xrange(0, bound2):
                         s2.append(line2[j])
                  s = s1 + s2
                  sen.append(s)
                  Sen = Sen + s
           Sentence = set(Sen)
           for word in Sentence:
                  dic[word] = 0
           for st in sen:
                  vector = []
                  for k in dic.keys():
                         if k in (Counter(st)).keys():
                               vector.append((Counter(st))[k])
                         if k not in (Counter(st)).keys():
                               vector.append(0)
                  Vector.append(vector)
           VECtor.append(Vector)
    return VECtor, sense_ID

def svm_clf_training(vector, senseid):
    prediction = []
    count = 0
    base = 0
    for i in xrange(0, len(vector)):
           pred_result = []
           clf = svm.LinearSVC()
           clf.fit(vector[i], senseid[i])
           for j in vector[i]:
                  pred_result.append(clf.predict(j))
           prediction.append(pred_result)
    for i in xrange(0, len(senseid)):
           for j in xrange(0, len(senseid[i])):
                  if senseid[i][j] == prediction[i][j]:
                         count += 1
                         base += 1
                  if senseid[i][j] != prediction[i][j]:
                         base += 1
    accuracy = float(count) / float(base)
    print accuracy
    return prediction

def kn_clf_training(vector, senseid):
    prediction = []
    count = 0
    base = 0
    for i in xrange(0, len(vector)):
           pred_result = []
           clf = neighbors.KNeighborsClassifier()
           clf.fit(vector[i], senseid[i])
           for j in vector[i]:
                  pred_result.append(clf.predict(j))
           prediction.append(pred_result)
    for i in xrange(0, len(senseid)):
           for j in xrange(0, len(senseid[i])):
                  if senseid[i][j] == prediction[i][j]:
                         count += 1
                         base += 1
                  if senseid[i][j] != prediction[i][j]:
                         base += 1
    accuracy = float(count) / float(base)
    print accuracy 
    return prediction  

def vec_output(vector, filename):
    outfile = open(filename, 'w')
    for vec in vector:
        outfile.write(str(vec) + '\n')
    outfile.close()


def main():
    vec, senseid = context_vector()
    vec_output(vec, 'vec_output.txt')
    vec_output(senseid, 'senseid_output.txt')
    svm_clf_training(vec, senseid)
    kn_clf_training(vec, senseid)

if __name__ == "__main__": main()
                               
                         

