from audioop import add
from cmath import sqrt
import matplotlib.pyplot as plt  # type:ignore


class Poly2:
    """ Classe permettant de representer un polynôme de degré 2."""

    def __init__(self, *coeffs):
        """ Méthode constructeur qui prend en paramètre, les coefficients du polynôme"""
        self.coeffs = list(coeffs)

    def __add__(self, other):
        """Addition 2 polynômes et qui renvoi du nouveau polynôme"""
        assert(len(self.coeffs) == len(other.coeffs))
        a = []
        for i in range(len(self.coeffs)):
            a.append(self.coeffs[i] + other.coeffs[i])
        return f"{a[2]}X^2 + {a[1]}x + {a[0]}"
    
    def __sub__(self, other):
        """Soustraction de 2 polynômes et renvoi du nouveau polynôme"""
        assert(len(self.coeffs) == len(other.coeffs))
        s = []
        for i in self.coeffs:
            s.append(self.coeffs[i] - other.coeffs[i])
        return f"{s[2]}X^2 + {s[1]}x + {s[0]}"

    def __repr__(self):
        msg = 'Poly2(' + ', '.join([str(c) for c in sorted(self.coeffs.values())]) + ')'
        return msg

    def __str__(self):
        """Méthode qui personalise la chaîne de caractère affichée par la fonction print
        Si: p1 = Poly(3, -4, 2)
        Alors print(p1) affiche: '2X^2 - 4X + 3'
        """
        
        return f"{self.coeffs[2]}X^2 + {self.coeffs[1]}x + {self.coeffs[0]}"

    def solve(self):
        """ Méthode qui renvoie les solutions si elles existent."""
        a = self.coeffs[2]
        b = self.coeffs[1]
        c = self.coeffs[0]
        delta = b*b-4*b*c
        if delta > 0:
            rDelta=sqrt(delta)
            solutions = [(-b-rDelta)/(2*a),(-b+rDelta)/(2*a)]
        elif delta < 0:
            rDelta=sqrt(delta)
            solutions = [(-b-rDelta)/(2*a),(-b+rDelta)/(2*a)]
        else:
            solutions = [-b/(2*a)]
        return solutions

    def __val(self, x):
        """ Méthode qui calcule et renvoie la valeur de y en fonction de x.
        Si: y = x^2 + 1
        Si: x prend pour valeur 5
        Alors: y = 5^2 + 1 = 26
        """
        a = self.coeffs[2]
        b = self.coeffs[1]
        c = self.coeffs[0]
        # y = ax^2 + bx + c
        y = a*x*x + b*x + c
        return y
        
    def draw(self, x_points=None):
        """ Méthode qui trace la courbe, voir fichier png."""
        bar = [1, 1, 1]
        p1 = Poly2(*bar)
        solutions = p1.solve()
        for x in range(solutions[0], solutions[1]):
            y = Poly2.__val(self, x)
            plt.plot(x, y,)
            plt.show()


if __name__ == "__main__":
    bar = [1, 1, 1]
    p1 = Poly2(*bar)

    baz = [1, 1, 1]
    p2 = Poly2(*baz)

    p3 = p1 + p2
    print(p3)  # affiche 2x^2 + 2x + 2

    print(p1.solve())  # affiche ((-0.5+0.8660254037844386j), (-0.5-0.8660254037844386j))
    p1.draw()  # trace la courbe de p1, voir fichier png
