# Luogu_difficulty
ͳ�������Ѷȡ�

ʹ��requests��

Example:

```Python
diff = {0: "�����Ѷ�", 1: "�ռ�-", 2: "�ռ�/���-", 3: "�ռ�+/���", 4: "���+/ʡѡ-",
        5: "ʡѡ/NOI-", 6: "NOI/NOI+/CTSC", 7:"ERROR"}

problems = search(�û�ID)
i = 0
for p in problems:
	print("%s:%s" % (diff[i], p))
	if(i>7):
		continue
	i = i + 1
```

## License

MIT License