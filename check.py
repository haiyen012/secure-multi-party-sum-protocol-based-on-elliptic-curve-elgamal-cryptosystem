# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 20:06:45 2023

@author: Admin
"""
from miner import Miner
from party import Party


class Check(Miner):
    def check_sum_with_and_without_protocol(self):
        sum_private_value = 0
        
        for id in range(0, self.num_parties):
            party = Party(self.curve, id)
            print(f"v{party.id}: {party.v}")
            sum_private_value = sum_private_value + party.v
        
        if sum_private_value == self.V:
            print("Sum that calculated by protocol is equal to sum of private value.")
        else:
            print("False")