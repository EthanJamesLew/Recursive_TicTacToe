class TicTacToe(object):
    def __init__(self, recursions, gameNum=None):
        """
    Recursively generates games of Tic Tac Toe until to terminates based on recursion depth supplied by the user
        """
        self.tics = []
        if recursions == 1:
            temp = []
            for i in range(0, 9):
                temp.append(TicTacToe(0, i))
            self.tics = temp
        elif recursions > 1:
             temp = []
             for i in range(0, 9):
                    temp.append(TicTacToe(recursions -1, i))
             self.tics = temp

        self.win = 0
        self.gameNum = gameNum
        
        self.level = recursions

    def iterateWin(self):
        """
    Searches through the games looking for wins
        """
        t = self.tics
        if t[0].win+t[1].win+t[2].win == 3 or t[3].win+t[4].win+t[5].win == 3 or t[6].win+t[7].win+t[8].win == 3:
            self.win = 1
        elif t[0].win+t[3].win+t[6].win == 3 or t[1].win+t[4].win+t[7].win == 3 or t[2].win+t[5].win+t[8].win == 3:
            self.win = 1
        elif t[0].win+t[4].win+t[8].win == 3 or t[2].win+t[4].win+t[6].win == 3:
            self.win = 1

        if t[0].win+t[1].win+t[2].win == 30 or t[3].win+t[4].win+t[5].win == 30 or t[6].win+t[7].win+t[8].win == 30:
                self.win = 10
        elif t[0].win+t[3].win+t[6].win == 30 or t[1].win+t[4].win+t[7].win == 30 or t[2].win+t[5].win+t[8].win == 30:
                self.win = 10
        elif t[0].win+t[4].win+t[8].win == 30 or t[2].win+t[4].win+t[6].win == 30:
                self.win = 10

        if self.win != 0:
            return self.level, self.gameNum
        elif self.level > 1:
            return [i.checkWin() for i in self.tics]

    def checkWin(self):
        """
    Calls iterateWin until it collapses maximally
        """    
        for i in range(0, self.level):
            self.iterateWin()
        return self.iterateWin()
            
    def addTic(self, idx, ticVal):
        """
    Given a string or integer index, addTic assigns a win at the recursion depth
        """
        idx = str(idx)
        if len(idx) != self.level:
            print("Recursion Depth Error: Too many indices provided.")
            return
        elif self.level > 1:
            self.tics[int(idx[0])].addTic(int(idx[1:]),ticVal) 
        else:
            self.tics[int(idx)].win = ticVal
    def getStates(self):
        if self.level > 1:
            return [i.getStates() for i in self.tics]
        else:
            return [self.tics[j].win for j in range(0, len(self.tics))]
        
    def __str__(self):
        return str(self.tics)
