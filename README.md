# SmartDict
This is just like a normal dictionary except you don't need to define keys before adding values.

**For example:**

```python
sd = SmartDict()
sd['x']['y']['z'] = [1,2,3,4,5]
print sd #=> SmartDict({'x': SmartDict({'y': SmartDict({'z': [1, 2, 3, 4, 5]})})})
##################################################################################
sd = SmartDict()
for i in range(20):
  if i%2:
    sd['odd', list].append(i)
  else:
    sd['even', list].append(i)
print sd #=> SmartDict({'even': [0, 2, 4, 6, 8, 10, 12, 14, 16, 18], 'odd': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]})
```
