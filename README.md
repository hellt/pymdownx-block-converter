# pymdownx-block-converter

PyMdown Extension v9.10+ introduces a new way to define
[blocks](https://facelessuser.github.io/pymdown-extensions/extensions/blocks/),
which you might know under the following names:

* admonitions
* details
* tabs

The new syntax improves the readability of the Markdown source and allows for
more flexibility. However, you might already have a lot of Markdown files that
use the old syntax.

This repo contains a [script](main.py) created by [@tiangolo](https://github.com/tiangolo)
to update Markdown block syntax (per [sqlmodel#712](https://github.com/fastapi/sqlmodel/pull/712)
, [sqlmodel#713](https://github.com/fastapi/sqlmodel/pull/713), and
[pymdown-extensions#1973](https://github.com/facelessuser/pymdown-extensions/discussions/1973)
). Additionally, this script is packaged in a container allowing conversion from
the old block syntax to the new one across your entire documentation base or
just a single file.

## Supported Syntax

* Admonitions declared with `!!!`
  * including those with varied spacing around the _type_
* Details declared with HTML tags
  * with and without &lt;summary/> tags
* Details declared with `???`, including the open attribute with `???+`
  * again, with and without a summary
* Tabs with `===`

**Limitations**:

1. The script doesn't handle **nested** tabs conversion at this moment.

## Usage

> [!IMPORTANT]
> It is always a good idea to first run the script against a single file to see
> if it works as expected.
>
> :sparkles: To do so, first determine whether to run the container or locally
> run the script.

### Container

#### Container Volume Mount Single File

To volume mount a specific file and fallback to pattern matching _/docs/*.md_:

```bash
sudo docker run --rm -v $(pwd)/path/to/file.md:/docs/test.md \
     ghcr.io/hellt/pymdownx-block-converter
```

#### Container Volume Mount Directory

To convert the whole documentation base that is typically contained in the
`docs` folder (uses fallback to _/docs/*.md_), run the following command:

```bash
sudo docker run --rm -v $(pwd)/docs:/docs \
     ghcr.io/hellt/pymdownx-block-converter
```

#### Container Volume Mount Directory, but Only Execute on Single File

To volume mount a directory, but only execute against a single file:

```bash
sudo docker run --rm -v $(pwd)/docs:/docs \
     ghcr.io/hellt/pymdownx-block-converter /docs/path/to/test.md
```

### Local Execution without Container

While there's nothing wrong with containers, it is possible to locally run the
script.

#### Local Execution on Single File

#### Local Execution on Single File

Local execution against a single file:

```bash
python block_conv.py /path/to/test.md
```

#### Local Execution on Directory

Local execution against a directory (utilizes globbing):

```bash
python block_conv.py /path/to/
```

#### Local Execution using Fallback

Running the script without a file or path argument fallsback and runs against
_/docs/*.md_ in (to remain backwards compatible with the container's
Dockerfile).

```bash
python block_conv.py
```
