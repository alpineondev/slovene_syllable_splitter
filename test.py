from slovene_syllable_splitter import create_syllables, get_vowel_graphemes
from slovene_phoneme_syllable_splitter import syllabize_phonemes

syllabize_graphemes = lambda word: create_syllables(word, get_vowel_graphemes())


def test():
    for word_gra, word_pho in [
        ("dandanašnji", "d a n d a n a S n j i"),
        ("lebervračko", "l E b @ r w r a tS k O"),
        ("neizbrisljivih", "n E i z b r i s l j i v i x"),
        ("ahmadovih", "a x m a d O v i x"),
        ("a", "a"),
        ("lebensphilosophie", "l E b @ n s f i l O s o f i j E"),
        ("lebingerja", "l E b i N g e r @ j a"),
        ("rja", "@ r j a"),
        ("abadenarnico", "a b a d E n a r @ n i ts O"),
    ]:
        syll_gra = syllabize_graphemes(word_gra)
        syll_pho = syllabize_phonemes(word_pho)
        print(f"{'|'.join(syll_gra)}\t{'|'.join(syll_pho)}")


test()
