import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
global data

def top():
    global data
    data = pd.read_csv('books.csv',error_bad_lines=False)
    data.sort_values(by=['average_rating','ratings_count'], inplace=True, ascending=[False,False])
    best=data[['title','average_rating','ratings_count']].head(10)
    print(best)
    #print(data[['title','average_rating','ratings_count']].head(10))

    plt.rcdefaults()
    fig, ax = plt.subplots()


    books = [t for t in best.title]
    print(books)

    
    y_pos = np.arange(len(books))
    ratings= [r for r in best.ratings_count]
    print(ratings)
    error = np.random.rand(len(books))

    ax.barh(y_pos, ratings, tick_label=y_pos,xerr=error, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(books, fontsize=5)
    ax.invert_yaxis()
    ax.set_xlabel('Ratings_count')
    ax.set_title('Best books based on Average Rating')
    
    plt.show()

def top2():
    global data
    data = pd.read_csv('books.csv',error_bad_lines=False)
    data.sort_values(by=['text_reviews_count','average_rating'], inplace=True, ascending=[False,False])
    best=data[['title','text_reviews_count','average_rating']].head(10)
    print(best)
    #print(data[['title','average_rating','ratings_count']].head(10))
    
    plt.rcdefaults()
    fig, ax = plt.subplots()


    books = [t for t in best.title]
    print(books)

    
    y_pos = np.arange(len(books))
    ratings= [r for r in best.text_reviews_count]
    print(ratings)
    

    ax.barh(y_pos, ratings, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(books, fontsize=5)
    ax.invert_yaxis()
    ax.set_xlabel('Text reviews count')
    ax.set_title('Best books based on number of reviews')
    
    plt.show()
    
    
def load():
    global data
    data = pd.read_csv('books.csv',error_bad_lines=False)
    print(data.columns)


if __name__=="__main__":
    #top()
    top2()

