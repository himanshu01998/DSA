def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    mid_line = (n-1) * 2
    right_line = (n-r_q) * 2
    left_line = (r_q-1) * 2
    print(mid_line, right_line, left_line)
    

if __name__ == '__main__':
    n = 8
    k = 3

    r_q = 4
    c_q = 4

    obstacles = []

    # for _ in range(k):
    #     obstacles.append(list(map(int, input().rstrip().split())))

    queensAttack(n, k, r_q, c_q, obstacles)