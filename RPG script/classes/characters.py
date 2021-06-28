import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Character:
    def __init__(self, hp, mp, atk, df, magic, items):
        self.max_hp = hp
        self.max_mp = mp
        self.hp = hp
        self.mp = mp
        self.atk_low = atk - 10
        self.atk_high = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ['Attack', 'Magic', 'Defend', 'Item']

    def generate_dmg(self):
        return random.randrange(self.atk_low, self.atk_high)

    def generate_enemy_action(self):
        if self.get_hp() > 0.75 * self.max_hp:
            return random.choices(self.actions[:3], weights=[0.7, 0.2, 0.1], k=1)[0]
        elif 0.75 * self.max_hp > self.get_hp() > 0.5 * self.max_hp:
            return random.choices(self.actions[:3], weights=[0.6, 0.2, 0.2], k=1)[0]
        elif 0.5 * self.max_hp > self.get_hp() > 0.25 * self.max_hp:
            return random.choices(self.actions[:3], weights=[0.2, 0.5, 0.3], k=1)[0]
        else:
            return random.choices(self.actions[:3], weights=[0, 0.8, 0.2], k=1)[0]

    def generate_spell_damage(self, i):
        mg_low = int(self.magic[i]['dmg']) - 20
        mg_high = int(self.magic[i]['dmg']) + 20
        return random.randrange(mg_low, mg_high)

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def get_df(self):
        return self.df

    def reduce_mp(self, cost):
        self.mp -= int(cost)

    def get_spell_name(self, i):
        return self.magic[i]['name']

    def get_spell_mp_cost(self, i):
        return self.magic[i]['cost']

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def restore_mp(self, dmg):
        self.mp += dmg
        if self.mp > self.max_mp:
            self.mp = self.max_mp

    def choose_action(self):
        i = 1
        print(bcolors.OKCYAN + '\nActions:' + bcolors.ENDC)
        for item in self.actions:
            print(bcolors.OKCYAN + str(i) + ". " + item + bcolors.ENDC)
            i += 1

    def choose_magic(self):
        i = 1
        print(bcolors.OKCYAN + '\nSpells:' + bcolors.ENDC)
        for spell in self.magic:
            print(bcolors.OKCYAN + str(i) + "." + spell['name'], '(cost:', str(spell['cost']) + ')' + bcolors.ENDC)
            i += 1

    def choose_item(self):
        i = 1
        print(bcolors.OKCYAN + '\nItems:' + bcolors.ENDC)
        for item in self.items:
            print(bcolors.OKCYAN + str(i) + "." + item.name, '(uses:', str(item.uses) + ')' + bcolors.ENDC)
            i += 1

    def character_death(self):
        print(bcolors.FAIL + bcolors.BOLD + 'You died! Game over!' + bcolors.ENDC)

    def enemy_death(self):
        print(bcolors.OKGREEN + bcolors.BOLD + 'The enemy lies dead at your feet!',
              'Congratulations, you\'ve won!' + bcolors.ENDC)

    def status_check(self):
        return random.randrange(1, 100) > 75

    def spell_fail_check(self):
        return random.randrange(1, 100) < 51

    def command_help(self):
        print(bcolors.OKGREEN, "\nHere's an explanation of all available actions and spells: ",
              '\n1. Attack - physical attack. Damage can be mitigated by Defend action.',
              '\n2. Magic - powerful spells that either heal you, or deal unavoidable damage:',
              '\n\ta) Fireball - damaging spell that has a chance of inflicting burn for two rounds. '
              'Burning characters take damage at the start of the round.',
              '\n\tb) Wind Slash - damaging spell that has a chance of inflicting dazed.'
              'Dazed characters have 50% chance of failing next two spells.'
              '\n\tc) Ice Blast - damaging spell that has a chance of inflicting freeze.'
              'Frozen characters skip their next round.'
              '\n\td) Cure Wounds - instantly restores from 80 to 120 health points.',
              '\n\te) Restoration - spell that restores 130 - 170 health points at the start of the next two '
              'rounds.',
              '\n3. Defend - put your guard up to mitigate physical damage. Active until attacked. Spells ignore '
              'guard.',
              '\n4. Items - use one of your available items to either heal, deal damage, or restore mana:',
              '\n\ta) Small Health Potion - heals you for 250 HP.',
              '\n\tb) Big Health Potion - heals you for 350 HP.',
              '\n\tc) Essence of Vitality - fully heals you and cures all status effects.',
              '\n\td) Fire Oak Flask - deals 300 damage and has a chance to inflict burn.',
              '\n\te) Mana Potion - restores 30 points of mana.',
              '\n\tf) Soothing Balm - heals you for 100 HP and negates the burn status effect.',
              '\n\tg) Potion of CLear Mind - heals you for 100 HP and negates the dazed status effect.',
              bcolors.ENDC)
