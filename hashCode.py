import collections
import itertools
import numpy as np

class Hash:

    def __init__(self):
        _NoOfTeams=[0,0,0]

    def _setTeams(self, T2,T3,T4):
        _NoOfTeams=[T2,T3,T4]

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
        file, MT, MP, T2, T3, T4, menu = self._ToVars(fileRaw)
        self._setTeams(T2,T3,T4)
        # return file, MT, M, T2, T3, T4
        return MP, T2, T3, T4, menu


    def _ListOfIngredients(self, menu):
        menuFlat = []
        for men in menu:
            for me in men:
                menuFlat.append(me)
        return menuFlat

    def Score(self, menu):
        listOfIngredients = self._ListOfIngredients(menu)
        uniqueIngredientsCollection = collections.Counter(listOfIngredients)
        print(uniqueIngredientsCollection)
        print("No of unique ingredients", len(uniqueIngredientsCollection))

    def _ListOfUniqueIngredientsScore(self, listOfPizza):
        listOfIngredients = self._ListOfIngredients(listOfPizza)
        uniqueIngredientsCollection = collections.Counter(listOfIngredients)
        return len(uniqueIngredientsCollection)

    def pizzaComboScore(self, menu):
        T = [0, 0, 1, 2, 1]
        MD = len(menu)
        depleting_menu = menu[:]
        pizzas_t4 = []
        for i in 4,3,2:
            Scores=[]
            pizza_combos=[]
            possible_Pizza_combos = itertools.combinations(depleting_menu, i)
            for pizzaCombo in possible_Pizza_combos:
                PizzaComboScore = self._ListOfUniqueIngredientsScore(pizzaCombo)
                Scores.append(PizzaComboScore)
                pizza_combos.append(pizzaCombo)
            list_of_pizza_combos = zip(Scores,pizza_combos)
            sorted_list = sorted(list_of_pizza_combos, key=lambda pair: pair[0])
            print("possible", sorted_list)
            Scores.sort()
            print("Scores",Scores)
            print("Menu:", menu)
            for j in range(T[i]):
                pizza_combo1 = sorted_list.pop()
                print("Removing combo: ",pizza_combo1)
                for k in pizza_combo1[1]:
                    print("removing pizza",k)
                    index = depleting_menu.index(k)
                    if (index > -1):
                        depleting_menu.pop(index)
                    pizzas_t4.append(menu.index(k))
                print("Pizzas for team 4 are",pizzas_t4)
            # print("Pizza combos sorted:",pizzaCombos        
            
if __name__ == "__main__":

    filenameA = "a_example.in"
    # filenameB = "b_little_bit_of_everything.in"
    # filenameC = "c_many_ingredients.in"
    # filenameD = "d_many_pizzas.in"
    # filenameE = "e_many_teams.in"

    # filenames = [filenameA, filenameB, filenameC, filenameD, filenameE]
    filenames = [filenameA]

    for filename in filenames:
        hash = Hash()
        print(filename)
        MP, T2, T3, T4, menu = hash.DataIn(filename)
        hash.Score(menu)
        hash.pizzaComboScore(menu)
        # menuSorted, menuScoreSorted, argSort = hash.Sort(menu)
        # ress = hash.Crude(M, T2, T3, T4, menu)
        # ressToFile = hash.ResToFile(ress, filename + ".out")
        # print(ressToFile[0])
