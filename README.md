# [Kalkulator](https://github.com/xidus/kalk)

Af [Joachim](https://github.com/xidus)

Kalkulator er et kommandolinjeprogram, der hjælper brugeren med at lave de elementære regnearter.

## Installation

For at komme igang med at bruge programmet, skal du have Python installeret og dernæst installere programmet fra kommandolinjen:

```sh
(base) $ git clone https://github.com/xidus/kalk
(base) $ cd kalk
(base) $ git checkout 1.0.1
(base) $ mamba env create -f environment.yml
(base) $ mamba activate kalk
(kalk) $ python -m pip install -e .
(kalk) $
```

## Kommandolinje-eksempler

Nu kan programmet anvendes på følgende måde:

### Sum

```sh
(base) $ mamba activate kalk
(kalk) $ kalk sum 1 2 3 4
10
```

### Subtraktion

```sh
(kalk) $ kalk sub 1 2 3 4
-9
```

### Multiplikation

```sh
(kalk) $ kalk mul 1 2 3 4
24
```

---

## Bidrag

*   Fejl og ønsker kan oprettes som [GitHub issues](https://github.com/xidus/kalk/issues) på kodens adresse.
*   Kodeforslag kan oprettes gennem GitHubs forking- og pull-request-mekanisme:
    -   På kodearkivets side, vælg Fork
    -   Fra din egen fork, lav en by branch og foretag rettelserne i denne.
    -   Når du er klar, kan du oprette et pull-request fra den nye branch.

*   Andet? Se kontaktoplysninger nedenfor.

---

## Kontakt

*   Udvikler: <udvikler@example.com>
*   Kontor: <kontor@example.com>

