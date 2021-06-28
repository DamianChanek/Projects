import random
from classes.characters import Character
from classes.game_info import bcolors
from classes.inventory import Item

# create spells #
magic = [{'name': 'Fireball',
          'cost': 10,
          'dmg': 60,
          'effect': 'burn'},
         {'name': 'Wind Slash',
          'cost': 10,
          'dmg': 60,
          'effect': 'daze'},
         {'name': 'Ice Blast',
          'cost': 10,
          'dmg': 60,
          'effect': 'freeze'},
         {'name': 'Cure Wounds',
          'cost': '10',
          'dmg': '150'},
         {'name': 'Restoration',
          'cost': '15',
          'dmg': '100'}]

# create items #
sh_potion = Item('Small Health Potion', 170, 2)
bh_potion = Item('Big Health Potion', 220, 1)
full_heal = Item('Essence of Vitality', 350, 1)
mana_potion = Item('Mana Potion', 40, 3)
grenade = Item('Fire Oak Flask', 300, 1)
heal_burn = Item('Soothing Balm', 100, 3)
heal_dazed = Item('Potion of Clear Mind', 50, 3)

player_items = [sh_potion, bh_potion, full_heal, grenade, mana_potion, heal_burn, heal_dazed]

# create battle participants #
player = Character(350, 65, 60, 55, magic, player_items)
enemy = Character(2000, 130, 60, 55, magic, None)

# game-on flag #
run = True
# round counter #
round_counter = 1

# game flags for multi-round effects #
restoration_1 = False
restoration_2 = False
player_defended = False
enemy_defended = False
enemy_burn = False
enemy_dazed = False
enemy_frozen = False
player_burn = False
player_dazed = False
player_frozen = False
enemy_burn_2 = False
enemy_dazed_2 = False
player_burn_2 = False
player_dazed_2 = False

# welcome message #
print(bcolors.OKBLUE + bcolors.BOLD + '\nWelcome to my RPG battle script! The goal of the game is simple: defeat the '
      'enemy!' + '\nIn your arsenal you have a wide variety of physical attacks, spells and items. ' +
      '\nFor more details about available actions type "help". Type "quit" to turn the game off.' +
      '\nGOOD LUCK!' + bcolors.ENDC)

print(bcolors.FAIL + bcolors.BOLD + '\n\nAN ENEMY ATTACKS!' + bcolors.ENDC)

