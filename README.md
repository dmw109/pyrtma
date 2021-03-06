# pyrtma
RTMA client written in python with no external dependencies. Supports the most used features only.

## Install
From root directory of the repo:
```shell
$ pip install .
```
## Usage
Create a module:
```python
import pyrtma

mod = pyrtma.rtmaClient()
mod.Connect('127.0.0.1:7111')
```

See /examples for pub/sub use case:

In one terminal run: 
```shell
$ python example.py --pub
```

And from another run: 
```shell
$ python example.py --sub
```

Bench testing utility: 
```shell
$ python testing/rtma_bench.py -h
usage: rtma_bench.py [-h] [-ms MSG_SIZE] [-n NUM_MSGS] [-np NUM_PUBLISHERS]
                     [-ns NUM_SUBSCRIBERS] [-s SERVER]

rtmaClient bench test utility

optional arguments:
  -h, --help           show this help message and exit
  -ms MSG_SIZE         Messge size in bytes.
  -n NUM_MSGS          Number of messages.
  -np NUM_PUBLISHERS   Number of concurrent publishers.
  -ns NUM_SUBSCRIBERS  Number of concurrent subscribers.
  -s SERVER            RTMA message manager ip address (default:
                       127.0.0.1:7111)
```
