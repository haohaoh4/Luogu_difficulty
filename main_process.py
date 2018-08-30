import sys
import msvcrt
import src.Luogu_diff as diff
import time
import logging
logger = logging.getLogger(__name__)


def main():
	logger.info("Start running")
	sys.stdout.flush()
	user_input = input("Please input your account's name or id.\n")
	begin_time = time.time()
	logger.info("Start time %s " % begin_time)
	if user_input == "debug_mode":
		logging.basicConfig(level=logging.NOTSET)
		user_input = input("Please input your account's name or id.\n")
	print("\nCollecting your info will cost about half a minute,\nPlease wait...\n")
	try:
		someone = diff.User(user_input)
	except ConnectionError:
		print("Can't find user %s." % user_input)
		return
	times = [0, 0, 0, 0, 0, 0, 0, 0]
	for p in someone.done_problems:
		if p.difficulty < 8:
			times[p.difficulty] = times[p.difficulty] + 1
		else:
			times[7] = times[7] + 1

	i = 0
	for n in times:
		print("%s:%s" % (diff.diff_name[i], n))
		i = i + 1
	logger.info("End time %s " % time.time())
	logger.info("Spend time %s " % (time.time() - begin_time))
	logger.info("Average time %s " % ((time.time() - begin_time) / someone.done_nums))


def main_end():
	print("\nPress any ket to exit...")
	msvcrt.getch()

# Average time of each problem:
# 0.5133928571428571
# 0.304135101010101
# 0.3140226218097448
# 0.31938976377952755
