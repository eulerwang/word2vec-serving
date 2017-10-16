# coding: utf-8

import json
import logging
import falcon
from gensim.models import Word2Vec
from config import logpath
from parse import SimilarWords, Similarity
from utils import get_model_path
from logger import build_logger


logger = build_logger(__name__, logpath)
models = {}
VALID_LANGUAGE_MODEL = ('tw', 'cn')


def get_model(lang):
    if lang not in models:
        path = get_model_path(lang)
        models[lang] = Word2Vec.load(path)
    return models[lang]

def make_response(res, data, status):
    res.body = json.dumps(data, indent=2, ensure_ascii=False)
    res.status = status
    res.append_header('Access-Control-Allow-Origin', '*')

def build_log_msg(service, *args):
    lang = args[0]
    params = ', '.join(args[1:])
    msg = 'service: {}, lang: {}, params: {}'.format(service, lang, params)
    return msg

def valid_lang_model(req, res, resource, params):
    lang = params['lang']
    if lang not in VALID_LANGUAGE_MODEL:
        msg = 'language {} is not supported.'.format(lang)
        raise falcon.HTTPBadRequest('Bad Request', msg)

def valid_vocabulary(req, res, resource, params):
    lang = params['lang']
    model = get_model(lang)
    for key in params:
        if key.startswith('text'):
            text = params[key]
            if text not in model.wv.vocab:
                msg = 'word {} not in vocabulary.'.format(text)
                logger.warning(msg)
                raise falcon.HTTPBadRequest('Bad Request', msg)


class SimilarWordsResource:
    ''' Return n most similar words of the given text.
    '''

    @falcon.before(valid_lang_model)
    @falcon.before(valid_vocabulary)
    def on_get(self, req, res, lang, text):
        try:
            model = get_model(lang)
            words = SimilarWords(model, text)
            data = words.to_json()
            status = falcon.HTTP_200
        except Exception as exp:
            data = {
                'status': '500 - Internal Server Error',
                'message': str(exp)
            }
            status = falcon.HTTP_500
        finally:
            msg = build_log_msg('similar_words', lang, text)
            logger.info(msg)
            make_response(res, data, status)


class SimilarityResource:
    ''' Return the similarity between 2 given text.
    '''

    @falcon.before(valid_lang_model)
    @falcon.before(valid_vocabulary)
    def on_get(self, req, res, lang, text1, text2):
        try:
            model = get_model(lang)
            similarity = Similarity(model ,text1, text2)
            data = similarity.to_json()
            status = falcon.HTTP_200
        except Exception as exp:
            data = {
                'status': '500 - Internal Server Error',
                'message': str(exp)
            }
            status = falcon.HTTP_500
        finally:
            msg = build_log_msg('similarity', lang, text1, text2)
            logger.info(msg)
            make_response(res, data, status)


def handle_404(req, res):
    data = {
        'status': '404 - Not Found'
    }
    status = falcon.HTTP_404
    make_response(res, data, status)
    

APP = falcon.API()
APP.add_route('/similar_words/{lang}/{text}/', SimilarWordsResource())
APP.add_route('/similarity/{lang}/{text1}/{text2}', SimilarityResource())
APP.add_sink(handle_404, '')
