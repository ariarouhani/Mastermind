
import random

from soursecode.model.letters import Letters
from soursecode.model.board import Board


def fill_spot(l1: Letters, b1: Board):

    for i in range(len(b1.spot)):
        b1.spot[i] = l1.alphabet[random.randrange(0, len(l1.alphabet))]
