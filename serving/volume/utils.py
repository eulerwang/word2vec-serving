# coding: utf-8


from config import basepath

def get_model_path(lang):
    ''' Return the word2vec model path.
    '''
    path = '{}/model/{}/wiki.text.model'.format(basepath, lang)
    return path

