#Goal= Get to heaven. Cookie Clicker but cookie doesn't want to be clicked.

obj_to_attack_with = {
    "Mouse" : 1,
    "Fist" : 5,
    "Boxing Glove" : 10,
    "Brass Knuckles" : 20,
    "Stick" : 50,
    "Knife" : 100,
    "Chair" : 200,
    "Slingshot": 500,
    "Gun" : 1000,
}

class Cookie_God:
    def do_things(self, current_object, score, shop):
        self.current_object = current_object
        self.score = score
        self.shop = shop
    def score_adder(self):
        self.score = 0
        while self.score != 1500000:
            if self.current_object == "Mouse":
                self.score += obj_to_attack_with["Mouse"]
            if self.current_object == "Fist":
                self.score += obj_to_attack_with["Fist"]
            if self.current_object == "Boxing Glove":
                self.score += obj_to_attack_with["Boxing Glove"]
            if self.current_object == "Brass Knuckles":
                self.score += obj_to_attack_with["Brass Knuckles"]
            if self.current_object == "Stick":
                self.score += obj_to_attack_with["Stick"]
            if self.current_object == "Knife":
                self.score += obj_to_attack_with["Knife"]
            if self.current_object == "Chair":
                self.score += obj_to_attack_with["Chair"]
            if self.current_object == "Slingshot":
                self.score += obj_to_attack_with["Slingshot"]
            if self.current_object == "Gun":
                self.score += obj_to_attack_with["Gun"]
        return self.score
    def shop(self):
        self.shop = obj_to_attack_with
        self.shop += "Heaven : 1500000"
        return self.shop

class Dialogue:
    def dialogue(self, dialogue):
        self.dialogue = dialogue
    def dialogue_show(self):
        for i in self.dialogue:
            print(i)
