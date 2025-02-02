from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class ActivityShikigamiAssets: 


	# Image Rule Assets
	# description 
	I_BATTLE_CLASS_1 = RuleImage(roi_front=(126,132,124,81), roi_back=(126,132,124,81), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/0110/0110_battle_class_1.png")
	# description 
	I_BATTLE_CLASS_2 = RuleImage(roi_front=(120,231,129,83), roi_back=(120,231,129,83), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/0110/0110_battle_class_2.png")
	# description 
	I_BATTLE_CLASS_3 = RuleImage(roi_front=(141,331,100,89), roi_back=(141,331,100,89), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/0110/0110_battle_class_3.png")
	# description 
	I_BATTLE_CLASS_4 = RuleImage(roi_front=(141,435,100,83), roi_back=(141,435,100,83), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/0110/0110_battle_class_4.png")
	# description 
	I_BATTLE_CHECK_1 = RuleImage(roi_front=(36,643,39,41), roi_back=(36,643,39,41), threshold=0.7, method="Template matching", file="./tasks/ActivityShikigami/0110/0110_battle_check_1.png")
	# description 
	I_BATTLE_CHECK_2 = RuleImage(roi_front=(31,649,39,45), roi_back=(31,649,39,45), threshold=0.7, method="Template matching", file="./tasks/ActivityShikigami/0110/0110_battle_check_2.png")
	# description 
	I_BATTLE_CHECK_3 = RuleImage(roi_front=(34,652,38,42), roi_back=(34,652,38,42), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/0110/0110_battle_check_3.png")
	# description 
	I_BATTLE_CHECK_4 = RuleImage(roi_front=(33,652,38,40), roi_back=(33,652,38,40), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/0110/0110_battle_check_4.png")


	# Click Rule Assets
	# description 
	C_RANDOM_LEFT = RuleClick(roi_front=(21,23,290,599), roi_back=(21,23,290,599), name="random_left")
	# description 
	C_RANDOM_RIGHT = RuleClick(roi_front=(969,55,296,638), roi_back=(969,55,296,638), name="random_right")
	# description 
	C_RANDOM_TOP = RuleClick(roi_front=(85,46,1159,101), roi_back=(85,46,1159,101), name="random_top")
	# description 
	C_RANDOM_BOTTOM = RuleClick(roi_front=(182,539,1063,100), roi_back=(182,539,1063,100), name="random_bottom")
	# description 
	C_RANDOM_ALL = RuleClick(roi_front=(42,94,1207,543), roi_back=(42,94,1207,543), name="random_all")


	# Image Rule Assets
	# 进入活动 
	I_SHI = RuleImage(roi_front=(382,308,49,39), roi_back=(64,280,1029,142), threshold=0.7, method="Template matching", file="./tasks/ActivityShikigami/as/as_shi.png")
	# 左上角返回 
	I_BACK_GREEN = RuleImage(roi_front=(23,27,44,44), roi_back=(23,27,44,44), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/as/as_back_green.png")
	# 进入爬塔 
	I_BATTLE = RuleImage(roi_front=(558,236,47,172), roi_back=(526,208,105,220), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/as/as_battle.png")
	# 归鹿之途 
	I_DRUM = RuleImage(roi_front=(1011,114,29,31), roi_back=(1011,114,29,31), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/as/as_drum.png")
	# 上锁图标 
	I_LOCK = RuleImage(roi_front=(795,654,25,32), roi_back=(795,654,25,32), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/as/as_lock.png")
	# 还未上锁图片 
	I_UNLOCK = RuleImage(roi_front=(801,652,28,28), roi_back=(801,652,28,28), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/as/as_unlock.png")
	# 点击战斗 
	I_FIRE = RuleImage(roi_front=(1143,575,70,79), roi_back=(1143,575,70,79), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/as/as_fire.png")
	# 体力按钮 
	I_AP = RuleImage(roi_front=(1127,493,32,26), roi_back=(1127,493,32,26), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/as/as_ap.png")
	# 活动体力 
	I_AP_ACTIVITY = RuleImage(roi_front=(1129,499,27,25), roi_back=(1129,499,27,25), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/as/as_ap_activity.png")
	# 切换按键 
	I_SWITCH = RuleImage(roi_front=(1220,499,23,23), roi_back=(1220,499,23,23), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/as/as_switch.png")
	# 购买活动的体力 
	I_BUY_JADE = RuleImage(roi_front=(1004,192,38,42), roi_back=(836,619,38,42), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/as/as_buy_jade.png")
	# 增加到最大 
	I_ADD_MAX = RuleImage(roi_front=(17,24,33,37), roi_back=(974,524,57,54), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/as/as_add_max.png")
	# description 
	I_NEW = RuleImage(roi_front=(1004,192,65,52), roi_back=(0,0,100,100), threshold=0.8, method="Template matching", file="./tasks/ActivityShikigami/as/as_new.png")


	# Ocr Rule Assets
	# 体力的数量检测 
	O_REMAIN_AP = RuleOcr(roi=(1154,679,104,25), area=(1154,679,104,25), mode="DigitCounter", method="Default", keyword="", name="remain_ap")
	# 活动体力的剩余检测 
	O_REMAIN_AP_ACTIVITY = RuleOcr(roi=(912,25,95,30), area=(912,25,95,30), mode="DigitCounter", method="Default", keyword="", name="remain_ap_activity")
	# 还有多少次购买体力的机会 
	O_REMAIN_BUY = RuleOcr(roi=(808,531,39,42), area=(808,531,39,42), mode="DigitCounter", method="Default", keyword="", name="remain_buy")


