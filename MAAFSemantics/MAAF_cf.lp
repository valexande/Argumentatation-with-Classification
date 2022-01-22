% Run with: ../exec/clingo5_4 MAAF_cf.lp input.lp 0

% Every answer set produced is a cf/ad/co-extension


%%%%%%%%%%%%%%%%%%%%%
% Conflict free Extension (Def 3)

% Generate all possible extensions
{cf_extension(A) : argument(A)}.

:- cf_extension(A1), 
  cf_extension(A2), 
  attacks(A1, A2, conflict).


#show cf_extension/1.


