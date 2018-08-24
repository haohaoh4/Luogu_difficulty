import requests

diff_name = {0: "入门难度", 1: "普及-", 2: "普及/提高-", 3: "普及+/提高", 4: "提高+/省选-",
        5: "省选/NOI-", 6: "NOI/NOI+/CTSC", 7:"ERROR"}

def get_difficulty(pid):
	req = requests.request("get", "http://www.luogu.org/problemnew/show/%s" % pid)
	if (str(req) != "<Response [200]>"):
		raise IOError("Can't access to Luogu.")
	req = req.content.decode('utf-8')
	i = 0
	for string in diff_name:
		if (req.find(diff_name[string])!=-1):
			break
		i = i + 1
	#print(i)
	if(i>7):
		return 7
	#times[i] = times[i] + 1
	return i


def search(uid):
	req = requests.request("get", "http://www.luogu.org/space/show?uid=%s" % uid)
	if (str(req) != "<Response [200]>"):
		raise IOError("Can't access to Luogu.")
	req = req.content.decode('utf-8')
	f = "[<a data-pjax href="
	begin = 0
	times = [0, 0, 0, 0, 0, 0, 0, 0]
	while (1):
		begin = req.find(f, begin)
		begin = begin + 38
		end = req.find("\">", begin)
		if (req[begin:end] == "<head>\n<meta charset=\"utf-8"):
			break
		d = get_difficulty(req[begin:end])
		times[d] = times[d] + 1
	return times
