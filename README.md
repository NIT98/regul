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