# Word2Vec serving
Docker running [Falcon](https://falconframework.org/) with [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) server serving [Gensim](https://radimrehurek.com/gensim/) word2vec service.

## Getting started
1. Put the trained word2vec model under the model/{language} directory.
2. Add the {language} to VALID\_LANGUAGE\_MODEL variable in server.py.
3. Change your path setting in utils.py.
4. Assign service port number in docker-compose.yml. (default: 5010)


### Setup
```
docker-compose up -d
```

### Usage
Curl command

Get the n most similar words of given word.

```
curl http://{your-ip-address}:{your-port}/similar_words/{lang}/{text}
```

Calculate the similarity between 2 words.

```
curl http://{your-ip-address}:{your-port}/similarity/{lang}/{text1}/{text2}
```

### Requirements
- falcon
- numpy
- scipy
- gensim
- uwsgi

