# Luogu_difficulty
统计做题难度。

使用requests库

Example:

```Python
import Luogu_diff

problems = search(用户ID)
i = 0
for p in problems:
	print("%s:%s" % (Luogu_diff.diff_name[i], p))
	if(i>7):
		continue
	i = i + 1

```

## License

MIT License