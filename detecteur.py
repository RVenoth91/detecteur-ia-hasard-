"""
Détecteur de Hasard vs Intelligence
Projet IA simple - Version corrigée
"""

def analyser_phrase(phrase):
    """
    Extrait 2 caractéristiques d'une phrase :
    1. Longueur moyenne des mots
    2. Nombre de lettres rares (z, q, w, x, y, k)
    """
    # Séparer la phrase en mots
    mots = phrase.split()
    
    # Si la phrase est vide
    if len(mots) == 0:
        return 0, 0
    
    # Calculer la longueur moyenne des mots
    somme_longueurs = 0
    for mot in mots:
        somme_longueurs = somme_longueurs + len(mot)
    longueur_moyenne = somme_longueurs / len(mots)
    
    # Compter les lettres rares
    lettres_rares = "zqwxyk"
    compteur_rares = 0
    for lettre in phrase.lower():
        if lettre in lettres_rares:
            compteur_rares = compteur_rares + 1
    
    return longueur_moyenne, compteur_rares


def entrainer_modele():
    """
    Entraîne le modèle avec des exemples connus
    """
    # Phrases écrites par des humains (exemples)
    phrases_humaines = [
        "Je suis un humain qui pense",
        "Bonjour comment tu vas aujourd'hui",
        "Le ciel est bleu et beau",
        "J'aime manger des pommes",
        "Demain il fera beau normalement"
    ]
    
    # Phrases générées aléatoirement (exemples)
    phrases_aleatoires = [
        "xkqz plm fj wxyz abc",
        "aaaaaaa eeee iiiii ooooo",
        "z q w r t y a z e r t y",
        "bjx kqz flm pqr stv",
        "mmmmm nnnnn bbbbb vvvvv"
    ]
    
    # Analyser toutes les phrases humaines
    scores_humains = []
    for phrase in phrases_humaines:
        lm, rares = analyser_phrase(phrase)
        scores_humains.append((lm, rares))
    
    # Analyser toutes les phrases aléatoires
    scores_hasard = []
    for phrase in phrases_aleatoires:
        lm, rares = analyser_phrase(phrase)
        scores_hasard.append((lm, rares))
    
    # Calculer la moyenne pour les humains
    somme_lm_humain = 0
    somme_rares_humain = 0
    for lm, rares in scores_humains:
        somme_lm_humain = somme_lm_humain + lm
        somme_rares_humain = somme_rares_humain + rares
    moyenne_lm_humain = somme_lm_humain / len(scores_humains)
    moyenne_rares_humain = somme_rares_humain / len(scores_humains)
    
    # Calculer la moyenne pour le hasard
    somme_lm_hasard = 0
    somme_rares_hasard = 0
    for lm, rares in scores_hasard:
        somme_lm_hasard = somme_lm_hasard + lm
        somme_rares_hasard = somme_rares_hasard + rares
    moyenne_lm_hasard = somme_lm_hasard / len(scores_hasard)
    moyenne_rares_hasard = somme_rares_hasard / len(scores_hasard)
    
    # Retourner le modèle (les deux profils)
    modele = {
        'humain': (moyenne_lm_humain, moyenne_rares_humain),
        'hasard': (moyenne_lm_hasard, moyenne_rares_hasard)
    }
    return modele


def predire(phrase, modele):
    """
    Prédit si une phrase est humaine ou aléatoire
    """
    # Analyser la phrase à tester
    lm, rares = analyser_phrase(phrase)
    
    # Profils du modèle
    lm_humain, rares_humain = modele['humain']
    lm_hasard, rares_hasard = modele['hasard']
    
    # Calculer la distance au profil humain
    distance_humain = abs(lm - lm_humain) + abs(rares - rares_humain)
    
    # Calculer la distance au profil hasard
    distance_hasard = abs(lm - lm_hasard) + abs(rares - rares_hasard)
    
    # Décider
    if distance_humain < distance_hasard:
        return "🧠 HUMAIN"
    else:
        return "🎲 HASARD"


# ============================================
# PROGRAMME PRINCIPAL
# ============================================

print("=" * 50)
print("🤖 Détecteur de Hasard vs Intelligence")
print("=" * 50)

# Étape 1 : Entraîner le modèle
print("\n📚 Entraînement du modèle en cours...")
modele = entrainer_modele()
print("✅ Modèle entraîné avec succès !")

# Étape 2 : Tester avec des exemples
print("\n" + "=" * 50)
print("📋 EXEMPLES DE TEST")
print("=" * 50)

# Liste des phrases à tester
phrases_a_tester = [
    "Je pense donc je suis",
    "Le chat dort sur le canapé",
    "azertyuiop qsdfghjklm wxcvbn",
    "Bonjour je m'appelle Venoth",
    "jksdhf kjsqdf mlkqsd jkqz"
]

for phrase in phrases_a_tester:
    resultat = predire(phrase, modele)
    print("\n📝 Phrase : \"" + phrase + "\"")
    print("→ Résultat : " + resultat)

# Étape 3 : Mode interactif
print("\n" + "=" * 50)
print("🎮 MODE INTERACTIF")
print("=" * 50)
print("Tape une phrase, je te dirai si c'est HUMAIN ou HASARD")
print("Tape 'quit' pour quitter")
print("-" * 50)

while True:
    # Demander une phrase à l'utilisateur
    saisie = input("\n✍️  Ta phrase : ")
    
    # Vérifier si l'utilisateur veut quitter
    if saisie.lower() == 'quit':
        print("\n👋 Merci d'avoir testé ! À bientôt !")
        break
    
    # Vérifier que la phrase n'est pas vide
    if saisie.strip() == "":
        print("⚠️  Tu n'as rien écrit ! Essaie encore.")
        continue
    
    # Prédire
    resultat = predire(saisie, modele)
    print("🔍 Résultat : " + resultat)