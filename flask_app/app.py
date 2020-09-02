from flask import Flask, request, render_template 
import flask
import numpy as np
import pandas as pd
import pickle 

app = Flask('readmorecanlit')

df = pd.read_csv('assets/canadian_post.csv', encoding = "ISO-8859-1")

default_quantity = 1

with open(f'assets/model2.p', 'rb') as f:
    cosine_similarities = pickle.load(f)

# Credit for this codeblock: 
# http://blog.untrod.com/2016/06/simple-similar-products-recommendation-engine-in-python.html

results = {}

for idx, row in df.iterrows():
    similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
    similar_items = [(cosine_similarities[idx][i], df['id'][i]) for i in similar_indices]
    results[row['id']] = similar_items[1:]

# Functions to look up content in the dataframe

# These functions are modified from a line of code from here:
# https://github.com/nikitaa30/Content-based-Recommender-System/blob/master/recommender_system.py

def return_id_from_title(title):
 #   print(df.loc[df['title'] == title]['id'].astype(str).tolist()[0].split(' - ')[0])
    return df.loc[df['title'] == title]['id'].astype(str).tolist()[0]

    #.split(' - ')[0]

def return_title_from_id(id):
    return df.loc[df['id'] == id]['title'].tolist()[0].split(' - ')[0]

def return_author_from_id(id):
    return df.loc[df['id'] == id]['author'].tolist()[0].split(' - ')[0]

def return_details_from_id(id):
    return df.loc[df['id'] == id]['details'].tolist()[0].split(' - ')[0]


# Function to make recommendations

def recommend_by_title(title, quantity):
    print("Here are some great Canadian recommendations!")
    print("  ")
   
    bookid = return_id_from_title(title)
    bookid = int(bookid)

    recommendations = results[bookid][:quantity]
    for recommendation in recommendations:

        print(return_title_from_id(recommendation[1]))
        print(return_author_from_id(recommendation[1]))
        print(return_details_from_id(recommendation[1]))
        print('') 


@app.route('/', methods=['GET', 'POST'])

def main():
    if flask.request.method == 'GET':
        return render_template('recommender.htm')
            
    if flask.request.method == 'POST':
        favourite_book = flask.request.form['favourite_book']
        final_recommendation = recommend_by_title(favourite_book, default_quantity)
        display_title = [1,2,3]
        display_author = [4,5,6]
        display_details = [7,8,9]
        # for i in range(len(final_recommendation)):
        #     display_title.append(final_recommendation.iloc[i][0])
        #     display_author.append(final_recommendation.iloc[i][1])
        #     display_details.append(final_recommendation.iloc[i][2])

        return render_template('recommendation.htm', favourite_book=flask.request.form['favourite_book']) 
        	# template_display_title=display_title, template_display_author=display_author, template_display_details=display_details, template_favourite_book=favourite_book)


@app.route('/recommendation')

def recommendation():
	# user_input = request.args
	# data = [user_input['user_input']]

	# user_recommendations = recommend_by_title(user_input, default_quantity)
	return render_template('recommender.htm')

if __name__ == '__main__':   # means 'if script is running from terminal'
	app.run(debug=True)