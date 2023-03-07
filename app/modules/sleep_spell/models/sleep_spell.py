def calc_results(enemies, sleep_dmg):
    results = []
    for enemy in enemies:
        if enemy.hp <= sleep_dmg:
            sleep_dmg -= enemy.hp
            result = enemy.name + " is asleep."
            enemy.asleep = True
        else:
            enemy.hp -= sleep_dmg
            result = enemy.name + " is awake."
        results.append(result)
    clean_results = [*set(results)]
    sorted_results = sorted(clean_results)
    return sorted_results
