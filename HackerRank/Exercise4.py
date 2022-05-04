# Jumping on the Clouds: Revisited - HackerRank Problem Solving


def jumpingOnClouds(c, k):
    n = len(c)
    energy = 100 #initial energy
    i = k % n #initial jump from 0
    print(c[i] )
    energy -= c[i] * 2 + 1 #initial energy loss
    while i != 0:
        i = (i + k) % n
        energy -= c[i] * 2 + 1
        
    return energy

if __name__ == '__main__':
    k = 2
    c = [0, 1, 0, 0, 0, 1, 1, 0]

    print(jumpingOnClouds(c, k))