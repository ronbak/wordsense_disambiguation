# Wordsense Disambiguation

Word sense disambiguation (WSD) is the task of determining which sense of an ambiguous word is being used in a 
particular context. The solution to this problem impacts other NLP-related problems such as machine translation
and document retrieval.

The standard WSD task has two variants: "lexical sample" and "all words". The former comprises disambiguation the
occurrences of a small sample of target words which where previously selected, while in the latter all the words
in a piece of running text need to be disambiguated. In this assignment we will be working on the lexical sample
task.

In the machine learning part, we apply several classifier(KNN, SVM) in the disambiguation task. Given a set of data,
usually represented as vectors, and several classes, predict which class each vector belongs to. To solve the 
problem, we will first train a classifier using some data whose classes have already been given. Then we will predict
the classes of a unlabeled data with the classifier we just trained.
