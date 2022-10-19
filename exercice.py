#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    # Copied from teacher since this exercice makes no sense
    # BAHA it doesn't even pass the tests

    if values is None:
        # TODO: Demander les valeurs ici
        values = []
        while len(values) < 10:
            values.append(input("Please enter a value\n"))

    num_values = [float(value) for value in values if value.isdigit()]
    str_values = [value for value in values if not value.isdigit()]

    return sorted(num_values) + sorted(str_values)


def anagrams(words: list = None) -> bool:
    while len(words) < 2:
        words.append(input("entrez un mot"))

    words = words[0:2]
    sortedWords = [sorted(word) for word in words]
    return sortedWords[0] == sortedWords[1]


def contains_doubles(items: list) -> bool:
    itemCounts = {}  # elem: count
    for item in items:
        if itemCounts.get(item, None):
            itemCounts[item] += 1
        else:
            itemCounts[item] = 1

    for count in itemCounts.values():
        if count > 1:
            return True

    return False

    # That is indeed OP
    return len(set(items)) != len(items)


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant
    #       ayant la meilleure moyenne ainsi que sa moyenne

    studentMeans = [(name, sum(grades)/len(grades)) \
                    for name, grades in student_grades.items()]

    studentMeans.sort(key = lambda x:x[1])
    return {studentMeans[-1][0]: studentMeans[-1][1]}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    charCounts = dict.fromkeys(sentence, 0)
    for char in sentence:
        charCounts[char] += 1

    # I'm not printing

    return charCounts


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    # whatever
    ...


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(
        f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
