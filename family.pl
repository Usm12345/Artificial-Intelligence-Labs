% Prolog facts and rules for family relationships

father(john, jim).
father(john, ann).
father(jim, lisa).
father(jim, michael).

mother(jane, jim).
mother(jane, ann).
mother(ann, lisa).
mother(ann, michael).

parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).
