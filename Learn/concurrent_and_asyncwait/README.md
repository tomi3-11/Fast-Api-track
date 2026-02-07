# Concurrency and Async wait
You can use `await` like this in third party libraries.
```python
results = await some_library()
```

then if you want to declare you path function with `async def` do it this way

```python
@app.get('/')
async def read_results():
    results = await some_library()
    return results
```

> Note
> You can only use `await` inside of a function created with `async def`.

In situations of using a third party that communicates with something (a database, an API, the filesystem, etc) and doesn't have support for using `await`, (this is currently the case for most database libraries) then declare your path operation functions as normarlly, with just `def`, like
```python
@app.get('/')
def results():
    results = some_library()
    return results
```
