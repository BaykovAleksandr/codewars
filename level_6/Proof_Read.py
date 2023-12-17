import pytest


def proofread(st):
    """You've just finished writing the last chapter for your novel when a virus suddenly infects your document. It has
    swapped the 'i's and 'e's in 'ei' words and capitalised random letters. Write a function which will:
    a) remove the spelling errors in 'ei' words. (Example of 'ei' words: their, caffeine, deceive, weight)
    b) only capitalise the first letter of each sentence. Make sure the rest of the sentence is in lower case.
    Example: He haD iEght ShOTs of CAffIEne. --> He had eight shots of caffeine."""
    a = list(st.split('. '))

    res = []
    for sentence in a:
        res.append(f"{sentence.capitalize().replace('ie', 'ei').replace('Ie', 'Ei')}")
    return '. '.join(res)


@pytest.mark.parametrize('text, result', [("SHe wEnt CaNoIenG.", "She went canoeing."),
        ("He haD iEght ShOTs of CAffIEne", "He had eight shots of caffeine"),
        ("THe neIghBour's ceiLing FEll on His Head. The WiEght of It crusHed him To thE gROuNd.", "The neighbour's "
                                                                                                  "ceiling fell on "
                                                                                                  "his head. The "
                                                                                                  "weight of it "
                                                                                                  "crushed him to the "
                                                                                                  "ground."),
        ("ThE kiDs enJoYEd the SLiegh RidE.", "The kids enjoyed the sleigh ride."),
        ("", "")

])
def test_solution(text, result):
    assert proofread(text) == result
