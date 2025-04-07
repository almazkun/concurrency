# Python and concurrency
from https://newvick.com/posts/python-concurrency/

```python
if cpu_intensive:
  'processes'
else:
  if suited_for_threads:
    'threads'
  elif suited_for_asyncio:
    'asyncio'
```