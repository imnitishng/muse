import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

import sentencepiece as spm
import numpy as np
import tensorflow_hub as hub
from data_utils import process_to_IDs_in_sparse_format


class USE_lite():

    def __init__(self):
        self.module = None
        self.input_placeholder = None
        self.encodings = None
        self.graph = tf.Graph()


    def load_persisting_model(self):
        '''
        Load the TF module and model alongwith graph to the machine's memory
        to speed up future machine inference calls.
        '''
        with tf.Session(graph = self.graph) as session:
            self.module = hub.Module("./models/use_lite")
            self.input_placeholder = tf.sparse_placeholder(tf.int64, shape=[None, None])
            self.encodings = self.module(
                inputs=dict(
                    values=self.input_placeholder.values,
                    indices=self.input_placeholder.indices,
                    dense_shape=self.input_placeholder.dense_shape))
        
            self.load_sp_model()

    
    def load_sp_model(self):
        '''
        Load the sentence piece model to run over our data
        '''
        with tf.Session(graph = self.graph) as sess:
            spm_path = sess.run(self.module(signature="spm_path"))

            self.sp = spm.SentencePieceProcessor()
            self.sp.Load(spm_path)
            print("SentencePiece model loaded at {}.".format(spm_path))


    def get_embeddings_and_corr(self, data):
        '''
        Get message embeddings and the correlation matrix 
        of all the messages.
        '''
        with tf.Session(graph = self.graph) as session:
            session.run(tf.global_variables_initializer())
            session.run(tf.tables_initializer())
            embeddings, corr = self.run_model(session, data)
        return embeddings, corr


    def run_model(self, session, messages):
        values, indices, dense_shape = process_to_IDs_in_sparse_format(self.sp, messages)

        message_embeddings = session.run(
            self.encodings,
            feed_dict={
                self.input_placeholder.values: values,
                self.input_placeholder.indices: indices,
                self.input_placeholder.dense_shape: dense_shape
            })
        
        corr = self.get_correlation(messages, message_embeddings, 90)
        return message_embeddings, corr


    def get_correlation(self, labels, features, rotation):
        corr = np.inner(features, features)
        return corr