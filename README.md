# Luogu_difficulty
ͳ�������Ѷȡ�

ʹ��requests��

Example:

```Python
import src.Luogu_diff as diff


def main():
	someone = diff.user(37617)
	times = [0, 0, 0, 0, 0, 0, 0, 0]

	for p in someone.done_problems:
		print("%s:%s" % (p, p.difficulty))
		if p.difficulty<8:
			times[p.difficulty] = times[p.difficulty] + 1
		else:
			times[7] = times[7] + 1
	i = 0
	for n in times:
		print("%s:%s" % (diff.diff_name[i], n))
		i = i + 1

main()

```
ʹ��src.Luogu_diff.Debug_mode()

## License

MIT License