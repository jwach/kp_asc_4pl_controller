class Preset:
    def __init__(self, l1=False, l2=False, l3=False, l4=False, kd=False):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.l4 = l4
        self.kd = kd


class Bank:
    def __init__(self, name, pa, pb, pc):
        if name:
            if len(name) > 10:
                raise Exception('Bank name cannot be longer than 10 characters')
            self.name = name.upper()
        self.pa = pa
        self.pb = pb
        self.pc = pc


class BankRepository:
    def __init__(self, banks=None):
        if banks is None:
            self.banks = self._get_empty_banks()
        else:
            self.banks = banks

    def _get_empty_banks(self):
        banks = {}
        for i in range(1, 100):
            banks[i] = (Bank(None,
                             Preset(False, False, False, False, False),
                             Preset(False, False, False, False, False),
                             Preset(False, False, False, False, False)))
        banks[5] = Bank('dupa', Preset(True, False, False, True), Preset(), Preset())
        return banks

    def get_all(self):
        return self.banks

    def get(self, bank_id):
        return self.banks[bank_id]

    def update(self, bank_id, bank):
        self.banks[bank_id] = bank
