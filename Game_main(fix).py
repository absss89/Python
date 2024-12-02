from character import Hero, Goblin, Orc, Dragon
from battle import Battle
import random


def create_random_monster():
    monster_type = random.choice([Goblin, Orc, Dragon])
    if monster_type == Goblin:
        return Goblin("고블린", 30, 10, 2, 10, 1)
    elif monster_type == Orc:
        return Orc("오크", 50, 15, 5, 8, 1)
    else:
        return Dragon("드래곤", 100, 20, 10, 5, 1)


def main():
    print("게임 시작")
    name = input("이름 입력: ")
    role = input("직업 입력(전사/마법사/궁수): ")
    hero = Hero(name, 100, 20, 5, role, speed=12)
    print(hero)
    battle = Battle()

    for i in range(5):
        monster = create_random_monster()
        print(monster.description())
        battle.fight(hero, monster)
        monster.level_up()

    print(hero)


if __name__ == '__main__':
    main()
