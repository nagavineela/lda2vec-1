"""Training word2vec on twenty newsgroups."""

from utils.dirs import create_dirs
from models.word2vec import Word2Vec
from trainers.word2vec import Word2VecTrainer
from utils.logger import Logger

import tensorflow as tf
BASE_DIR = "/Users/jethrokuan/Documents/Code/hash-lda2vec/test/"

HPARAMS = {
    "learning_rate": 0.01,
    "embedding_size": 256,
    "vocabulary_size": 157164,
    "negative_samples": 64
}

CONFIG = {
    "summary_dir": "{}/summaries/".format(BASE_DIR),
    "checkpoint_dir": "{}/checkpoints/".format(BASE_DIR),
    "max_to_keep": 3,
    "batch_size": 50,
    "file_path": "experiments/twenty_newsgroups/train_data.csv",
    "num_epochs": 10000,
    "num_iter_per_epoch": 20,
}

create_dirs([CONFIG["summary_dir"], CONFIG["checkpoint_dir"]])

sess = tf.Session()

model = Word2Vec(CONFIG, HPARAMS)
logger = Logger(sess, CONFIG)
trainer = Word2VecTrainer(sess, model, CONFIG, logger)
model.load(sess)
trainer.train()