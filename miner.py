# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 10:59:34 2023

@author: Nguyen Hai Yen
"""

class Miner:
    '''
    In an ideal world, we have a miner that has all public information of parties
    - curve: elliptic curve that we use for SMS protocol
    Miner has the following information about parties:
        - num_parties: number of parties participating in the protocol
        - all_P_values, all_Q_values, all_M_values: these are all public
        information of parties
        - sum_of_P: sum of all values in all_P_values array
        - sum_of_Q: sum of all values in all_Q_values array
        - sum_of_M: sum of all values in all_M_values array
        - V: result of the protocol, which is the sum of all private value v 
        of parties.
    '''
    def __init__(self, curve, num_parties):
        self.curve = curve
        self.num_parties = num_parties
        self.all_P_values = []
        self.all_Q_values = []
        self.all_M_values = []
        self.sum_of_P = None
        self.sum_of_Q = None
        self.sum_of_M = self._calculate_sum_messages()
        self.V = self._find_sum_private_value()


    def _sum_public_key_P(self):
        sum_P = self.curve.g
        for P in self.all_P_values:
            sum_P = sum_P + P
        self.sum_of_P = sum_P - self.curve.g
        return self.sum_of_P


    def _sum_public_key_Q(self):
        sum_Q = self.curve.g
        for Q in self.all_Q_values:
            sum_Q = sum_Q + Q
        self.sum_of_Q = sum_Q - self.curve.g
        return self.sum_of_Q


    def _calculate_sum_messages(self):
        sum_M = self.curve.g
        for M in self.all_M_values:
            sum_M = sum_M + M
        return sum_M - self.curve.g


    def _find_sum_private_value(self):
        for v in range(self.num_parties):
            if v * self.curve.g == self.sum_of_M:
                return v
