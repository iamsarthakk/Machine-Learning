import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import lightfm

#Fetch the data
data = fetch_movielens(min_rating = 4.0)

#Create Model
model = LightFM(loss = 'warp') #warp = Weighted Approximate-Rank Pairwise

#Train the Model
model.fit(data['train'], epochs = 30, num_threads = 2)

def recommendation(model, data, user_ids):

    #no. of users and movies in training Model
    n_users, n_items = data['train'].shape

    #Generate Recommendation for each user we input

    for user_id in user_ids:

        #movies they already like
        known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]
         #tocsr(): conver data into compressed parsed row format
         #it is a subarray in our datamatrix which will be access using
         #indices attribute

        #movies our model predicts they will like
        scores = model.predict(user_id, np.arange(n_items))
        #rank them in order of most liked to least
        top_items = data['item_labels'][np.argsort(-scores)]

        #print out the results
        print("User %s" % user_id)
        print("     Known positives:")

        for x in known_positives[:3]:
            print("        %s" % x)

        print("     Recommended:")

        for x in top_items[:3]:
            print("        %s" % x)

sample_recommendation(model, data, [3, 25, 450])
© 2019 GitHub, Inc.
