import requests
from src.Luogu_problem import Problem

diff_debug = False
class user:
	uid = 0
	name = ""
	done_problems = []
	done_difficulty = [0 in range(0, 8)]
	rating = 0

	def __init__(self, uid):
		self.uid = uid
		self.get_base_info()

	def __str__(self):
		return self.name

	def get_base_info(self):
		req = requests.request("get", "http://www.luogu.org/space/show?uid=%s" % self.uid)
		req = requests.get("http://www.luogu.org/space/show?uid=%s" % self.uid)
		if str(req) != "<Response [200]>":
			raise IOError("Can't access to Luogu.")
		req = req.content.decode('utf-8')
		f = "[<a data-pjax href="
		begin = 0
		while 1:
			begin = req.find(f, begin)
			begin = begin + 38
			end = req.find("\">", begin)
			if req[begin:end] == "<head>\n<meta charset=\"utf-8":
				break
			print(req[begin:end])
			self.done_problems.insert(-1, Problem(req[begin:end]))

