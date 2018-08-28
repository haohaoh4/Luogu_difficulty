import requests
import logging
from src.Luogu_problem import Problem
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


class User:
	uid = 0
	name = ""
	done_problems = []
	done_difficulty = [0 in range(0, 8)]
	rating = 0

	def __init__(self, uid):
		req = requests.get("http://www.luogu.org/space/ajax_getuid?username=%s" % uid, headers=header)
		if str(req) != "<Response [200]>":
			logger.error("Can't access to Luogu %s." % ("https://www.luogu.org/space/ajax_getuid?username=%s" % uid))
			raise IOError("Can't access to Luogu.")
		req = str(req.content.decode("utf-8"))
		if req.find("404") != -1:
			logger.error("User %s not found" % uid)
			raise ConnectionError("Can't find user %s." % uid)

		user_id_begin = req.find("uid\"")
		if req.find("\"", user_id_begin + 4) == -1:
			user_id_begin = user_id_begin + 5
			user_id_end = req.find("\"}}")-1
		else:
			user_id_begin = user_id_begin + 6
			user_id_end = req.find("}}")-1

		user_id = req[user_id_begin:user_id_end]
		logger.debug("user_id:%s" % user_id)
		logger.debug(user_id_begin)

		self.uid = user_id
		self.get_base_info()

	def __str__(self):
		return self.name

	def get_base_info(self):
		url = "http://www.luogu.org/space/show?uid=%s" % self.uid
		req = requests.get(url, headers=header)
		if str(req) != "<Response [200]>":
			logger.error("Can't access to Luogu.requests info %s.URL is %s" % (req, url))
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
			logger.debug(req[begin:end])
			self.done_problems.append(Problem(req[begin:end]))
