import spacy
from spacy.util import minibatch, compounding

def train_spacy(nlp, train_data, n_iter=100):
    # get the pipeline
    pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]

    with nlp.disable_pipes(*other_pipes):  # only train NER
        optimizer = nlp.resume_training()

        for itn in range(n_iter):
            losses = {}
            batches = minibatch(train_data, size=compounding(4.0, 32.0, 1.001))
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(texts, annotations, sgd=optimizer, drop=0.35, losses=losses)

    return nlp

# usage
nlp = spacy.load('en_core_web_sm')  # load your base model
train_data = ...  # load your training data
nlp = train_spacy(nlp, train_data)
