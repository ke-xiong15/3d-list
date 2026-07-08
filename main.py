def main():
    _3d_list = []
    for i in range(100):
        _3d_list.append([])
        for j in range(100):
            _3d_list[i].append([])
            for k in range(100):
                _3d_list[i][j].append(0)
    assert len(_3d_list) == 100
    assert len(_3d_list[0]) == 100
    assert len(_3d_list[0][0]) == 100
if __name__ == "__main__":
    main()
    