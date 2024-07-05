import pkg_resources
from symspellpy import SymSpell

import clipboarder

def fix_spelling(word):
    # see: https://symspellpy.readthedocs.io/en/latest/examples/lookup_compound.html
    sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
    dictionary_path = pkg_resources.resource_filename(
        "symspellpy", "frequency_dictionary_en_82_765.txt"
    )
    sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)

    suggestions = sym_spell.lookup_compound(word, max_edit_distance=2, transfer_casing=True)

    return suggestions[0].term

if __name__ == "__main__":
    clipboarder.run(fix_spelling)
