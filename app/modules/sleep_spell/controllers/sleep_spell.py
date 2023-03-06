from flask import flash, redirect, render_template, request
from app.modules.sleep_spell.models.enemy import Enemy


class SleepSpellController():
    def form(self):
        num_enemies = 0
        return render_template("sleep_spell.html", title="sleep spell", num_enemies=num_enemies)

    def result(self):
        if request.method == "POST":
            # validate user inputs as integers
            try:
                num_enemies = int(request.form["num_enemies"])
                sleep_dmg = int(request.form["sleepinput"])
                for i in range(1, num_enemies+1):
                    hp = int(request.form[f"hpinput{i}"])
            except ValueError:
                flash("invalid input, please enter an integer")
                return redirect(request.url)

            # create a list of enemy objects from form input values and sort by hp
            enemies = []
            for i in range(1, num_enemies+1):
                name = f"enemy {i}"
                hp = int(request.form[f"hpinput{i}"])
                enemy = Enemy(name, hp)
                enemies.append(enemy)
            enemies.sort(key=lambda x: x.hp, reverse=True)

            # calculate the sleep spell results for each enemy and store in a list
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
