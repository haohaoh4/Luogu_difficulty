# Luogu_difficulty
统计做题难度。

使用requests库

Example:

```Python
diff = {0: "入门难度", 1: "普及-", 2: "普及/提高-", 3: "普及+/提高", 4: "提高+/省选-",
        5: "省选/NOI-", 6: "NOI/NOI+/CTSC", 7:"ERROR"}

problems = search(用户ID)
i = 0
for p in problems:
	print("%s:%s" % (diff[i], p))
	if(i>7):
		continue
	i = i + 1
```

## License

MIT License