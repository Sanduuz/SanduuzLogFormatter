# Sanduuz Log Formatter (SLF)

Sanduuz Log Formatter is a custom log formatter for the python logging library.

### Installation

SLF can now be installed through the [Python Package Index](https://pypi.org/project/sanduuzlogformatter/):

`python3 -m pip install sanduuzlogformatter`

### Usage:

```python
import logging
from sanduuzlogformatter import SLF

formatter = SLF()

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)

logger.info("This is a message from SLF!")
```

### Features:

A custom date format can be given to the formatter during initialization:

```python3
formatter = SLF(datefmt="%Y-%m-%d")
```

A custom maximum length for the info section `| module:function:linenumber |` can be given to the formatter during initialization:

```python3
formatter = SLF(info_section_max_length=75)
```
