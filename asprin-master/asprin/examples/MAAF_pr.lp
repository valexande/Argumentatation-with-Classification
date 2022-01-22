% Run with: ../exec/clingo5_4 MAAF_ad.lp input.lp 0

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
% Preferred Extension (Def 7)

#preference(p1,more(cardinality)){ad_extension(A)}.
#optimize(p1).

#show ad_extension/1.