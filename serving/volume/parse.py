# coding: utf-8


class SimilarWords:
    '''
    '''
    def __init__(self, model, text):
        self.doc = model.most_similar(text)


    def to_json(self):
        ''' Convert list of tuples to json format.
        '''
        return dict(self.doc)


class Similarity:
    '''
    '''
    def __init__(self, model, text1, text2):
        self.doc = model.similarity(text1, text2) 

    def to_json(self):
        return {'similarity': self.doc}
    
