from ast import literal_eval
from pprint import pprint

class Read:
    def __init__(self, inp):
        self.f = open("sys\\var.oms", "r", encoding="utf_8")
        self.r = self.f.readlines()#                             リスト
        self.inp = inp

    def run(self):
        inp = self.inp
        v = Vpri()
        v.run(inp)
        self.f.close()


class Vpri:
    def run(self, inp):
        fil_data = open("sys\\var.oms", encoding="utf_8")
        cov = open("sys\\varconp.oms", "w", encoding="utf_8")
        self.inp = inp
        for line in fil_data:
            line = line.replace("{", "").replace("}", "").replace("'", "")
            line = line.rstrip()
            s = line.split(":")[0]
            cov.write(s + ":" + self.inp +"\n")
            if s == self.inp:
                print(line.split(":")[-1])
                break
            else:
                print(line.split(":")[-1])
                continue
        fil_data.close()
        cov.close()
"""
r = Read()
r.run()
"""