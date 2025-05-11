#zlomky.py
#autor- Klara Novakova
from math import gcd
class Zlomek:
    def __init__(self, citatel, jmenovatel):
        if jmenovatel==0:
            raise ValueError("jmenovatel nesmi byt nula")
        delitel = gcd(citatel,jmenovatel)
        self.citatel=citatel//delitel
        self.jmenovatel=jmenovatel//delitel
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
    


zlomek1=Zlomek(1,2)
zlomek2=Zlomek(2,3)
zlomek3=zlomek2+zlomek1
zlomek4=zlomek2-zlomek1
zlomek5=zlomek2*zlomek1
zlomek6=zlomek2/zlomek1
zlomek7=abs(zlomek4)
print(zlomek3)
print(zlomek4)
print(zlomek5)
print(zlomek6)
print(zlomek7)