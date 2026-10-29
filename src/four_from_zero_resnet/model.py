"""
The model for four-from-zero-resnet.

a small ResNet (about 5 residual blocks, 64 channels) with a policy head over 7 columns
and a value head, plus Monte Carlo tree search with PUCT. Reuse the Connect Four engine
from blindfold-tfm.

forward() accepts return_cache=True and returns a dict of internal activations, and a
patch argument (or forward hooks) overwrites a named activation for interventions.
"""

# TODO: implement. See README.md for the plan.
