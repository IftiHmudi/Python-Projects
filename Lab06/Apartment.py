class Apartment:
    def __init__(self, rent, metersFromUCSB, condition):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition

    def getRent(self):
        return self.rent
    def getMetersFromUCSB(self):
        return self.metersFromUCSB
    def getCondition(self):
        return self.condition

    def getApartmentDetails(self):
        return "(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {}".format(self.getRent(), self.getMetersFromUCSB(), self.condition)

    def __lt__(self,rhs):
        
        if self.getRent() < rhs.getRent():
            return True
        if (self.getRent() == rhs.getRent()) and (self.getMetersFromUCSB() < rhs.getMetersFromUCSB()):
            return True
        if (self.getRent() == rhs.getRent()) and (self.getMetersFromUCSB() == rhs.getMetersFromUCSB()):
            if self.getCondition().upper() == "EXCELLENT":
                x= 3
            elif self.getCondition().upper() == "AVERAGE":
                x = 2
            elif self.getCondition().upper() == "BAD":
                x = 1
            if rhs.getCondition().upper() == "EXCELLENT":
                y= 3
            elif rhs.getCondition().upper() == "AVERAGE":
                y = 2
            elif rhs.getCondition().upper() == "BAD":
                y = 1

            return x > y

        return False

    def __gt__(self,rhs):
        '''
        the < operator will return True for 
        Apartment1 < Apartment2 
        if Apartment1 is better than Apartment2
        '''
        if self.getRent() > rhs.getRent():
            return True
        if (self.getRent() == rhs.getRent()) and (self.getMetersFromUCSB() > rhs.getMetersFromUCSB()):
            return True
        if (self.getRent() == rhs.getRent()) and (self.getMetersFromUCSB() == rhs.getMetersFromUCSB()):
            if self.getCondition().upper() == "EXCELLENT":
                x= 3
            elif self.getCondition().upper() == "AVERAGE":
                x = 2
            elif self.getCondition().upper() == "BAD":
                x = 1
            if rhs.getCondition().upper() == "EXCELLENT":
                y= 3
            elif rhs.getCondition().upper() == "AVERAGE":
                y = 2
            elif rhs.getCondition().upper() == "BAD":
                y = 1

            return x < y

        return False

    def __eq__(self, rhs):
        if (self.getRent() == rhs.getRent()) and (self.getMetersFromUCSB() == rhs.getMetersFromUCSB()) and (self.getCondition() == rhs.getCondition()):
            return True
        else:
            return False