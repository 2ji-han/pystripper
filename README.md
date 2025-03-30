# pystripper

pythonコードを型ヒントのみを含んだ.pyiとコードのみの.pyに分割するツールです。

## 使い方

```bash
pip install pystripper
python -m pystripper --help

Usage: python -m pystripper [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  strip      Strip the input file and save it to the output file.
  strip-dir  Strip all files in the input directory and save them to the output directory.
```

## TODO

- [ ] docstringの抽出に対応
- [ ] minifyの選択を追加
