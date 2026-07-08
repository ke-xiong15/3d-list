def main():
    _3d_list = [[[0]]]
    for i in range(0,100,1):
        for j in range(0,100,1):
            for k in range(0,100,1):
                _3d_list[i][j].append(0)
def __test__3d_list():
    assert len(_3d_list) == 100
    assert len(_3d_list[0]) == 100
    assert len(_3d_list[0][0]) == 100
if __name__ == "__main__":
    main()
    __test__3d_list()