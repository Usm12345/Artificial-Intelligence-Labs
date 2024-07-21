from pyswip import Prolog

def main():
    # Initialize Prolog
    prolog = Prolog()

    # Load the Prolog file containing family facts and rules
    prolog.consult("family.pl")

    # Query family relationships
    for solution in prolog.query("parent(john, X)"):
        print(f"John is a parent of {solution['X']}.")

    for solution in prolog.query("parent(X, lisa)"):
        print(f"{solution['X']} is a parent of Lisa.")

if __name__ == "__main__":
    main()
