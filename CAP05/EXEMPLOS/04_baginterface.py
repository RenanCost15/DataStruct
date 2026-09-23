"""Capítulo 5 — baginterface.py, p. 132–133 (PDF p. 150–151)."""
class BagInterface(object):
    """Interface para todos os tipos de bag."""
    def __init__(self, sourceCollection=None): pass
    def isEmpty(self): return True
    def __len__(self): return 0
    def __str__(self): return ""
    def __iter__(self): return None
    def __add__(self, other): return None
    def __eq__(self, other): return False
    def count(self, item): return 0
    def clear(self): pass
    def add(self, item): pass
    def remove(self, item): pass
