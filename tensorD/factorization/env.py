# Created by ay27 at 17/6/5
import tensorflow as tf


class Environment(object):
    def __init__(self, data_provider, summary_path=None, is_distributed=False, cluster_spec=None):
        self._data_provider = data_provider
        self._is_distributed = is_distributed
        self._sum_path = summary_path

    @property
    def is_distributed(self):
        return self._is_distributed

    @property
    def is_master(self):
        # TODO
        return False

    def data_queue(self):
        return self._data_provider.data_queue()

    def full_data(self):
        return self._data_provider.full_data()

    @property
    def summary_path(self):
        return self._sum_path

    @property
    def sess(self):
        return tf.Session()
