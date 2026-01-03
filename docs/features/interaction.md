# User Interaction

Get input from users during script execution.

## Request Point

Get a point selection from the user:

```python
point = cad.request_point("Click a point in the drawing")
print(f"Selected: {point}")
```

## Request String

Get text input from the user:

```python
name = cad.request_string("Enter object name")
print(f"Name: {name}")
```

## Request Integer

Get numeric input from the user:

```python
count = cad.request_int("How many objects?")
print(f"Count: {count}")
```

## See Also

- [Quick Start](../getting-started/quickstart.md)
