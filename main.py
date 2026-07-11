class main:
    def __init__(self):
        self._3d_list = []
    def main(self):
        for i in range(100):
            self._3d_list.append([])
            for j in range(100):
                self._3d_list[i].append([])
                for k in range(100):
                    self._3d_list[i][j].append(0)
        assert len(self._3d_list) == 100
        assert len(self._3d_list[0]) == 100
        assert len(self._3d_list[0][0]) == 100

if __name__ == "__main__":
    main()
    