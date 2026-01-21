# Sequence diagram 

```mermaid
sequenceDiagram
    actor Main
    participant Input as input() -> str
    participant Normalize as normalize(value: str) -> str 
    participant Check as check(value: str) -> bool
    participant Get price as get_price(price: float, weight: float) -> float
    Main ->>+ Input: Input price
    Input -->>- Main: price
    Main ->>+ Input: Input weight
    Input -->>- Main: weight
    Main ->>+ Normalize: Normalize price
    Normalize -->>- Main: price
    Main ->>+ Normalize: Normalize weight
    Normalize -->>- Main: weight
    Main ->>+ Get price: Get FULL price
    Get price ->>+ Check: Check price
    Get price ->>+ Check: Check weight
    alt Check
         Get price -->>- Main: price * weight
    else not Check
%%         Get price -->>- Main: Error message
    end
%%    Main ->>+ Check: Check price
%%    Check -->>- Main: price
%%    Main ->>+ Check: Check weight
%%    Check -->>- Main: weight
%%    Main ->>+ Get price: Get FULL price
%%    Get price -->>- Main: price * weight

```

```mermaid
sequenceDiagram
    actor Main
    participant Input as input() -> str
    participant Normalize as normalize(value: str) -> str 
    participant Check as check(value: str) -> bool
    participant GetPrice as get_price(price: float, weight: float) -> float

    Main ->>+ Input: Input price
    Input -->>- Main: price

    Main ->>+ Input: Input weight
    Input -->>- Main: weight

    Main ->>+ Normalize: Normalize price
    Normalize -->>- Main: price

    Main ->>+ Normalize: Normalize weight
    Normalize -->>- Main: weight

    Main ->>+ Check: Check price
    Check -->>- Main: true / false

    Main ->>+ Check: Check weight
    Check -->>- Main: true / false

    alt price and weight valid
        Main ->>+ GetPrice: Get FULL price
        GetPrice -->>- Main: price * weight
    else invalid input
        Main -->> Main: Error message
    end
```


# Sequence diagram 2 

```mermaid
sequenceDiagram
    actor Main
    participant Input
    participant Normalize
    participant Check
    participant Get price

    Main->>+Get price: Get FULL price
    Get price->>+Normalize: Input price
    Normalize->>+Input: GET price
    Input-->>-Normalize: Input price
    Normalize-->>-Get price: Normalize price
    
    Get price->>+Normalize: Input weight
    Normalize->>+Input: GET weight
    Input-->>-Normalize: Input weight
    Normalize-->>-Get price: Normalize weight
    
    Get price->>+Check: Input price and weight
    Check-->>-Get price: True or False
    Get price-->>-Main: Get FULL price

```