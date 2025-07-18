def printMAT(mat: list[list[int]]) -> None:

    for r in range(len(mat)):

        for c in range(len(mat[r])):
            print(f"{mat[r][c]:<5}", end="")

        print("\n")