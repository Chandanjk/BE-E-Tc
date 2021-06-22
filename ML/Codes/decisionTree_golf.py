import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn import tree

def load_dataset():
    df = pd.read_csv('Dataset1.csv');

    #convert string data into float
    from sklearn.preprocessing import LabelEncoder
    lab = LabelEncoder()
    df['Outlook'] = lab.fit_transform(df['Outlook'])
    df['Temp'] = lab.fit_transform(df['Temp'])
    df['Humidity'] = lab.fit_transform(df['Humidity'])
    df['Windy'] = lab.fit_transform(df['Windy'])
    df['Play'] = lab.fit_transform(df['Play'])

    #convert to numpy
    data = df.to_numpy()   
    return data

def train_data(data):
    clf = DecisionTreeClassifier(criterion = "entropy" )
    clf.fit(data[:,0:4], data[:,4])
    return clf;

def display_image(clf):
    fn=['outlook','temperature','humidity','wind']
    cn = ['yes' , 'no']
    fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (4,4), dpi=300)
    tree.plot_tree(clf , feature_names=fn , class_names=cn, filled=True , rounded=True)
    fig.savefig('decision_tree.png')

data = load_dataset()
clf = train_data(data)
display_image(clf);