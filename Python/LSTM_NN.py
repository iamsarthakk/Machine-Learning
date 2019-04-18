from __future__ import absolute_import, division, print_function

import os
from six import moves
import ssl
import tflearn
from tflearn.data_utils import *

path = "US_cities.txt"
if not os.path.isfile(path):
    context = ssl._create_unverified_context()
    moves.urllib.request.urlretrieve("https://raw.githubusercontent.com/tflearn/tflearn.github.io/master/resources/US_Cities.txt", path, context=context)

#City name max length
maxlen = 20

#Vectorize text file
X, Y, char_idx = textfile_to_semi_redundant_sequences(path, seq_maxlen = maxlen,
                 redun_Step=3)     #Function provide by tflearn to vectorize word

#Create LSTM
g = tflearn.input_data(shape = [None,maxlen,len(char_idx)])
g = tflearn.lstm(g,512, return_seq=True)   #LSTM layer
g = tflearn.dropout(g,0.5)      #To reduce overfitting
g = tflearn.lstm(g,512)
g = tflearn.dropout(g,0.5)
g = tflearn.fully_connected(g, len(char_idx),activation='sofmax')

m = tflern.SequenceGenerator(g, dictionary = char_idx, seq_maxlen = maxlen,
                                clip_gradients=5.0,
                                checkpoint_path='model_us_cities')

#Training
for i in range(40):
    seed = random_sequence_from_textfile(path, maxlen)
    m.fit(X, Y, validation_set = 0., batch_Size=128,
    n_epoch=1, run_id='us cities')
    print('Testing')
    print(m.generate(30,temperature=1.2, seq_seed = seed))
    print('Testing')
    print(m.generate(30, temperature=1.0, seq_seed=seed))
    print("-- Test with temperature of 0.5 --")
    print(m.generate(30, temperature=0.5, seq_seed=seed))
