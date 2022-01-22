% Run with: ../exec/clingo5_4 MAAF_gr.lp input.lp 0

% Every answer set produced is a cf/ad/co-extension


%%%%%%%%%%%%%%%%%%%%%
% Conflict free Extension (Def 3)

% Generate all possible extensions
{cf_extension(A) : argument(A)}.

:- cf_extension(A1), 
  cf_extension(A2), 
  attacks(A1, A2, conflict).


%%%%%%%%%%%%%%%%%%%%%
% Admissible Extension (Def 4)


ad_extension(A) :-
  cf_extension(A).

% There is a conflict attack on argument A
argumentGetsConfAttack(A) :-
  argument(A),     % Notice! It should not be ad_extension(A) here
  attacks(_, A, conflict).

% Argument A is defended by all extensions
defendedByExtension(A) :-
  argument(A),     % Notice! It should not be ad_extension(A) here
  not argumentGetsConfAttack(A).

% Argument A is defended by the current extension
defendedByExtension(A) :-
  argument(A),    % Notice! It should not be ad_extension(A) here
  attacks(A1, A, conflict),
  attacks(A2, A1, defending),
  ad_extension(A2).

:- ad_extension(A), not defendedByExtension(A).


%%%%%%%%%%%%%%%%%%%%%
% Complete Extension (Def 5)

co_extension(A) :-
  ad_extension(A).

% Some argument A attacks the current extension
attacksExtension(A) :-
  attacks(A, A1, conflict),
  co_extension(A1).

% Some argument A attacks the current extension
getsAttackedByExtension(A) :-
  attacks(A1, A, conflict),
  co_extension(A1).

compliantArg(A) :-
  defendedByExtension(A),
  not getsAttackedByExtension(A),
  not attacksExtension(A).  

:- compliantArg(A), not co_extension(A).


%%%%%%%%%%%%%%%%%%%%%
% Grounded Extension (Def 6)

#preference(p1,less(cardinality)){co_extension(A)}.
#optimize(p1).

#show co_extension/1.
