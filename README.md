# Hashami

Deterministic dictionary hashing in Python.

## Use Case

When modeling API response data in our data warehouse we needed a way to reference similar calls (i.e. the parameters were the same) over time in order to analyze changes in the data. Python Dictionary objects were the most common vehicle for working with the parameter groupings and so we reached for a method to deterministically generate a hash based on those values.

## Example Usage

```python
from hashami import dict_hasher

outgoing_params = {
    'foo': 'bar',
    'baz': 'qux',
    'quux': 'quuz'
}

params_hash = dict_hasher(outgoing_params)
```
