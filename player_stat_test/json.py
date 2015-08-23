import sys
import os
import json

class DB:
    dirname = 'save'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    path = os.path.join(dirname, 'database{}'.format(sys.version.split()[0])+'.txt')
    @staticmethod
    def load():
        data = open(DB.path)
        obj = json.load(data)
        for i in obj.items():
            print (i)
        data.close()
        return obj
    @staticmethod
    def save(obj):
        f = open(DB.path, 'w')
        f.write(json.dumps(obj))
        f.close()

##################################

data = {
'player':{
'wins':0,
'losses':0,
'ranked':13,
'stars': 0,
'hearts':0,
'stamina':100,
'points':2,
'current_round':1,
'current_opponent' :1,
}, 
'opponent':{
'wins':0,
'losses':0,
'name':'Little Mac',
'age' :17,
'height':" 5' 7\" (170 cm)",
'weight':"107 lb (49KG)",
'location' :"Bronx, NY",

}
}

DB.save(data)
obj = DB.load()
