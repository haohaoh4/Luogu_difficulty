import requests
import logging
logger = logging.getLogger(__name__)

header = {
	'Host': 'www.luogu.org',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Language': 'zh-CN,zh;q=0.8',
	'Accept-Encoding': 'gzip, deflate',
	'Referer': 'http://www.baidu.com',
	'Connection': 'keep-alive',
	'Cache-Control': 'max-age=0',
}


class Problem:
	pid = ""
	name = ""
	difficulty = 7
	passed = 0
	summit = 0

	def __init__(self, problem_id, full_data=False):
		self.pid = problem_id
		self.get_base_info()
		if full_data:
			self.get_extra()

	def __str__(self):
		return self.pid
		# return self.pid + " " + self.name
		# It's uncompleted.

	def get_base_info(self):
		diff_name = {0: "入门难度", 1: "普及-", 2: "普及/提高-", 3: "普及+/提高", 4: "提高+/省选-", 5: "省选/NOI-", 6: "NOI/NOI+/CTSC", 7: "ERROR"}
		req = requests.get("http://www.luogu.org/problemnew/show/%s" % self.pid, headers=header)
		if str(req) != "<Response [200]>":
			raise IOError("Can't access to Luogu %s." % ("http://www.luogu.org/problemnew/show/%s" % self.pid))
		req = req.content.decode('utf-8')
		i = 0
		for string in diff_name:
			if req.find(diff_name[string]) != -1:
				break
			i = i + 1
		if i > 7:
			self.difficulty = 7
		else:
			self.difficulty = i

	def get_extra(self):
		logger.error("incoming")
		raise Exception("incoming")
