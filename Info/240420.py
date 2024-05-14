class car () :
    on = False
    # year 
    # CP 
    # KM 
    # nr_usi 
    def start(self):
        print ("vroom vroom")
    on = True
    def __init__ (self, year, CP, KM, nr_usi):
        self.year = year
        self.CP = CP
        self.KM = KM
        self.nr_usi = nr_usi
    def pret (self):
        const = 10000
        varsta = 2024 - self.year
        aCP = self.CP // 10
        aKM = self.KM // 10000
        pret = const + (varsta * ( -0.05 * const))
        pret += (aCP * 100)## pret=pret+(aCP * 100)
        pret += aKM * (-150)## pret=pret+ aKM *(-150)
        return pret
    print (pret)
m1 = car (year = 2016, CP = 90, KM = 200000, nr_usi = 5)
m1.start ()
m1.pret ()
print (m1.pret())
    