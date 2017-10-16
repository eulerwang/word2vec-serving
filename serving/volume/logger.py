# coding: utf-8

import logging


def build_logger(name, logpath):
    '''
    '''
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # create file handler
    f_handler = logging.FileHandler(logpath)
    f_handler.setLevel(logging.INFO)

    # create stream handler
    #s_handler = logging.StreamHandler()
    #s_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    f_handler.setFormatter(formatter)
    #s_handler.setFormatter(formatter)

    logger.addHandler(f_handler)
    #logger.addHandler(s_handler)
    return logger


