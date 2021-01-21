def staircase(n):
    # Base Case - minimum steps possible and number of ways the child can climb them

    # Inductive Hypothesis - ways to climb rest of the steps

    # Inductive Step - use Inductive Hypothesis to formulate a solution
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return staircase(n-1)+staircase(n-2)+staircase(n-3)
