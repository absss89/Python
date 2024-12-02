import random


class Character:
    def __init__(self, name, hp, attack, defense, speed):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed

    def take_damage(self, damage):
        act ual_damage = max(0, damage - self.defense)
        self.hp = max(0, self.hp -actual_damage)
        return actual_damage

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return (f"{self.name} - HP: {self.hp}, 공격력: {self.attack}, "
                f"방어력: {self.defense}, 속도: {self.speed}")


class Equipment:
    def __init__(self, name, grade, attack_bonus=0, defense_bonus=0):
        self.name = name
        self.grade = grade
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus

    def __str__(self):
        return f"{self.grade} {self.name} (+공격력: {self.attack_bonus}, +방어력: {self.defense_bonus})"


class Monster(Character):
    def __init__(self, name, hp, attack, defense, speed, level):
        super().__init__(name, hp, attack, defense, speed)
        self.level = level

    def exp_reward(self):
        return self.level * 20

    def drop_loot(self):
        if random.random() < 0.5:
            equipment_type = "무기" if random.random() < 0.5 else "갑옷"
            rarity_chance = random.random()
            if rarity_chance < 0.5:
                grade = "일반"
            elif rarity_chance < 0.8:
                grade = "레어"
            else
                grade = "전설"

            attack_bonus = defense_bonus = 0
            if equipment_type == "무기":
                attack_bonus = self.level * 2
            else:
                defense_bonus = self.level * 2

            return Equipment(equipment_type, grade, attack_bonus, defense_bonus)
        return None

    def level_up(self):
        self.level += 1
        self.hp += 10
        self.attack += 2
        self.defense += 2
        self.speed += 1


class Hero(Character):
    def __init__(self, name, hp, attack, defense, speed, role):
        super().__init__(name, hp, attack, defense, speed)
        self.role = role
        self.exp = 0
        self.level = 1
        self.weapon = None
        self.armor = None

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= self.level * 100:
            self.level_up()

    def special_attack(self):
        if self.role == "전사":
            return self.attack + 4
        elif self.role == "마법사":
            return self.attack + 3
        elif self.role == "궁수":
            return self.attack + 2
        else:
            return self.attack

    def level_up(self):
        self.level += 1
        self.exp = 0
        if self.role == "전사":
            self.hp += 10
            self.attack += 5
            self.defense += 5
        elif self.role == "마법사":
            self.hp += 6
            self.attack += 10
            self.defense += 4
        elif self.role == "궁수":
            self.hp += 8
            self.attack += 8
            self.defense += 4
        print(f"{self.name}이(가) 레벨업했습니다. 현재 레벨: {self.level}")
        print(f"HP: {self.hp}, 공격력: {self.attack}, 방어력: {self.defense}")

    def equip(self, equipment):
        if equipment.grade == 'weapon':
            self.weapon = equipment
        elif equipment.grade == 'armor':
            self.armor = equipment

    def calculate_attack(self):
        base_attack = self.attack
        if self.weapon:
            return base_attack + self.weapon.attack_bonus
        return base_attack

    def calculate_defense(self):
        base_defense = self.defense
        if self.armor:
            return base_defense + self.armor.defense_bonus
        return base_defense


    def __str__(self):
        return (f"{self.name}[{self.role}] -  레벨: {self.level}, HP: {self.hp}, 공격력: {self.calculate_attack()}, "
                f"방어력: {self.calculate_defense()}, 속도: {self.speed}, 경험치: {self.exp}")
