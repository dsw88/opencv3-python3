import pickle

with open('pkmn_index', 'rb') as f:
    data = pickle.load(f)
    print(data)

