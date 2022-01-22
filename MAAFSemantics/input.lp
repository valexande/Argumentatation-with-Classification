
% Main domain predicates definitions
argument(a;b;c;d).

%%

% Problem instance
attacks(a,b, conflict).
attacks(a,c, conflict).

attacks(a,b, defending).
attacks(b,c, defending).
attacks(d,a, defending).