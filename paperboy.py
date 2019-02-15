# Each paperboy should have several attributes:
#
# Name
# Experience (the number of papers they've delivered)
# Earnings (amount of money they've earned)
class Paperboy:

    def __init__(self,name,exp=0,earnings=0):
        self.name = name
        self.experience = exp
        self.earnings = earnings

    # Every day, each paperboy is given a house number to start at and a house number to finish at. They get paid $0.25 for every paper they deliver and $0.50
    #for every paper over their quota. If at the end of the day they haven't met their quota, they lose $2.
#
# The minimum number of papers to deliver is 50. The quota is calculated as half of your experience added to the minimum. So the first time a paperboy makes a delivery, the quota is 50. The next time, the quote is 50 plus half the number of papers that the paperboy has delivered in the past. In this way the quota should increase after every delivery the paperboy makes.
#
# Each paperboy should have at least these methods:
#
# __str__
# quota
# This method should calculate and return the paperboy's quota for his next delivery
# deliver(self, start_address, end_address)
# This method will take two house numbers and return the amount of money earned on this delivery as a floating point number. It should also update the paperboy's experience!
# Let's assume that the start_address is always a smaller number than the end_address
# As a stretch exercise you can figure out how to ensure it still works if the above assumption isn't met!
# report
# This method should return a string about the paperboy's performance
# e.g. "I'm Tommy, I've delivered 90 papers and I've earned $38.25 so far!"

jeff = Paperboy('jeff',3,4)
print(jeff)
