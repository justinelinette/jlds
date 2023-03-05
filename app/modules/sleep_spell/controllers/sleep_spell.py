from flask import render_template, request
from app.modules.sleep_spell.models.enemy import Enemy


class SleepSpellController():
    def form(self):
        num_enemies = 0
        return render_template("sleep_spell.html", title="sleep spell", num_enemies=num_enemies)

    def result(self):
        if request.method == "POST":
            num_enemies = int(request.form["num_enemies"])
            sleep_dmg = int(request.form["sleepinput"])
            enemies = []
            for i in range(1, num_enemies+1):
                name = f"enemy {i}"
                hp = int(request.form[f"hpinput{i}"])
                enemy = Enemy(name, hp)
                enemies.append(enemy)
            results = []
            for enemy in enemies:
                if enemy.hp <= sleep_dmg:
                    sleep_dmg -= enemy.hp
                    result = "is asleep."
                    enemy.asleep = True
                else:
                    enemy.hp -= sleep_dmg
                    result = "is awake."
                results.append(result)
        zipped = zip(enemies, results)
        return render_template("result.html", enemies=enemies, results=results, zip=zip, title="sleep spell results")
