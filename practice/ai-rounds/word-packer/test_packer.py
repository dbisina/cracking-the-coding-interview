from bits import mask_of
from packer import best_pack
from words import normalize


def test_mask_rejects_repeated_letters():
    assert mask_of("book") is None
    assert mask_of("bok") == (1 << 1) | (1 << 14) | (1 << 10)


def test_normalize():
    assert normalize("  Hello-World! ") == "helloworld"


def test_all_disjoint():
    assert best_pack(["ab", "cd", "ef"]) == 6


def test_empty():
    assert best_pack([]) == 0


def test_words_with_repeats_are_ignored():
    assert best_pack(["aa", "bc"]) == 2


def test_skipping_an_early_word_wins():
    assert best_pack(["ab", "cd", "cdefgh"]) == 8


def test_pick_best_combination():
    assert best_pack(["un", "iq", "ue"]) == 4
    assert best_pack(["cha", "r", "act", "ers"]) == 6
