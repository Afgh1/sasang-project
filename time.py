t = [1, 2, '1', '2', '3', '4']
t[2:] = 'abc'
t[0] = [1, 2]
t[1:2] = [5, 6]


if __name__ == '__main__':
    print(t)
    print(t.index(6))