import random
import math
import json
def read_classe(name):
    

    f = open(("classes/" + name + ".json"), mode="r")
    attributes = json.load(f)
    name=classe(
        attributes["strength"],
        attributes["vitality"],
        attributes["agility"],
        attributes["inteligence"],
        attributes["spirit"],
        attributes["skills"]
    )

    return name

class Monster:
    def __init__(self,name,classe,nivel,strength,vitality,agility,inteligence,spirit):
        self.classe=read_classe(classe)
        self.name = name
        self.nivel=nivel
        self.strength=strength
        self.vitality=vitality
        self.agility=agility
        self.inteligence=inteligence
        self.spirit=spirit
        self.skills=read_classe(classe).skills
        self.maxhp=self.vitality*10
        self.hp = self.maxhp
        self.attack =self.strength*10
        self.mattack = self.inteligence*1.2
        self.iniciativa=self.agility*10
        self.debuff=""
        self.debuffowner=""


class Player:
    def __init__(self,name,classe,nivel,strength,vitality,agility,inteligence,spirit):
        self.name = name
        self.classe=read_classe(classe)
        self.nivel=nivel
        self.strength=strength+(self.nivel-1)
        self.vitality=vitality+(nivel-1)
        self.agility=agility+(nivel)
        self.inteligence=inteligence+(nivel)
        self.spirit=spirit+(nivel)
        self.skills=read_classe(classe).skills
        self.hpmax=self.vitality*self.classe.vitality
        self.hp = self.hpmax
        self.attack =self.strength*self.classe.strength
        self.mattack = self.inteligence*self.classe.inteligence
        self.iniciativa=self.agility*self.classe.agility
        self.debuff=None
        self.debuffowner=None

class classe:
    def __init__(self,strength,vitality,agility,inteligence,spirit,skills):
        self.strength=strength
        self.vitality=vitality
        self.agility=agility
        self.inteligence=inteligence
        self.spirit=spirit
        self.skills=skills

class skills:
    def __init__(self,tipo,dano,alvos):
        self.tipo=""
        self.dano=1
        self.alvos=[]







player=Player("kenetsu","sorcerer",1,0,16,20,10,10)
enemy=Monster("goblin","mage",1,1,8,15,10,10)


def checkdebuff(target):
     if target.debuff != None:
      if target.debuff == "poison":
         dano=math.ceil(enemy.mattack*0.2)
         player.hp=player.hp - dano
         print(f"voce recebeu {dano} por veneno")




def battle(*args):
   
   players=[]

   for p in args:
      players.append(p)
 
   turn=0
   agility_order=[]
   for p in players:
      agility_order.append((p,p.agility))

   agility_order.sort(key=lambda x: x[1] ,reverse=True)

   print(agility_order)
   while len(agility_order) > 1:
      for p in agility_order:
        jogador=p[0]
        print (jogador.name)

   

battle(player,enemy)


