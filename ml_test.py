import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()
clf = svm.SVC(gamma = 0.001,C = 100)
x,y = digits.data[:-100], digits.target[:-100]
clf.fit(x,y)
print('Prediction', clf.predict(digits.data)[-4])
plt.imshow(digits.images[-4], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()