# game begins #
while run:
    print('========================',
          bcolors.OKCYAN, bcolors.BOLD, '\nRound', round_counter, 'begins!', bcolors.ENDC)

    # restoration checks #
    if restoration_1:
        print(bcolors.OKBLUE, '\nYour restoration spell is active.', bcolors.ENDC)
        heal_dmg = player.generate_spell_damage(4)
        player.heal(heal_dmg)
        print(bcolors.OKBLUE + 'It heals you for ' + str(heal_dmg) + ' health points.' + bcolors.ENDC)
        restoration_1 = False

    elif not restoration_1:
        if restoration_2:
            print(bcolors.OKBLUE, '\nYour restoration spell is active.', bcolors.ENDC)
            heal_dmg = player.generate_spell_damage(4)
            player.heal(heal_dmg)
            print(bcolors.OKBLUE + 'It heals you for ' + str(heal_dmg) + ' health points.' + bcolors.ENDC)
            restoration_2 = False
            print(bcolors.WARNING + '\nYour restoration spell wanes... '
                                    'You will not longer be healed at the beginning of next turn.' + bcolors.ENDC)

    # enemy burn checks #
    if enemy_burn:
        enemy_burn_dmg = enemy.generate_spell_damage(0)
        enemy.take_dmg(enemy_burn_dmg)
        print(bcolors.OKGREEN + 'The enemy is burning! It takes ' + str(enemy_burn_dmg)
              + ' points of damage!' + bcolors.ENDC)
        enemy_burn = False

    elif not enemy_burn:
        if enemy_burn_2:
            enemy_burn_dmg = enemy.generate_spell_damage(0)
            enemy.take_dmg(enemy_burn_dmg)
            print(bcolors.OKGREEN + 'The enemy is burning! It takes ' + str(enemy_burn_dmg)
                  + ' points of damage!' + bcolors.ENDC)
            enemy_burn_2 = False

    # player burn checks #
    if player_burn:
        player_burn_dmg = player.generate_spell_damage(0)
        player.take_dmg(player_burn_dmg)
        print(bcolors.FAIL + 'You\'re burning! You take ' + str(player_burn_dmg)
              + ' points of damage!' + bcolors.ENDC)
        player_burn = False

    elif not player_burn:
        if player_burn_2:
            player_burn_dmg = player.generate_spell_damage(0)
            player.take_dmg(player_burn_dmg)
            print(bcolors.FAIL + 'You\'re burning! You take ' + str(player_burn_dmg)
                  + ' points of damage!' + bcolors.ENDC)
            player_burn_2 = False

    # player frozen check #
    if player_frozen:
        print(bcolors.FAIL + 'You\'re frozen and can\'t move!' + bcolors.ENDC)
        # player takes damage if frozen, but restores 25% of max MP #
        player_dmg = enemy.generate_dmg()
        player.take_dmg(player_dmg)
        print(bcolors.FAIL + 'The enemy seizes opportunity and attacks!' + ' You take '
              + str(player_dmg) + ' points of damage.' + bcolors.ENDC)
        restored_mp = player.restore_mp(player.get_max_mp() * 0.25)
        print(bcolors.OKGREEN + 'While being frozen you siphoned some magic from the ice element. You restored ' +
              str(restored_mp) + ' points of mana' + bcolors.ENDC)
        round_counter += 1
        player_frozen = False
        continue

    # check if player died #
    if player.get_hp() <= 0:
        player.character_death()
        run = False
    # check if enemy died #
    if enemy.get_hp() <= 0:
        enemy.enemy_death()
        run = False

    # HP, MP info #
    print(bcolors.OKGREEN + '\nPlayer:' + bcolors.ENDC + bcolors.WARNING + '\t\t\tEnemy:' + bcolors.ENDC)
    print(bcolors.OKGREEN + 'HP:' + str(player.get_hp()) + '/' + str(player.get_max_hp()) + bcolors.ENDC +
          bcolors.WARNING + '\t\tHP:' + str(enemy.get_hp()) + '/' + str(enemy.get_max_hp()) + bcolors.WARNING)
    print(bcolors.OKGREEN + 'MP:' + str(player.get_mp()) + '/' + str(player.get_max_mp()) + bcolors.ENDC +
          bcolors.WARNING + '\t\tMP:' + str(enemy.get_mp()) + '/' + str(enemy.get_max_mp()) + bcolors.ENDC
          # align to the right if player mp becomes single digit #
          if player.get_mp() > 9
          else bcolors.OKGREEN + 'MP:' + str(player.get_mp()) + '/' + str(player.get_max_mp()) + bcolors.ENDC +
          bcolors.WARNING + '\t\t\tMP:' + str(enemy.get_mp()) + '/' + str(enemy.get_max_mp()) + bcolors.ENDC)
    # player actions #
    player.choose_action()
    choice = input(bcolors.OKCYAN + '\nChoose action: ' + bcolors.ENDC)
    index = None
    # quitting the game #
    if choice == 'quit':
        print(bcolors.OKGREEN, '\nThanks for playing!', bcolors.ENDC)
        break
        # run = False prints warning message for some reason... #
    # explanation of actions and spells #
    elif choice == 'help':
        player.command_help()
        continue
    # player actions #
    else:
        # failsafe for inputs that aren't numbers #
        try:
            choice = int(choice)
            index = choice - 1
        except ValueError:
            print(bcolors.FAIL, "\nInvalid command. Please type the number assigned to the action",
                  "you'd like to take.", bcolors.ENDC)
            continue
    # attack action if enemy's defence is up #
    if index == 0:
        if enemy_defended:
            enemy_dmg_def = player.generate_dmg() - enemy.get_df()
            if enemy_dmg_def < 0:
                enemy_dmg_def = 0
            enemy.take_dmg(enemy_dmg_def)
            print(bcolors.WARNING, '\nYou barely scratched it! The enemy takes',
                  'no damage!' + bcolors.ENDC if enemy_dmg_def == 0 else str(enemy_dmg_def) +
                  ' points of damage.' + bcolors.ENDC)
            # check if player won, else return enemy's current HP #
            if enemy.get_hp() <= 0:
                enemy.enemy_death()
                run = False
            else:
                print(bcolors.OKGREEN + 'It has ' + str(enemy.get_hp()) + ' health points left.' + bcolors.ENDC)
            enemy_defended = False
        # regular attack action #
        else:
            enemy_dmg = player.generate_dmg()
            enemy.take_dmg(enemy_dmg)
            print(bcolors.OKGREEN, '\nAttack successful! The enemy takes', enemy_dmg, 'points of damage!', bcolors.ENDC)
            # check if player won #
            if enemy.get_hp() <= 0:
                enemy.enemy_death()
                run = False
            else:
                print(bcolors.OKGREEN, '\nIt has', enemy.get_hp(), 'health points left.', bcolors.ENDC)
    # magic action #
    if index == 1:
        player.choose_magic()
        m_choice = input(bcolors.OKCYAN + '\nChoose a spell: ' + bcolors.ENDC)
        m_index = None
        # quitting the game #
        if m_choice == 'quit':
            print(bcolors.OKGREEN + bcolors.BOLD + '\nThanks for playing!' + bcolors.ENDC)
            run = False
        # explanation of actions and spells #
        if m_choice == 'help':
            player.command_help()
            continue
        # failsafe for inputs that aren't numbers #
        try:
            m_choice = int(m_choice)
            m_index = m_choice - 1

        except ValueError:
            print(bcolors.FAIL + "\nInvalid command. Please type the number assigned to the spell",
                  "you'd like to cast." + bcolors.ENDC)
            continue
        # confirm chosen spell #
        print(bcolors.OKGREEN, '\nYou chose to cast', magic[m_index]['name'] + '!' + bcolors.ENDC)
        # check if player has enough mana for the spell, if not reset back to action choice #
        if int(player.get_spell_mp_cost(m_index)) > player.get_mp():
            print(bcolors.FAIL + 'but the spell fails... You\'re too exhausted!' + bcolors.ENDC)
            continue
        # reduce player's mana by the spell's cost #
        else:
            player.reduce_mp(player.get_spell_mp_cost(m_index))
        # if dazed check if player fails the spell (the penalty is losing mana for nothing) #
        if player_dazed:
            if player.spell_fail_check():
                print(bcolors.WARNING + 'You can\'t keep your focus and fumble the spell!' + bcolors.ENDC)
                player_dazed = False
                continue
            else:
                print(bcolors.OKGREEN + 'Despite being dazed you keep your concentration!' + bcolors.ENDC)
                player_dazed = False
        elif player_dazed_2:
            if player.spell_fail_check():
                print(bcolors.WARNING + 'You can\'t keep your focus and fumble the spell!' + bcolors.ENDC)
                player_dazed_2 = False
                continue
            else:
                print(bcolors.OKGREEN + 'Despite being dazed you keep your concentration!' + bcolors.ENDC)
                player_dazed_2 = False
        # instant heal spell #
        if m_index == 3:
            heal_dmg = player.generate_spell_damage(m_index)
            player.heal(heal_dmg)
            print(bcolors.OKBLUE + '\nYou healed for ' + str(heal_dmg) + ' health points.' +
                  '\nYour current HP is ' + str(player.get_hp()) + bcolors.ENDC)
        # recurring heal spell #
        elif m_index == 4:
            restoration_1 = True
            restoration_2 = True
            print(bcolors.OKBLUE + 'You will be healed at the start of the next 2 rounds.' + bcolors.ENDC)
        # damaging spells #
        else:
            player_spell_dmg = player.generate_spell_damage(m_index)
            enemy.take_dmg(player_spell_dmg)
            print(bcolors.OKGREEN + 'Enemy takes ' + str(player_spell_dmg) + ' points of damage!' + bcolors.ENDC)
            # check if player won, else confirm the enemy's current HP #
            if enemy.get_hp() <= 0:
                enemy.enemy_death()
                run = False
            else:
                print(bcolors.OKGREEN + 'It has ' + str(enemy.get_hp()) + ' health points left.' + bcolors.ENDC)
                # check if spell applied burn, dazed or freeze status effects #
                if m_index == 0:
                    enemy_burn = enemy.status_check()
                    enemy_burn_2 = enemy_burn
                    if enemy_burn:
                        print(bcolors.OKGREEN + 'The enemy is burning!' +
                              ' It will take fire damage at the begging of the next two rounds.' + bcolors.ENDC)
                elif m_index == 1:
                    enemy_dazed = enemy.status_check()
                    enemy_dazed_2 = enemy_dazed
                    if enemy_dazed:
                        print(bcolors.OKGREEN + 'The enemy is dazed! It\'s spells will have a chance of failing' +
                              ' for the next two rounds.' + bcolors.ENDC)
                else:
                    enemy_frozen = enemy.status_check()
                    if enemy_frozen:
                        print(bcolors.OKGREEN + 'Your spell freezes the enemy! It won\'t be able to move this round.'
                              + bcolors.ENDC)
    # defend action #
    if index == 2:
        print(bcolors.OKGREEN + '\nYou chose to defend! ' +
              "Enemy's next attack will deal significantly less dmg." + bcolors.ENDC)
        player_defended = True

    # item action #
    if index == 3:
        player.choose_item()
        item_choice = input(bcolors.OKCYAN + '\nChoose an item: ' + bcolors.ENDC)
        item_index = None
        # check if player quit the game #
        if item_choice == 'quit':
            print(bcolors.OKGREEN + bcolors.BOLD + '\nThanks for playing!' + bcolors.ENDC)
            run = False
        # explanation of actions and spells #
        if item_choice == 'help':
            player.command_help()
            continue
        # failsafe for inputs that aren't numbers #
        try:
            item_choice = int(item_choice)
            item_index = item_choice - 1
        except ValueError:
            print(bcolors.FAIL + "\nInvalid command. Please type the number assigned to the item",
                  "you'd like to use." + bcolors.ENDC)
            continue
        # confirm chosen item #
        print(bcolors.OKGREEN + '\nYou chose to use ' + player_items[item_index].name + '!' + bcolors.ENDC)
        # healing items #
        if item_index in range(0, 3):
            # check if item has any uses left #
            if player_items[item_index].uses == 0:
                print(bcolors.FAIL + 'You don\'t have any vials of ' + player_items[item_index].name + " left!"
                      + bcolors.ENDC)
                continue
            # heal and take away 1 use of the item #
            else:
                player_items[item_index].uses -= 1
                player.heal(player_items[item_index].dmg)
                print(bcolors.OKGREEN + 'You were healed for ' + str(player_items[item_index].dmg) + ' health points.'
                      + bcolors.ENDC)
        # grenade #
        elif item_index == 3:
            # check if item has any uses left #
            if player_items[item_index].uses == 0:
                print(bcolors.FAIL + 'You don\'t have any vials of ' + player_items[item_index].name + " left!"
                      + bcolors.ENDC)
                continue
            # deal damage and check if burn is applied, take away 1 use of the item #
            else:
                player_items[item_index].uses -= 1
                enemy.take_dmg(player_items[item_index].dmg)
                print(bcolors.OKGREEN + 'It lands right before the enemy\'s feet and explodes, dealing '
                      + str(player_items[item_index].dmg) + ' points of damage!' + bcolors.ENDC)
                enemy_burn = enemy.status_check()
                enemy_burn_2 = enemy_burn
                # check if grenade killed the enemy #
                if enemy.get_hp() <= 0:
                    enemy.enemy_death()
                    run = False
                if enemy_burn:
                    print(bcolors.OKGREEN + 'The enemy is burning!' +
                          ' It will take fire damage at the begging of the next two rounds.' + bcolors.ENDC)
        # mana potion #
        elif item_index == 4:
            # check if item has any uses left #
            if player_items[item_index].uses == 0:
                print(bcolors.FAIL + 'You don\'t have any ' + player_items[item_index].name + " left!" + bcolors.ENDC)
                continue
            # restore mana #
            else:
                player_items[item_index].uses -= 1
                player.restore_mp(player_items[item_index].dmg)
                print(bcolors.OKGREEN + 'It restored ' + str(player_items[item_index].dmg) +
                      ' points of mana.' + bcolors.ENDC)
        # soothing balm #
        elif item_index == 5:
            # check if item has any uses left #
            if player_items[item_index].uses == 0:
                print(bcolors.FAIL + 'You don\'t have any ' + player_items[item_index].name + " left!" + bcolors.ENDC)
                continue
            # heal and cure burn #
            else:
                player_items[item_index].uses -= 1
                player.heal(player_items[item_index].dmg)
                player_burn_2 = False
                print(bcolors.OKGREEN + 'You were healed for ' + str(player_items[item_index].dmg) + ' health points.' +
                      ' You\'re no longer burning!' + bcolors.ENDC)
        # potion of clear mind #
        elif item_index == 6:
            # check if item has any uses left #
            if player_items[item_index].uses == 0:
                print(bcolors.FAIL + 'You don\'t have any vials of ' + player_items[item_index].name + " left!"
                      + bcolors.ENDC)
                continue
            # heal and cure dazed #
            else:
                player_items[item_index].uses -= 1
                player.heal(player_items[item_index].dmg)
                player_dazed = False
                player_dazed_2 = False
                print(bcolors.OKGREEN + 'You were healed for ' + str(player_items[item_index].dmg) + ' health points.'
                      + ' You\'re no longer dazed!' + bcolors.ENDC)

    # failsafe in case player inputs an invalid action number #
    if index not in range(0, 4):
        print(bcolors.WARNING + "\nPlease type a number assigned to the action you'd like to take (1-4)."
              + bcolors.FAIL)
        continue
    # increase round counter after player's action #
    round_counter += 1

    # ENEMY'S TURN #
    print(bcolors.FAIL + bcolors.BOLD + "\n\n===ENEMY'S TURN!===" + bcolors.ENDC)
    if enemy_frozen:
        print(bcolors.OKGREEN + '\nThe enemy is frozen and it can\'t move!' + bcolors.ENDC)
        enemy_frozen = False
        continue
    # generate enemy action based on the AI method (see conditions in characters.py) #
    enemy_action = enemy.generate_enemy_action()
    # magic action #
    if enemy_action == 'Magic':
        print(bcolors.WARNING + '\nThe enemy chooses to cast a spell!' + bcolors.ENDC)
        enemy_spell_index = random.randrange(0, 2)
        # check if enemy has enough mana for the spell, if not it skips it's turn #
        if enemy.get_mp() < enemy.get_spell_mp_cost(enemy_spell_index):
            print(bcolors.WARNING + '... but nothing happens!' + bcolors.ENDC)
            continue
        # reduce enemy's MP by spell's cost #
        else:
            enemy.reduce_mp(enemy.get_spell_mp_cost(enemy_spell_index))
        # check if enemy is dazed (reduced chance for a spell to succeed, check characters.py for details #
        if enemy_dazed:
            if enemy.spell_fail_check():
                print(bcolors.WARNING + 'The enemy fumbles the spell!' + bcolors.ENDC)
                enemy_dazed = False
                continue
            else:
                print('The enemy is dazed... but pushes through it!')
                enemy_dazed = False
        elif enemy_dazed_2:
            if enemy.spell_fail_check():
                print(bcolors.WARNING + 'The enemy fumbles the spell!' + bcolors.ENDC)
                enemy_dazed_2 = False
                continue
            else:
                print('The enemy is dazed... but pushes through it!')
                enemy_dazed_2 = False
        # if spell didn't fail, cast it and check for status effects #
        enemy_spell_name = enemy.get_spell_name(enemy_spell_index)
        enemy_spell_dmg = enemy.generate_spell_damage(enemy_spell_index)
        print(bcolors.WARNING + '\nThe enemy casts ' + enemy_spell_name + '!',
              '\nYou take ' + str(enemy_spell_dmg) + ' points of damage!' + bcolors.ENDC)
        # check if player died #
        if player.get_hp() <= 0:
            player.character_death()
            run = False
        # check if spell applied burn, dazed or freeze status effects #
        if enemy_spell_index == 0:
            player_burn = player.status_check()
            player_burn_2 = player_burn
            if player_burn:
                print(bcolors.WARNING + 'You\'re burning!' +
                      ' You will take fire damage at the begging of the next two rounds.' + bcolors.ENDC)
        elif enemy_spell_index == 1:
            player_dazed = player.status_check()
            player_dazed_2 = player_dazed
            if player_dazed:
                print(bcolors.WARNING + 'You\'re dazed! Your spells will have a chance of failing'
                                        ' for the next two rounds.' + bcolors.ENDC)
        else:
            player_frozen = player.status_check()
            if player_frozen:
                print(bcolors.WARNING + 'The enemy\'s spell freezes you! You won\'t be able to move this round.'
                      + bcolors.ENDC)
    # non-magic actions #
    else:
        print(bcolors.WARNING + 'The enemy chooses to ' + enemy_action + '!' + bcolors.ENDC)
        # attack action #
        if enemy_action == 'Attack':
            # check if player's guard is up #
            if player_defended:
                player_dmg_def = enemy.generate_dmg() - player.get_df()
                if player_dmg_def < 0:
                    player_dmg_def = 0
                player.take_dmg(player_dmg_def)
                print(bcolors.WARNING, '\nThe enemy barely scratched you! You take',
                      'no damage!' + bcolors.ENDC if player_dmg_def == 0 else str(player_dmg_def) +
                      ' points of damage.' + bcolors.ENDC)
                # check if player died #
                if player.get_hp() <= 0:
                    player.character_death()
                    run = False
                else:
                    print(bcolors.WARNING + 'Your guard was successful!' + bcolors.ENDC)
                # un-flag player's guard #
                player_defended = False
            # regular attack action #
            else:
                player_dmg = enemy.generate_dmg()
                player.take_dmg(player_dmg)
                print(bcolors.FAIL + "It\'s vicious attack takes away",
                      player_dmg, 'of your HP!', bcolors.ENDC)
                # check if player died #
                if player.get_hp() <= 0:
                    player.character_death()
                    run = False
                else:
                    print(bcolors.WARNING, '\nYou are left with', player.get_hp(), 'points of health.', bcolors.ENDC)
        # defence action #
        else:
            enemy_defended = True
            print(bcolors.WARNING + 'Your next physical attack will be less effective.' + bcolors.ENDC)
