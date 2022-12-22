import math
import numpy as np

country = input("Country:")
le = float(input("levensverwachting bij geboorte:"))
mys = float(input("gemiddeld aantal jaren scholing voor een 25-jarige :"))
eys = float(input("gemiddeld aantal jaren scholing voor een 5-jarige :"))
gnipc = float(input("bruto nationaal inkomen per hoofd van de bevolking :"))

volksgezondheid = (le - 20) / (82.3 - 20)
gemiddelde_scholingsjarenindex = mys / 13.2
verwachte_scholingsjarenindex = eys / 20.6

kennis = math.sqrt((gemiddelde_scholingsjarenindex * verwachte_scholingsjarenindex)) / 0.951

levensstandaard = (np.log(gnipc) - np.log(100)) / (np.log(107721) - np.log(100))


def geometric_mean(numbers):
    product = math.prod(numbers)
    n = len(numbers)
    mean = pow(product, 1 / n)
    return mean


development_index = geometric_mean([volksgezondheid, kennis, levensstandaard])
development_index = f'{development_index:.3f}'

print("De HDI van " + country + " bedraagt " + development_index + ".")
