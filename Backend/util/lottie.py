import re
from .coin import CoinResult
from .dice import DiceRollResult
from typing import List, Dict, Any
LOTTIE_ASSETS = {
    "dice": {
        4: "lottie/dice/d4.json",
        6: "lottie/dice/d6.json",
        8: "lottie/dice/d8.json",
        10: "lottie/dice/d10.json",
        12: "lottie/dice/d12.json",
        20: "lottie/dice/d20.json",
        100: "lottie/dice/d100.json",
    },
    "coin": "lottie/coin/flip.json"
}

def get_dice_ui_metadata(result: DiceRollResult) -> Dict[str, Any]:
    quantity = len(result["rolls"])
    
    sides_match = re.search(r"d(\d+)", result["expression"])
    sides = int(sides_match.group(1)) if sides_match else 0
    
    description = f"Lancio di {quantity} {'dado' if quantity == 1 else 'dadi'} da {sides}"
    
    dice_details = []
    for val in result["rolls"]:
        dice_details.append({
            "sides": sides,
            "value": val,
            "lottie_path": LOTTIE_ASSETS["dice"].get(sides, "lottie/dice/generic.json")
        })
        
    bonus = result["bonus"]
    bonus_display = ""
    if bonus != 0: bonus_display = f"{'+' if bonus > 0 else '-'} {abs(bonus)}"

    rolls_str = " + ".join(map(str, result["rolls"]))
    formula = rolls_str
    if bonus != 0: formula += f" {'+' if bonus > 0 else '-'} {abs(bonus)}"
    
    return {
        "description": description,
        "dice": dice_details,
        "bonus_display": bonus_display,
        "total_display": f"= {result['total']}",
        "formula": f"{formula} = {result['total']}",
        "quantity": quantity,
        "sides": sides
    }

def get_coin_ui_metadata(result: CoinResult) -> Dict[str, Any]:
    return {
        "description": "Lancio della moneta",
        "result_text": result.value, # "Testa" o "Croce"
        "lottie_path": LOTTIE_ASSETS["coin"],
        "is_heads": result == CoinResult.HEADS
    }
