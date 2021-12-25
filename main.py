def poser_une_question(question, r1, r2, r3, r4, réponse_question):
    global score
    print('Question:')
    print(' ', question)
    print(' (a)', r1)
    print(' (b)', r2)
    print(' (c)', r3)
    print(' (d)', r4)
    réponse = input('Quelle est votre réponse?')
    if réponse == réponse_question:
        print('Bonne réponse!')
        score += 1
    else:
        print('Mauvaise réponse!')


score = 0
poser_une_question('En quelle année est sorti le python:', '1991', '2005', '1996', '1995', 'a')
poser_une_question("Combien y a-t-il d'états en Amérique?", '56', '58', '53', '52', 'd')
poser_une_question("Quelle est la capitale de la france?", 'Bordeaux', "Paris", 'Nice', 'Marseille', 'b')
print('Votre score est:', score)
