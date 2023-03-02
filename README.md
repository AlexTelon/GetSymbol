# Utility to find Unicode symbols

Uses LLM's to get the symbols you are looking for.

You need an openai key to use this. Usage is not free but it is cheap. But check the [pricing](https://beta.openai.com/pricing) before you use it.

## Setup

```shell
# Download an openai key and do one of these things:
#  1. store it in a file called .openai_key.secret
#  2. set the OPENAI_API_KEY environment variable
> pip install .
```

The tool should work like this:

```shell
> getsymbol arrows
⇐ ⇑ ⇒ ⇓ ⇔ ⇕ ⇖ ⇗ ⇘ ⇙ ⇚ ⇛ ⇜ ⇝ ⇞ ⇟
> getsymbol degrees
° ℃ ℉
> getsymbol letters with dots over them
̇a ̇b ̇c ḍe ḥf ḳg ḷh ṃi ṇj ṛk ṣl ṭm ̇n ̇o ̇p ̇q ṡr ṭu ṿw ẋx ẏy ̣z
̇A ̇B ḌC ḤD ḲE ḶF ṂG ṆH ṚI ṢJ ṬK ̇L ̇M ̇N ̇O ̇P ̇Q ṢR ṬU ṾV ẊW ẎX ẒY
$ getsymbol pirate
⚓️🏴‍☠️
```

It is not perfect. First the language model is instructed to only respond with symbols (as opposed to free flowing english, but you might still get text and not just symbols).

For me country flags are not shown properly but I wont pretend I know this is the tool or my terminal's fault.