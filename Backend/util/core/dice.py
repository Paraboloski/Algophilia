import re
import random
from result import Result, Err
from typing import TypedDict, List, Tuple
from middleware.config import ok, err, guard, ParseError, ValidationError

class DiceRollResult(TypedDict):
    total: int
    rolls: List[int]
    expression: str
    bonus: int


def roll_single(sides: int) -> int: return random.randint(1, sides)

def parse_dice_expression(expression: str) -> Result[Tuple[int, int, int], ParseError]:
    clean_expr = expression.replace(" ", "").lower()
    pattern = r"(\d+)d(\d+)(?:([+-])(\d+))?"
    match = re.fullmatch(pattern, clean_expr)

    if not match:
        pattern_short = r"d(\d+)(?:([+-])(\d+))?"
        match = re.fullmatch(pattern_short, clean_expr)

        if not match:
            return err(ParseError(
                message="Espressione dadi non valida",
                type="dice_expression",
                default="1d6"
            ))

        quantity = 1
        sides = int(match.group(1))
        sign = match.group(2)
        bonus_val = int(match.group(3)) if match.group(3) else 0

        bonus = bonus_val if sign != "-" else -bonus_val
        return ok((quantity, sides, bonus))

    quantity = int(match.group(1))
    sides = int(match.group(2))
    sign = match.group(3)
    bonus_val = int(match.group(4)) if match.group(4) else 0

    bonus = bonus_val if sign != "-" else -bonus_val

    return ok((quantity, sides, bonus))


def roll(quantity: int, sides: int, bonus: int = 0) -> Result[DiceRollResult, ValidationError]:
    g1 = guard(quantity > 0, ValidationError(
        message="La quantità deve essere > 0",
        field="quantity",
        value=quantity
    ))
    if isinstance(g1, Err):return g1

    g2 = guard(sides > 0, ValidationError(
        message="Il numero di facce deve essere > 0",
        field="sides",
        value=sides
    ))
    if isinstance(g2, Err):
        return g2

    rolls = [roll_single(sides) for _ in range(quantity)]
    total = sum(rolls) + bonus

    sign = "+" if bonus >= 0 else "-"
    expression = f"{quantity}d{sides}"
    if bonus != 0: expression += f" {sign} {abs(bonus)}"

    result: DiceRollResult = {
        "total": total,
        "rolls": rolls,
        "expression": expression,
        "bonus": bonus,
    }

    return ok(result)


def roll_dice(expression: str) -> Result[DiceRollResult, ParseError | ValidationError]:
    parsed = parse_dice_expression(expression)
    if isinstance(parsed, Err): return parsed
    quantity, sides, bonus = parsed.unwrap()
    return roll(quantity, sides, bonus)