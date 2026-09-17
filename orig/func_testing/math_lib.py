import random

def add(x, y):
	return x + y

def sub(x, y):
	return x - y

def div(x, y):
    return x / y

def file_add(file_name):
    total = 0
    f = open(file_name, 'r')
    for line in f:
        total = add(total, int(line.strip()))
    f.close()
    return total

def rand_norm(mean, std_dev):
    return random.gauss(mean, std_dev)
