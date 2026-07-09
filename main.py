def main():
    _3d_list = [[[0]]]
    for i in range(0,100,1):
        for j in range(0,100,1):
            for k in range(0,100,1):
                _3d_list[i][j].append(0)
            _3d_list[i].append([0])
        _3d_list.append([[0]])
if __name__ == "__main__":
    main()