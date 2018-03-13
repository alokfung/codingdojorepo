class MathDojo(object):
    def __init__(self):
        self.value = 0

    def add(self, *vals):
        for val in vals:
            if type(val).__name__ == 'int':
                self.value += val
            elif type(val).__name__ == 'list' or type(val).__name__ == 'tuple':
                for inner_val in val:
                    self.value += inner_val
        return self

    def subtract(self, *vals):
        temp = 0
        for val in vals:
            if type(val).__name__ == 'int':
                temp += val
            elif type(val).__name__ == 'list' or type(val).__name__ == 'tuple':
                for inner_val in val:
                    temp += inner_val
        self.value -= temp
        return self

    def result(self):
        print self.value



md = MathDojo()

md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()
md.add([1,2,3,4],(1,2)).result()