# Utility to find Unicode symbols

Uses LLM's to get the symbols you are looking for.

You need an openai key to use this. Usage is not free but it is cheap. But check the [pricing](https://beta.openai.com/pricing) before you use it.

Remember this is a language model so you never really know what it will return. You might ask for the USD symbol expecting `$` but get `💲 🇺 🇸 💹`which is close but probably not what you really wanted.


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
getsymbol --one arrows
➡️
```

It is not perfect. First the language model is instructed to only respond with symbols (as opposed to free flowing english, but you might still get text and not just symbols).

For me country flags are not shown properly but I wont pretend I know unicode and utf to know where the issue really is.

## Costs


A simple request for "arrows" that returns "← ↓ ↑ →" would with the current prompt be 51 tokens.
As of today (2023-03-04) it is 0.02\$ per 1000 tokens. See [pricing](https://beta.openai.com/pricing) for current pricing information.

51 / 1000 * 0.02 = 0.00102\$
If all requests are like this then 980 of them would cost 1\$.