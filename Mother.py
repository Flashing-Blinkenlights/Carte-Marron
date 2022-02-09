"""Knows all the raw ingredients and their nutrient values"""


def watervolume(nutrients):
    # TODO: convert water g to dl
    return None


class Nutrient():
    """docstring for Nutrient."""

    # liquids
    self.water = {"value" = None, "unit" = "g"}
    self.alcohol = {"value" = None, "unit" = "g"}
    # calories
    self.total_calories = {"value" = None, "unit" = "kcal"}
    self.fat_calories = {"value" = None, "unit" = "kcal"}
    # carbohydrates
    self.total_carbohydrates = {"value" = None, "unit" = "g"}
    self.starch = {"value" = None, "unit" = "mg"}
    self.sugar = {"value" = None, "unit" = "mg"}
    self.fructose = {"value" = None, "unit" = "mg"}
    self.maltose = {"value" = None, "unit" = "mg"}
    self.galactose = {"value" = None, "unit" = "mg"}
    self.glucose = {"value" = None, "unit" = "mg"}
    self.lactose = {"value" = None, "unit" = "mg"}
    self.sucrose = {"value" = None, "unit" = "mg"}
    self.fibre = {"value" = None, "unit" = "mg"}
    # fats
    self.total_fat = {"value" = None, "unit" = "mg"}
    self.saturated_fat = {"value" = None, "unit" = "mg"}
    self.monounsaturated_fat = {"value" = None, "unit" = "mg"}
    self.polyunsaturated_fat = {"value" = None, "unit" = "mg"}
    self.omega3 = {"value" = None, "unit" = "mg"}
    self.omega6 = {"value" = None, "unit" = "mg"}
    # proteins
    self.protein = {"value" = None, "unit" = "mg"}
    self.tryptophan = {"value" = None, "unit" = "mg"}
    self.threinine = {"value" = None, "unit" = "mg"}
    self.isoleucine = {"value" = None, "unit" = "mg"}
    self.leucine = {"value" = None, "unit" = "mg"}
    self.lysine = {"value" = None, "unit" = "mg"}
    self.methionine = {"value" = None, "unit" = "mg"}
    self.cystine = {"value" = None, "unit" = "mg"}
    self.phenylalanine = {"value" = None, "unit" = "mg"}
    self.tyrosine = {"value" = None, "unit" = "mg"}
    self.vraline = {"value" = None, "unit" = "mg"}
    self.arginine = {"value" = None, "unit" = "mg"}
    self.histidine = {"value" = None, "unit" = "mg"}
    self.alanine = {"value" = None, "unit" = "mg"}
    self.aspartic_acid = {"value" = None, "unit" = "mg"}
    self.glutamic_acid = {"value" = None, "unit" = "mg"}
    self.glycine = {"value" = None, "unit" = "mg"}
    self.proline = {"value" = None, "unit" = "mg"}
    self.serine = {"value" = None, "unit" = "mg"}

    self.vitaminA = {"value" = None, "unit" = "µg"}
    self.thiamin = {"value" = None, "unit" = "µg"}
    self.riboflavin = {"value" = None, "unit" = "µg"}
    self.niacin = {"value" = None, "unit" = "mg"}
    self.vitaminB6 = {"value" = None, "unit" = "mg"}
    self.vitaminB12 = {"value" = None, "unit" = "µg"}

    self.folate = {"value" = None, "unit" = "µg"}
    self.folic_acid = {"value" = None, "unit" = "mg"}

    self.vitaminC = {"value" = None, "unit" = "mg"}
    self.iodine = {"value" = None, "unit" = "µg"}
    self.vitaminE = {"value" = None, "unit" = "µg"}
    self.panto_acid = {"value" = None, "unit" = "µg"}
    self.vitaminK = {"value" = None, "unit" = "µg"}
    self.retinol = {"value" = None, "unit" = "µg"}
    self.alpha_carotine = {"value" = None, "unit" = "µg"}
    self.beta_carotine = {"value" = None, "unit" = "µg"}
    self.beta_cryptoxanthin = {"value" = None, "unit" = "µg"}
    self.lycopene = {"value" = None, "unit" = "mg"}
    self.lutein_zeaxanthin = {"value" = None, "unit" = "mg"}
    self.beta_tocopherol = {"value" = None, "unit" = "mg"}
    self.gamma_tocopherol = {"value" = None, "unit" = "mg"}
    self.delta_tocipherol = {"value" = None, "unit" = "mg"}

    self.calcium = {"value" = None, "unit" = "mg"}
    self.iron = {"value" = None, "unit" = "mg"}
    self.magnesium = {"value" = None, "unit" = "mg"}
    self.potassium = {"value" = None, "unit" = "mg"}
    self.sodium = {"value" = None, "unit" = "mg"}
    self.phosphorus = {"value" = None, "unit" = "mg"}
    self.zinc = {"value" = None, "unit" = "mg"}
    self.copper = {"value" = None, "unit" = "µg"}
    self.manganese = {"value" = None, "unit" = "mg"}
    self.selenium = {"value" = None, "unit" = "mg"}
    self.fluoride = {"value" = None, "unit" = "mg"}

    self.cholesterol = {"value" = None, "unit" = "mg"}
    self.phytosterols = {"value" = None, "unit" = "mg"}

    def __init__(self, carbohydrates={}, protein=0, fat=0, liquid=0, fibre=0,
                 vitaminA=0, thiamin=0, riboflavin=0, niacin=0,
                 vitaminB6=0, vitaminB12=0, folate=0, vitaminC=0,
                 calcium=0, iodine=0, iron=0, magnesium=0, potassium=0,
                 sodium=0, zinc=0):

        self.total_carbohydrates["value"] = total_carbohydrates
        self.protein["value"] = protein
        self.fat["value"] = fat

        self.liquid["value"] = liquid
        self.fibre["value"] = fibre
        self.vitaminA["value"] = vitaminA
        self.thiamin["value"] = thiamin
        self.riboflavin["value"] = riboflavin
        self.niacin["value"] = niacin
        self.vitaminB6["value"] = vitaminB6
        self.vitaminB12["value"] = vitaminB12
        self.folate["value"] = folate
        self.vitaminC["value"] = vitaminC
        self.calcium["value"] = calcium
        self.iodine["value"] = iodine
        self.iron["value"] = iron
        self.magnesium["value"] = magnesium
        self.potassium["value"] = potassium
        self.sodium["value"] = sodium
        self.zinc["value"] = zinc


class Ingredient(object):
    """docstring for Ingredient."""

    self.nutrients

    def __init__(self, arg):
        super(Ingredient, self).__init__()
        self.arg = arg
