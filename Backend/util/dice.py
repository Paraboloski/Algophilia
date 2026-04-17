import re
import random
from typing import TypedDict, List, Optional

class DiceRollResult(TypedDict):
    total: int
    rolls: List[int]
    expression: str
    bonus: int

def roll_single(sides: int) -> int:
    if sides < 1: return 0
    return random.randint(1, sides)

def parse_dice_expression(expression: str) -> tuple[int, int, int]:
    clean_expr = expression.replace(" ", "").lower()
    
    pattern = r"(\d+)d(\d+)(?:([+-])(\d+))?"
    match = re.fullmatch(pattern, clean_expr)
    
    if not match:
        pattern_short = r"d(\d+)(?:([+-])(\d+))?"
        match = re.fullmatch(pattern_short, clean_expr)
        if match:
            quantity = 1
            sides = int(match.group(1))
            sign = match.group(2)
            bonus_val = int(match.group(3)) if match.group(3) else 0
            bonus = bonus_val if sign == "+" or not sign else -bonus_val
            return quantity, sides, bonus
        raise ValueError(f"Espressione dadi non valida: {expression}")
    
    quantity = int(match.group(1))
    sides = int(match.group(2))
    sign = match.group(3)
    bonus_val = int(match.group(4)) if match.group(4) else 0
    
    bonus = bonus_val if sign == "+" or not sign else -bonus_val
    
    return quantity, sides, bonus

def roll(quantity: int, sides: int, bonus: int = 0) -> DiceRollResult:
    if quantity < 1: quantity = 1
        
    rolls = [roll_single(sides) for _ in range(quantity)]
    total = sum(rolls) + bonus
    
    sign = "+" if bonus >= 0 else "-"
    expression = f"{quantity}d{sides}"
    if bonus != 0:
        expression += f" {sign} {abs(bonus)}"
    
    return {
        "total": total,
        "rolls": rolls,
        "expression": expression,
        "bonus": bonus
    }

def roll_dice(expression: str) -> DiceRollResult:
    quantity, sides, bonus = parse_dice_expression(expression)
    return roll(quantity, sides, bonus)
