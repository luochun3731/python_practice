class Operation:
    def get_result(self):
        pass


class Add(Operation):
    def get_result(self):
        return float(self.op1) + float(self.op2)


class Sub(Operation):
    def get_result(self):
        return float(self.op1) - float(self.op2)


class Mul(Operation):
    def get_result(self):
        return float(self.op1) * float(self.op2)


class Div(Operation):
    def get_result(self):
        try:
            result = float(self.op1) / float(self.op2)
            return result
        except ZeroDivisionError:
            print('ZeroDivisionError')
            return 0


class Undef(Operation):
    def get_result(self):
        print('Undefined operation')
        return 0


class OperationFactory:
    operation = {'+': Add(), '-': Sub(), '*': Mul(), '/': Div()}

    def create_operation(self, ch):
        if ch in self.operation:
            op = self.operation[ch]
        else:
            op = Undef()
        return op


if __name__ == '__main__':
    op = input('operator: ')
    op1 = input('op1: ')
    op2 = input('op2: ')
    factory = OperationFactory()
    cal = factory.create_operation(op)
    cal.op1 = op1
    cal.op2 = op2
    print(cal.get_result())