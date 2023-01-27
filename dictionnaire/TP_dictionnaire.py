###################################
##     Exercice 4  : MORSE       ##
###################################

# compléter les fonctions pour qu'elles
# répondent à leur docstring

dict_morse={
    'A':'- ---',
    'B':'--- - - -',
    'C':'--- - --- -',
    'D':'--- - -',
    'E':'-',
    'F':'- - --- -',
    'G':'--- --- -',
    'H':'- - - -',
    'I':'- -',
    'J':'- --- --- ---',
    'K':'--- - ---',
    'L':'- --- - -',
    'M':'--- ---',
    'N':'--- -',
    'O':'--- --- ---',
    'P':'- --- --- -',
    'Q':'--- --- - ---',
    'R':'- --- -',
    'S':'- - -',
    'T':'---',
    'U':'- - ---',
    'V':'- - - ---',
    'W':'- --- ---',
    'X':'--- - - ---',
    'Y':'--- - --- ---',
    'Z':'--- --- - -',
    }

def traduction_en_morse(texte):
    '''
    traduit un texte en majuscules en morse
    avec un espace entre chaque lettre
    et 7 espaces entre chaque mot
    texte : str
    return : str
    >>>mon_texte="LE MORSE EST UN LANGAGE CODE"
    >>>traduction_en_morse(mon_texte)=="- --- - -   -       --- ---   --- --- ---   - --- -   - - -   -       -   - - -   ---       - - ---   --- -       - --- - -   - ---   --- -   --- --- -   - ---   --- --- -   -       --- - --- -   --- --- ---   --- - -   -"
    True
    '''
    texte.upper()
    mots = texte.split()
    morse = ""
    for mot in mots:
        for lettre in mot:
            morse += dict_morse[lettre] + " "
        morse += " " * 6
    return morse.rstrip()

def dictionnaire_morse_caractere(mon_dict):
    '''
    retourne un dictionnaire dont les clés
    sont des caractères morses et les valeurs
    les lettres associées
    : mon_dict : un dictionnaire qui traduit des
    caractères en morse
    : return : dict()
    >>> mon_morse_dico=dictionnaire_morse_caractere(dict_morse)
    >>> mon_morse_dico['--- --- -']='G'
    '''
    dict = {}
    for cle, value in mon_dict.items():
        dict[value] = cle
    return dict
    


mon_texte="LE MORSE EST UN LANGAGE CODE"
morse = traduction_en_morse(mon_texte)
print(morse)

dict = dictionnaire_morse_caractere(dict_morse)

print(dict)



def traduction_morse_francais(mon_code):
    '''
    traduit un code en morse en texte en français
    : mon_code: str
    : return : str
    >>>mon_texte="LE MORSE EST UN LANGAGE CODE"
    >>>code_a_decoder=traduction_en_morse(mon_texte)
    >>>traduction_morse_francais(code_a_decoder))=="LE MORSE EST UN LANGAGE CODE"
    True
    '''
    global dict_morse
