# Group Management

Create and manage groups of objects.

## Creating Groups

```python
cad.create_group("MyGroup", [circle, line, rectangle])
```

## Adding to Groups

```python
cad.add_to_group("MyGroup", new_circle)
```

## Removing from Groups

```python
cad.remove_from_group("MyGroup", circle)
```

## Selecting Groups

```python
cad.select_group("MyGroup")
```

## See Also

- [Object Creation](object-creation.md)
- [Layer Management](layers.md)
