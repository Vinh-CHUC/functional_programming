-module(lambda_calculus_erl).
-compile(export_all).

foo() ->
    F=fun(X, Y) ->
        fun(F) -> F(X, Y) end
    end.
