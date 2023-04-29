# 191203040603盘景文
import os
import random
import time
class PLAY:
    play_name = ''
    play_score = 0
    chooses = ["石头", "剪刀", "布"]

    def getUserName(self):
        return self.play_name

    def setUserName(self, name):
        self.play_name = name

    def getUserScore(self):
        return self.play_score

    def setUserScore(self, score):
        self.play_score += int(score)


    def punch(self):
        pass


class PLAYer(PLAY):
    player = ''
    password = ''
    again_password = ''

    def punch(self):
        while True:
            choose = int(input("你选择出什么手势："))
            if 0 <= choose < 3:
                print(self.getUser(), "你出的是:", self.chooses[choose])
                return self.chooses[choose]
            elif choose == 3:
                return 3
            else:
                print("输入错误，请重新输入")

    def setUser(self, name):
        self.play = name

    def getUser(self):
        return self.play

    def setPassword(self, password):
        self.password = password

    def getPassword(self):
        return self.password

    def setAffirmPassword(self, affirm_Password):
        self.again_password = affirm_Password

    def getAffirmPassword(self):
        return self.again_password


class AI(PLAY):

    def punch(self):
        self.setUserName("电脑AI")
        ai = random.choice(self.chooses)
        print(self.getUserName(), "出的是:", ai)
        return ai


class Game:
    player = PLAYer()
    ai = AI()
    game_cs = 0
    win_lose = [("石头", "剪刀"), ("剪刀", "布"), ("布", "石头")]

    def index(self):
        print("    首页")
        print("1 注册账号")
        print("2 登录账号")
        print("3 排行榜")
        print("4 退出系统")
        choice = int(input("请输入您的选择："))
        if choice == 1:
            self.addPLAYer()
        elif choice == 2:
            return self.login()
        elif choice == 3:
            self.look()
        elif choice == 4:
            exit(0)
        else:
            print("输入错误！")

    def writefile(self, fileName):
        f = open(fileName, "a+",encoding="utf-8")
        return f

    def readFile(self, fileName):
        with open(fileName, "r",encoding="utf-8") as f:
            return f.readlines()

    def look(self):
        look = self.readFile("积分榜.csv")
        print("积分榜")
        for i in range(len(look)):
            k = i
            for j in range(k+1,len(look)):
                if look[j].split(",")[1] > look[k].split(",")[1]:
                    k = j;
            if(i != k):
                temp = look[i];
                look[i] = look[k];
                look[k] = temp;
        print("   用户   积分       获取时间    \n")
        for i in look:
            print("   "+i.split(",")[0]+"    "+i.split(",")[1]+"       "+i.split(",")[2])




    def addPLAYer(self):
        writeUser = self.writefile("用户数据.txt")
        user = self.readFile("用户数据.txt")
        print("注册账号")
        while True:
            self.player.setUser(input("请输入账号："))
            if len([i for i in user if self.player.getUser() == i.split(" ")[0]]) == 0:
                break
            else:
                print("账号已注册,请重新输入")
        while True:
            self.player.setPassword(input("请输入密码:"))
            self.player.setAffirmPassword(input("再次确认密码:"))
            if self.player.getPassword() == self.player.getAffirmPassword():
                break
            else:
                print("两次输入密码不一致，请重新输入")
        writeUser.write(self.player.getUser() + " " + self.player.getPassword() + "\n")
        writeUser.close()
        print("注册成功!")
        return False

    def login(self):
        user = self.readFile("用户数据.txt")
        index = 0
        for i in user:
            user[index] = tuple(i.replace("\n", "").split())
            index += 1
        print("账号登录")
        while True:
            self.player.setUser(input("账号："))
            while True:
                self.player.setPassword(input("密码："))
                self.player.setAffirmPassword(input("再次确认密码:"))
                if self.player.getPassword() == self.player.getAffirmPassword():
                    break
                else:
                    print("两次输入密码不一致，请重新输入")
            if (self.player.getUser(), self.player.getPassword()) in user:
                print("登录成功")
                break
            else:
                print("输入错误，请重新输入")
        return True

    def updateScore(self):
        score_r = None
        if not os.path.exists("积分榜.csv"):
            score_w = self.writefile("积分榜.csv")
        else:
            score_r = self.readFile("积分榜.csv")
            score_w = self.writefile("积分榜.csv")
        if score_r != None:
            score_w.write(str(self.player.getUser()) + "," + str(self.player.getUserScore()) + "," + str(
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + "\n")
        else:
            score_w.write(str(self.player.getUser()) + "," + str(self.player.getUserScore()) + "," + str(
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + "\n")

    def mainGame(self):
        while True:
            win = 0
            lose = 0
            draw = 0
            if self.index():
                print("猜拳游戏")
                print("0 石头")
                print("1 剪刀")
                print("2 布")
                print("3 返回")
                while True:
                    p = self.player.punch()
                    if p == 3:
                        self.updateScore()
                        print("游戏结果")
                        print("您进行了{}局游戏，赢{}局，输{}局，平局{}局，获得{}分\n".format((win+lose+draw),win,lose,draw,self.player.getUserScore()))
                        break
                    c = self.ai.punch()
                    if p == c:
                        print("平局")
                        draw += 1
                    elif (p, c) in self.win_lose:
                        print(self.player.getUser(), "赢了")
                        win += 1
                        self.player.setUserScore(10)
                    else:
                        print(self.player.getUser(), "输了")
                        lose += 1

if __name__ == "__main__":
    g = Game()
    g.mainGame()

