# Regul
```
    regex := | 
            expr regex

    expr := 
        expr+   |
        expr?   |
        expr*   |
        expr expr   |
        expr | expr |
        ( expr )    |
        expr { sizing } |
        .
        ^
        $
        [ item ]
        [ ^item ]
        

    sizing :=  |
            digit ,     |
            , digit     |
            digit , digit

    item := item |
            item item |
            range |
            ch

    range := ch-ch

    ch := *
    digit := digit digit | 0~9
```

# Resolve ambiguity
```
    regex := | 
            expr regex

    expr := expr-union

    expr-union := expr-post  |
        expr-post | expr
    
    expr-post := expr-prim expr-unary |
                 expr-prim expr-size
                    
    expr-size := { sizing }

    unary-oprator := |
        +   | 
        ?   |
        *

    expr-prim := 
        expr-group        |
        expr-any          |
        expr-set          |
        ch

    expr-group := ( expr ) 
   
    expr-any := .
   
    expr-set := 
        [ item ]        | 
        [^ item ]       | 

    sizing :=  |

            digit ,     |
            , digit     |
            digit , digit

    item := |
            range item |
            ch item

    range := ch-ch

    ch := *
    digit := digit digit | 0~9
```