# calculate descriptors

## やること

- sdf から mordred で記述子を計算し、csv と結合して返す

## やらないこと

- コンフォーマーの計算

## 仕様

```shell
$ python main.py structure.sdf label.csv -o output.csv
```

## テスト

```shell
 $ python -m unittest discover tests
```
