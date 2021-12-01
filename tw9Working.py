from sklearn.model_selection import
     train_test_split
from sklearn.neighbours import.kneighbourclassifier
from sklearn import dataset's
  iris=dataset's.load_iris()
print("Iris dataset loaded")
x=train.x_test.y_train.y_test=train_test_split(iris.data.iris.target.test_size=0.1)
print("dataset is split into training and testing")
print("dataset is split into training and testing")
print("dataset is split into training and testing")
print("size of training data and its label",x_train.shape,y_train.shape)
print("size of testing data and its label",x_test.shape.y_test.shape)
for i in range 
         (len(iris.target_names)):
                                 print("label",i,"-"str(iris.target_names[i]))
                                 classifier.fit(x_train,y_train)
                                 y_pred=classifier.predict(x_test)
                                 print("result of classification using k-nn with k=1")
 for r in range(0,len(x_test)):
                               print("sample".",str(x_test[r],"
                                                    actual label:",str(y_test[r])
                                                    "predicted_label:",str(y_pred[r])
                                                    print ("classification"
                                                           Accuracy:",classifier.score(x.test.y_test))))


