import requests
from src.Luogu_problem import Problem
from src.Luogu_user import user

diff_debug = False
diff_name = {0: "入门难度", 1: "普及-", 2: "普及/提高-", 3: "普及+/提高", 4: "提高+/省选-",5: "省选/NOI-", 6: "NOI/NOI+/CTSC", 7: "ERROR"}


def Debug_mode():
	global diff_debug
	diff_debug = True
	import src.Luogu_problem as luogu_p
	import src.Luogu_user as luogu_u
	luogu_p.diff_debug = True
	luogu_u.diff_debug = True
