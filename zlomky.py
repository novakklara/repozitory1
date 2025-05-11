#zlomky.py
#autor- Klara Novakova
from math import gcd
class Zlomek(object):
    def __init__(self, citatel, jmenovatel):
        if jmenovatel==0:
            raise ValueError("jmenovatel nesmi byt nula")
        delitel = gcd(citatel,jmenovatel)
        self.citatel=citatel/delitel
        self.jmenovatel=jmenovatel/delitel
    def __add__(self, other):
        novy_citatel=self.citatel*other.jmenovatel+other.citatel*self.jmenovatel
        novy_jmenovatel=self.jmenovatel*other.jmenovatel
        return Zlomek(novy_citatel,novy_jmenovatel)
    def __sub__(self, other):
        novy_citatel=self.citatel*other.jmenovatel-other.citatel*self.jmenovatel
        novy_jmenovatel=self.jmenovatel*other.jmenovatel
        return Zlomek(novy_citatel,novy_jmenovatel)
    def __mul__(self, other):
        novy_citatel=self.citatel*other.citatel
        novy_jmenovatel=self.jmenovatel*other.jmenovatel
        return Zlomek(novy_citatel,novy_jmenovatel)
    def __truediv__(self,other):
        novy_citatel=self.citatel*other.jmenovatel
        novy_jmenovatel=self.jmenovatel*other.citatel
        return Zlomek(novy_citatel,novy_jmenovatel)        
    def __neg__(self):
        return Zlomek(-self.citatel,self.jmenovatel)
    def __pos__(self):
        return Zlomek(+self.citatel,self.jmenovatel)
    def __abs__(self):
        return Zlomek(abs(self.citatel),abs(self.jmenovatel))
    def __str__(self):
        if self.jmenovatel==1:
            return(f"{self.citatel}")
        return (f"{self.citatel}/{self.jmenovatel}")
    


    zlomek1=Zlomek(5,8)
    zlomek2=Zlomek(12,7)
    zlomek3=zlomek2+zlomek1
    print(zlomek3)