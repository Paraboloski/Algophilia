import random
from enum import Enum

class CoinResult(str, Enum):
    HEADS = "Testa"
    TAILS = "Croce"

def flip_coin() -> CoinResult: return random.choice(list(CoinResult))
