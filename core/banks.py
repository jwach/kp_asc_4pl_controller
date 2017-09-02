import cPickle

from core import display, lighting
from config import *


class Preset:
    def __init__(self, l1, l2, l3, l4, kd):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.l4 = l4
        self.kd = kd


class Bank:
    def __init__(self, name, pa, pb, pc):
        self.name = name
        self.pa = pa
        self.pb = pb
        self.pc = pc


class BankRepository:
    def __init__(self, bank_file):
        self.bank_file = bank_file

    def get_all(self):
        self._load()
        return self.banks

    def get(self, bank_id):
        self._load()
        return self.banks[bank_id]

    def _load(self):
        with open(self.bank_file, 'rb') as f:
            self.banks = cPickle.load(f)


class BankController:  # CONSIDER LOCKING HERE!!!
    def __init__(self, bank_repository):
        self.bank_repository = bank_repository
        self.current = (1, self.bank_repository.get(1))

    def start(self):
        self._load_bank()

    def up(self):
        new_id = ((self.current[0]) % 99) + 1  # 1..99 with rollover
        new_bank = self.bank_repository.get(new_id)
        self.current = (new_id, new_bank)
        self._load_bank()

    def down(self):
        new_id = ((self.current[0] + (99 - 2)) % 99) + 1  # 1..99 with rollover
        new_bank = self.bank_repository.get(new_id)
        self.current = (new_id, new_bank)
        self._load_bank()

    def load_preset_a(self):
        if PRESET_A_LED in lighting.constant_lights:
            self._load_empty_preset()
        else:
            self._load_empty_preset()
            self._load_preset(self.current[1].pa)
            lighting.on(PRESET_A_LED)

    def load_preset_b(self):
        if PRESET_B_LED in lighting.constant_lights:
            self._load_empty_preset()
        else:
            self._load_empty_preset()
            self._load_preset(self.current[1].pb)
            lighting.on(PRESET_B_LED)

    def load_preset_c(self):
        if PRESET_C_LED in lighting.constant_lights:
            self._load_empty_preset()
        else:
            self._load_empty_preset()
            self._load_preset(self.current[1].pc)
            lighting.on(PRESET_C_LED)

    def _load_preset(self, preset):
        if preset.l1:
            lighting.on(LOOP_1)
        if preset.l2:
            lighting.on(LOOP_2)
        if preset.l3:
            lighting.on(LOOP_3)
        if preset.l4:
            lighting.on(LOOP_4)
        if preset.kd:
            lighting.on(KILL_DRY)

    def _load_empty_preset(self):
        lighting.off((LOOP_1, LOOP_2, LOOP_3, LOOP_4, KILL_DRY))
        lighting.off((PRESET_A_LED, PRESET_B_LED, PRESET_C_LED))

    def _load_bank(self):
        self._load_empty_preset()
        display.show(str('{:02d}'.format(self.current[0])) + '*' + getattr(self.current[1], 'name', ''))
