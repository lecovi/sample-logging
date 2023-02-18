# sample-logging
A simple Python app to show how to use Python Logging module

# Usage

```bash
$ python3 cli.py
```

## Explanation

- [Main](/../../main/cli.py): Logger is everywhere, but not working as expected. Why?
    - When we are [getting the logger](/../../main/cli.py#L9), we are passing `__name__` as the name of the logger.
    - The `__name__` is the name of the module, in this case, `__main__` because we are running the script directly.
- [With Print and Logger](/cli.py): Logger is working as expected and we are using `print` to show the message.
    - We are [getting the logger](/cli.py#L9) with the name of the package `src`.
- [With Logger Module](/../../feature/with-logger-module/cli.py): Logger is working as expected and we removed `print` calls.
    - We are [getting the logger](/../../feature/with-logger-module/src/logger.py#L3) with the name of the package `src`.
    - We are [importing the logger](/../../feature/with-logger-module/cli.py#L1) from the `src/logger.py` module.