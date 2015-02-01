# goodreads-python

`goodreads-python` is a Python wrapper for [Goodreads](http://goodreads.com)
API.

## Getting started

To use `goodreads-python`, you need to register for a
[developer key](https://www.goodreads.com/api/keys). Using the API key and
secret (optional), you can create a `GoodreadsClient` object to be used for
further queries.

```python
import goodreads
gc = client.GoodreadsClient("sy1BoFti8To9YO2uUc2NQ",
                            "NwQZdMRrhdgYTdg81dZrPfrTeBIGqnBcqR6nbIPCMg")
```
