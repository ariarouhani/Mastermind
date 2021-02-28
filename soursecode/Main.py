
import soursecode.AI.ai as ai

from soursecode.model.letters import Letters
from soursecode.model.board import Board


b1 = Board()
l1 = Letters()

ai.fill_spot(l1, b1)
print(b1.spot)  # TODO remove the debug line
