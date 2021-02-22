import collections
import numpy as np
# import matplotlib.pyplot as plt
# plt.ion()


class Hash:

    def __init__(self):
        pass

    def _ReadIp(self, filename):
        with open(filename, "r") as f:
            file = f.read()
        file = file.split("\n")
        if len(file[-1]) == 0:
            file.pop(-1)
        return file

    def _ToVars(self, file):
        """
        MT: Line 1
        M: Total number of pizza
        T2: No of team of 2
        T3: No of team of 3
        T4: No of team of 4
        menu : list of list of ingredients of individual pizza
    
        """
        MT = file.pop(0)
        # print(MT)
        MT = MT.split(" ")
        if len(MT) > 4:
            MT.pop(-1)
        MT = np.int0(MT)
        M = MT[0]
        T2 = MT[1]
        T3 = MT[2]
        T4 = MT[3]
        menu = []
        for item in file:
            item = item.split(" ")
            menu.append(item[1:])
        return file, MT, M, T2, T3, T4, menu

    def DataIn(self, filename):
        fileRaw = self._ReadIp(filename)
        file, MT, M, T2, T3, T4, menu = self._ToVars(fileRaw)
        # return file, MT, M, T2, T3, T4
        return M, T2, T3, T4, menu

    def _MenuFlat(self, menu):
        menuFlat = []
        for men in menu:
            for me in men:
                menuFlat.append(me)
        return menuFlat

    def _MenScore(self, men, ingeredientsCounted):
        score = 0
        print("Pizza: ")
        for me in men:
            score = score + (1 / ingeredientsCounted[me])
            # print(me, score)
        return score

    # def _ingeredientsCounted(self, menuFlat):
    def MenuScore(self, menu):
        """
        ingredientsCounted = Total number of ingredients
        """
        menuFlat = self._MenuFlat(menu)
        ingeredientsCounted = collections.Counter(menuFlat)
        print(ingeredientsCounted)
        menuScore = []
        exit
        for men in menu:
            menuScore.append(self._MenScore(men, ingeredientsCounted))
        return menuScore

    def Sort(self, menu):
        menuScore = self.MenuScore(menu)
        argSort = np.argsort(menuScore)
        menuSorted = []
        menuScoreSorted = []
        for i in argSort:
            menuSorted.append(menu[i])
            menuScoreSorted.append(menuScore[i])
        return menuSorted, menuScoreSorted, argSort

    def ResToFile(self, ress, filename="trash"):
        resToFile = []
        resToFile.append(str(len(ress)) + "\n")
        for line in ress:
            resToFile.append(" ".join(str(item) for item in line) + "\n")
        with open(filename, "w") as f:
            f.writelines(resToFile)
        return resToFile

    def ScoreOfResFile(self, filename="trash"):
        with open(filename, "r") as f:
            file = f.readlines()
        fileList = []
        for fil in file:
            fileList.append(fil[:-1])
        if len(fileList) != int(fileList[0]):
            print("Wrong number of lines on first line")
            return 0

    def Crude(self, M, T2, T3, T4, menu):
        menuSorted, menuScoreSorted, argSort = self.Sort(menu)
        argSort = list(argSort)
        ress = []

        for t in range(T4):
            res = [4]
            for k in range(4):
                if len(argSort) >= 1:
                    res.append(argSort.pop(-1))
            if len(res) == 5:
                ress.append(res)

        for t in range(T3):
            res = [3]
            for k in range(3):
                if len(argSort) >= 1:
                    res.append(argSort.pop(-1))
            if len(res) == 4:
                ress.append(res)

        for t in range(T2):
            res = [2]
            for k in range(2):
                if len(argSort) >= 1:
                    res.append(argSort.pop(-1))
            if len(res) == 3:
                ress.append(res)
        return ress


if __name__ == "__main__":
    hash = Hash()

    filenameA = "a_example.in"
    # filenameB = "b_little_bit_of_everything.in"
    # filenameC = "c_many_ingredients.in"
    # filenameD = "d_many_pizzas.in"
    # filenameE = "e_many_teams.in"

    # filenames = [filenameA, filenameB, filenameC, filenameD, filenameE]
    filenames = [filenameA]

    for filename in filenames:
        print(filename)
        M, T2, T3, T4, menu = hash.DataIn(filename)
        menuSorted, menuScoreSorted, argSort = hash.Sort(menu)
        ress = hash.Crude(M, T2, T3, T4, menu)
        ressToFile = hash.ResToFile(ress, filename + ".out")
        print(ressToFile[0])
