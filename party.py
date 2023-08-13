"""
Created on Sat Aug 12 18:06:57 2023

@author: Yen Nguyen Hai
"""
import random
from utils import rand_prime
from miner import Miner


class Party(Miner):
    """
    Class Party with the following parameters:
    - id: identification, numerical order of a party
    - v: private value used to calculate a preserved sum
    - p, q: private keys randomly selected by the user
    - P, Q: public keys
    - M: intermediary messages
    """

    def __init__(self, id, *arg):
        super().__init__(*arg)
        self.id = id
        self.v = random.randint(0, 50)
        self.p = rand_prime()
        self.q = rand_prime()
        self.P = self._calc_public_key_P()
        self.Q = self._calc_public_key_Q()
        self.M = self._calc_messages()


    def _calc_public_key_P(self):
        return self.p * self.curve.g
        

    def _calc_public_key_Q(self):
        return self.q * self.curve.g


    def _calc_messages(self):
        return (self.v * self.curve.g + self.q * self.sum_of_P - self.p * self.sum_of_Q)
