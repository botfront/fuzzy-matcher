# Fuzzy Matcher

A super simple MIT licensed fuzzy matching library to be used as an MIT alternative to Fuzzy Wuzzy which is GPL licensed.
It is much less featured as Fuzzy Wuzzy, so if GPL is not blocking you, you should probably use Fuzzy Wuzzy instead.

## Usage

```python
from fuzzy_matcher import process
query = "orange"
val = ['blue', 'orange', 'brown', 'ornage', 'range', 'angel', 'gang', 'ang']
fuzzy = process.extract(query, val, limit=3, scorer='ratio')
```

should output:
```python
[('orange', 100), ('range', 83), ('ornage', 66)]
```

### Supported scorers

Only `ratio` and `partial_ratio` are supported at this time.
Note that scores will not be the same as FuzzyWuzzy's. 