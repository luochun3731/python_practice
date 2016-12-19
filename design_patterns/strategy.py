class CashSuper:
    def accept_cash(self, money):
        return 0


class CashNormal(CashSuper):
    def accept_cash(self, money):
        return money


class CashRebate(CashSuper):
    discount = 0

    def __init__(self, ds):
        self.discount = ds

    def accept_cash(self, money):
        return money * self.discount


class CashReturn(CashSuper):
    total = 0
    ret = 0

    def __init__(self, t, r):
        self.total = t
        self.ret = r

    def accept_cash(self, money):
        if money >= self.total:
            return money - self.ret
        else:
            return money


class CashContext:
    def __init__(self, csuper):
        self.cs = csuper

    def get_result(self, money):
        return self.cs.accept_cash(money)


if __name__ == '__main__':
    money = int(input('money: '))
    strategy = {1: CashContext(CashNormal()), 2: CashContext(CashRebate(0.8)), 3: CashContext(CashReturn(300, 100))}
    ctype = int(input('type: 1 for normal, 2 for 80% discount, 3 for 300 -100\n'))
    if ctype in strategy.keys():
        cc = strategy[ctype]
    else:
        print('Undefined type, use normal mode')
        cc = strategy[1]
    print(u'you will pay: {0}'.format(str(cc.get_result(money))))