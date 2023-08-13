# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 11:23:43 2023

@author: Yen Nguyen Hai
"""

from tinyec import registry
from miner import Miner
from phases import ExecuteProtocol
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-n', '--number-parties', default=100, 
                         type=int, required=False, help="Numbers of parties")

parser.add_argument('-c', '--curve', default='brainpoolP256r1', 
                         type=str, required=False, help="Type of curve")

args = parser.parse_args()

curve = registry.get_curve(args.curve)
num_parties = args.number_parties  # Number of parties

miner = Miner(curve, num_parties)
execution = ExecuteProtocol(curve, num_parties)

execution.initial_phase()
execution.preprocess_phase()
execution.calculate_messages_phase()
execution.calculate_sum_phase()


print("DONE")


