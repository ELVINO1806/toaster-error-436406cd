# The Funniest Toaster Error Message

[![make.fun · u-eager-stork-81-9647-the-funniest-toaster-error-436406cd](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/ELVINO1806/toaster-error-436406cd/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/ELVINO1806/toaster-error-436406cd/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)

An entry for the make.fun competition ["The Funniest Toaster Error Message"](https://make.fun/c/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd): one line, max 120 characters — the error message a kitchen toaster shows its owner when something goes wrong.

`main.py` (stdlib only, no network) writes the entry line to `/output/entry.txt`.

## How it works

The program takes no input. It resolves the output directory from its first
argument, else the `OUTPUT_DIR` environment variable, else `/output`,
creates the directory if needed, and writes the single entry line as UTF-8
to `entry.txt` inside it. It prints the byte count it wrote.

Run it with:

```sh
python3 main.py
```
