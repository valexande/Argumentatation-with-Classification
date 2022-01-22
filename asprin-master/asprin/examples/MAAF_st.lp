% Run with: ../exec/clingo5_4 MAAF_cf.lp input.lp 0

% Every answer set produced is a cf/ad/co-extension


%%%%%%%%%%%%%%%%%%%%%
% Conflict free Extension (Def 3)

% Generate all possible extensions
{cf_extension(A) : argument(A)}.

:- cf_extension(A1), 
  cf_extension(A2), 
  attacks(A1, A2, conflict).


%%%%%%%%%%%%%%%%%%%%%
% Stable Extension (Def 8)
#preference(p1,more(cardinality)){cf_extension(A)}.
#optimize(p1).


other(A) :- argument(A), not cf_extension(A).

:- other(A), cf_extension(B), attacks(B,A, defending).

#show cf_extension/1.


