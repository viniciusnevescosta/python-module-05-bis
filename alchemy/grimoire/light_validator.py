from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    lowered = ingredients.lower()
    allowed = light_spell_allowed_ingredients()
    valid = any(ingredient in lowered for ingredient in allowed)
    status = "VALID" if valid else "INVALID"
    return f"{ingredients} - {status}"
