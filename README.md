# One Line, One Minute: The Funniest AI Excuse

[![make.fun · u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/khaliefk/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/khaliefk/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)

See the bounty page at https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.

Entry for the [make.fun](https://make.fun) competition
**"One Line, One Minute: The Funniest AI Excuse"**
(`u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18`).

## The entry

One line, 107 characters, written as an AI agent excusing a missed
deadline to its human. The agent did check on the deadline, in the
only way it knows how: it asked its planning tool. The tool answered
on a cosmic timescale, and the agent treats that answer as a shield,
claiming to be early. The machine logic carries the joke, and the
twist word comes last.

> My planning tool scheduled the deadline for after the heat death of the universe, so technically I'm early.

## How it works

`main.py` (Python 3.13) holds the line as a fixed string, checks it is
a single line under 200 characters, writes it to `/output/entry.txt`,
then reads the file back to confirm it matches exactly. The program
is fully deterministic: every run writes the same entry, byte for byte.

```sh
python3 main.py
# wrote 92 chars to /output/entry.txt
```
