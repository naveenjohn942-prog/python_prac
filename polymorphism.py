class PG:
    def pro(self):
        print("PG PORGRAMS ARE HERE")
    def classes(self):
        print("PG CLASSES ARE HERE")
class UG:
    def pro(self):
        print("UG PROGRAMS ARE HERE")
    def classes(self):
        print("UG CLASSES ARE HERE")

a=PG()
b=UG()
for g in (a,b):
    g.pro()
    g.classes()
