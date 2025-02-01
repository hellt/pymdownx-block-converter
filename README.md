# pymdownx-block-converter

PyMdown Extension v9.10+ introduces a new way to define [blocks](https://facelessuser.github.io/pymdown-extensions/extensions/blocks/), which you might know under the following names:

* admonitions
* details
* tabs

The new syntax improves the readability of the markdown source and allows for more flexibility. However, you might already have a lot of markdown files that use the old syntax. This repo contains a [script](main.py) by [@tiangolo](https://github.com/tiangolo) packaged in a container that converts the old syntax to the new one across all your doc base or just a single file.

**Limitations**:

1. The script doesn't handle **nested** tabs conversion at this moment.
2. The script doesn't handle details blocks defined as `!!!+` at this moment.

## Usage

It is always a good idea to first run the script against a single file to see if it works as expected. To do so, run the following command:

```bash
sudo docker run --rm -v $(pwd)/path/to/file.md:/docs/test.md \
     ghcr.io/hellt/pymdownx-block-converter:0.1.0
```

To convert the whole doc base that is typically contained in the `docs` folder, run the following command:

```bash
sudo docker run --rm -v $(pwd)/docs:/docs \
     ghcr.io/hellt/pymdownx-block-converter:0.1.0
```
