import plotly.graph_objects as go
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import plotly.express as px
import pandas as pd

def foo():

    x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
    y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
    names = list('abcdefghij')
    data = list(zip(x, y))

    kmeans = KMeans(n_clusters=3)
    kmeans.fit(data)

    df = pd.DataFrame({"x":x,"y":y,'labels':kmeans.labels_,'names':names})
    color_map = {0:'r',1:'g',2:'b'}
    df['colors'] = df['labels'].map(color_map)
    print(df)

    fig = px.scatter(df, x="x", y="y", hover_data=['names'], color="colors")
    fig.show()


    #plt.scatter(x, y, c=kmeans.labels_)
    #plt.show()



if __name__=='__main__':
    print('start...')
    foo()
    print ("END")