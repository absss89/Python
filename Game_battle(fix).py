import random
from character import Hero, Goblin, Orc, Dragon

class Battle:
    def fight(self, hero, monster):
        print(f"전투 시작 {hero.name} vs {monster.name}")
        hero_turn = hero.speed >= monster.speed
        turn = 1

        while hero.is_alive() and monster.is_alive():
            print(f"== 턴 {turn} ==")
            if hero_turn:
                if random.random() < 0.3:  # 30% 확률로 특수 공격 사용
                    damage = monster.take_damage(hero.special_attack())
                    print(f"{hero.name}가 {monster.name}에게 특수 공격으로 {damage}의 데미지를 입힘!")
                else:
                    damage = monster.take_damage(hero.calculate_attack())
                    print(f"{hero.name}가 {monster.name}에게 {damage}의 데미지를 입힘")
                if not monster.is_alive():
                    print(f"{monster.name}이(가) 쓰러졌다!")
                    hero.gain_exp(monster.exp_reward())
                    loot = monster.drop_loot()
                    if loot:
                        hero.equip(loot)
                    return
            else:
                if random.random() < 0.3:
                    damage = hero.take_damage(monster.special_attack())
                    print(f"{monster.name}가 특수 공격으로 {hero.name}에게 {damage}의 데미지를 입힘!")
                else:
                    damage = hero.take_damage(monster.attack)
                    print(f"{monster.name}가 {hero.name}에게 {damage}의 데미지를 입힘")
                if not hero.is_alive():
                    print(f"{hero.name}이(가) 쓰러졌다!")
                    return
            hero_turn = not hero_turn
            turn += 1

        print("전투 종료")
