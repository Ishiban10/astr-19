# Code Journal #1 - Prompt #4

class Animal:
    def __init__(self, lenArm, lenLeg, numEyes, tail, furry):
        self.lenArm = lenArm
        self.lenLeg = lenLeg
        self.numEyes = numEyes
        self.tail = tail
        self.furry = furry

    def description(self):
        return f"Length of arms: {self.lenArm} cm\nLength of legs: {self.lenLeg} cm\nNumber of eyes: {self.numEyes}\nDoes it have a tail?: {self.tail}\nIs it furry?: {self.furry}"


A = Animal(22.5, 33.4, 3, True, False)
print(A.description())

