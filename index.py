import random

def train_test_split(data, test_size=0.2, random_seed=None):
    
    if random_seed is not None:
        random.seed(random_seed)
    

    shuffled_data = data[:]
    random.shuffle(shuffled_data)
    
    split_idx = int((1 - test_size) * len(shuffled_data))
    
    training_set = shuffled_data[:split_idx]
    testing_set = shuffled_data[split_idx:]
    
    return training_set, testing_set

# Example :
dataset = [(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E'), (6, 'F'), (7, 'G'), (8, 'H'), (9, 'I'), (10, 'J')]

# Split the dataset with 20% for testing
train_set, test_set = train_test_split(dataset, test_size=0.2, random_seed=42)

print("Training Set:", train_set)
print("Testing Set:", test_set)
