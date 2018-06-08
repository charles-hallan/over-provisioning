#CoS_i = CoS(MRth, Brv, Bu)

from nacm import *
from cos import CoS

class Link:                                         # Classe de enlace (link), que possui os dados das classes de servico e seus atributos principais
    def __init__(self):
        self.cos_list=[]
        self.cos_a = CoS(20.0, 5.0, 0.0)            # Classes de servico
        self.cos_b = CoS(20.0, 5.0, 0.0)
        self.cos_c = CoS(20.0, 5.0, 0.0)
        self.cos_d = CoS(20.0, 5.0, 0.0)

        self.cos_list.append(self.cos_a)
        self.cos_list.append(self.cos_b)
        self.cos_list.append(self.cos_c)
        self.cos_list.append(self.cos_d)

        self.stats_a = {}                           # Tabela de estados
        self.stats_b = {}
        self.stats_c = {}
        self.stats_d = {}

    def add_session(self, cos, resv, id):
        if cos == "A":
            self.stats_a[str(id)]=[resv]
        if cos == "B":
            self.stats_b[str(id)]=[resv]
        if cos == "C":
            self.stats_c[str(id)]=[resv]
        if cos == "D":
            self.stats_d[str(id)]=[resv]

    def del_session(self, cos, id):
        if cos == "A":
            del stats_a[id]
        if cos == "B":
            del stats_b[id]
        if cos == "C":
            del stats_c[id]
        if cos == "D":
            del stats_d[id]


link0 = Link()
for i in range(1, 5):
    require(link0, link0.cos_b, 3.0)
    link0.add_session("B", 3.0, i)

for i in range(1, 5):
    require(link0, link0.cos_c, 3.0)
    link0.add_session("C", 3.0, i)

for i in range(1, 8):
    require(link0, link0.cos_a, 3.0)
    link0.add_session("A", 3.0, i)

print link0.cos_a.mrth
print link0.cos_a.brv
print link0.cos_a.bu
print
print link0.cos_b.mrth
print link0.cos_b.brv
print link0.cos_b.bu
print
print link0.cos_c.mrth
print link0.cos_c.brv
print link0.cos_c.bu
print
print link0.cos_d.mrth
print link0.cos_d.brv
print link0.cos_d.bu
