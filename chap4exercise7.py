# Rewrite the grade program from the previous chapter using
# a function called computegrade that takes a score as its parameter and
# returns a grade as a string.

def computeGrade(score):
    """
    This function takes a score and
    returns a grade as a string.
    e.g.
    Score Grade
    >= 0.9  A
    >= 0.8  B
    >= 0.7  C
    >= 0.6  D
    < 0.6   F
    others  Bad score
    """
    try:
        type(score) == float

        if 0.9 <= score <= 1.0:
            print("A")
        elif score >= 0.8:
            print("B")
        elif score >= 0.7:
            print("C")
        elif score >= 0.6:
            print("D")
        elif score >= 0.0:
            print("F")
        else:
            print("Bad score")
    except:
        print("Bad score")

computeGrade(0.5)