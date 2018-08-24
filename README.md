# Luogu_difficulty
统计做题难度。

使用requests库

Example:

```Python
import src.Luogu_diff as diff


def main():
	someone = diff.user(120380)
	times = [0 in range(0, 9)]

	for p in someone.done_problems:
		print("%s:%s" % (p, p.difficulty))
		times[p.difficulty] = times[p.difficulty] + 1
	i = 0
	for n in times:
		print("%s:%s %s" % (diff.diff_name[i], n))
		i = i + 1

main()

```

## License

MIT License