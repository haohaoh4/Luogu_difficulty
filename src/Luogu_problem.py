import requests
import logging
logger = logging.getLogger(__name__)


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
		req = requests.request("get", "http://www.luogu.org/problemnew/show/%s" % self.pid)
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
		logger.ERROR("incoming")
		raise Exception("incoming")
