from sklearn import tree
#[height, weight, shoe size]
x= [[181,80,44], [177,70,43],[160,60,38],[166,65,40],[190,90,47],[175,64,39]]
y= ['male','female','female','female','male','female']
clf = tree.DecisionTreeClassifier()
clf=clf.fit(x,y)
prediction=clf.predict([190,70,43])
print (prediction)