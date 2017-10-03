
class Dès(object):
    def __init__(self):
        self.Face = 0
        
        
    # Start of user code -> properties/constructors for Dès class

    # End of user code
    def Random(self):
        # Start of user code protected zone for Random function body
        return 0
        # End of user code	
    # Start of user code -> methods for Dès class

    # End of user code

class Case(object):
    def __init__(self):
        self.id = 0
        self.image = ""
        self.prix = 0
        self.couleur = 0
        
        self.plateau = None
        
    # Start of user code -> properties/constructors for Case class

    # End of user code
    # Start of user code -> methods for Case class

    # End of user code

class Joueur(object):
    def __init__(self):
        self.Argent = 0
        self.Bonheur = 0
        self.Vie = 0
        self.Position = 0
        self.Caracteristique = 
        self.Pseudo = ""
        self.Sexe = 0
        
        self.plateau = None
        
    # Start of user code -> properties/constructors for Joueur class

    # End of user code
    def deplacement(self):
        # Start of user code protected zone for deplacement function body
        raise NotImplementedError
        # End of user code	
    def achat(self):
        # Start of user code protected zone for achat function body
        return None
        # End of user code	
    # Start of user code -> methods for Joueur class

    # End of user code

class Plateau(object):
    def __init__(self):
        self.id_case = 
        self.dernierjoueur = None
        
        self.case = None
        self.joueur = None
        
    # Start of user code -> properties/constructors for Plateau class

    # End of user code
    def creationtableau(self):
        # Start of user code protected zone for creationtableau function body
        raise NotImplementedError
        # End of user code	
    def toursuivant(self):
        # Start of user code protected zone for toursuivant function body
        raise NotImplementedError
        # End of user code	
    def creationjoueur(self):
        # Start of user code protected zone for creationjoueur function body
        raise NotImplementedError
        # End of user code	
    # Start of user code -> methods for Plateau class

    # End of user code


class Spécial(Case):
    def __init__(self):
        self.modife argent = None
        self.modifie vie = None
        
        
    # Start of user code -> properties/constructors for Spécial class

    # End of user code
    # Start of user code -> methods for Spécial class

    # End of user code

class Achat(Case):
    def __init__(self):
        self.cout = None
        
        
    # Start of user code -> properties/constructors for Achat class

    # End of user code
    # Start of user code -> methods for Achat class

    # End of user code

class Chance(Case):
    def __init__(self):
        self.gagne maladie = None
        
        
    # Start of user code -> properties/constructors for Chance class

    # End of user code
    # Start of user code -> methods for Chance class

    # End of user code


# Start of user code -> functions/methods for model package

# End of user code
