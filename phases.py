# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 11:11:49 2023

@author: Yen Nguyen Hai
"""
from party import Party
from miner import Miner
from utils import to_hex


class ExecuteProtocol(Miner):
    
    def __init__(self, curve, num_parties):
        super(ExecuteProtocol, self).__init__(curve, num_parties)
        
    def initial_phase(self):
        for id in range(0, self.num_parties):
            party = Party(id, self.curve, self.num_parties)
            Miner.all_P_values.append(party.P)
            Miner.all_Q_values.append(party.Q)


    def preprocess_phase(self):
        print(f"Sum of public key P: {to_hex(self.sum_of_P)}")
        print(f"Sum of public key Q: {to_hex(self.sum_of_Q)}")


    def calculate_messages_phase(self):
        for id in range(0, self.num_parties):
            party = Party(id, self.curve)
            Miner.all_M_values.append(party._calc_messages(self.curve))


    def calculate_sum_phase(self):
        print(f"Sum of all private values is: {self.V}")
