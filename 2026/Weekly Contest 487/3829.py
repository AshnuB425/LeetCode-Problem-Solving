#Approach 1: HashMap+ 2 Pointers
class RideSharingSystem:

    def __init__(self):
        self.a=[]
        self.b=[]
        self.e=dict()
        self.i=0
        self.j=0

    def addRider(self, riderId: int) -> None:
        self.a.append(riderId)

    def addDriver(self, driverId: int) -> None:
        self.b.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        if self.i<len(self.a) and self.j<len(self.b):
            c=self.a[self.i]
            d=self.b[self.j]
            self.e[c]=1
            self.i+=1
            self.j+=1
            return [d,c]
        else:
            return [-1,-1]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.a:
            if riderId not in self.e:
                self.a.remove(riderId)


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)
