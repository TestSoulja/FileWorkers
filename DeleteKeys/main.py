import json
import os

s = os.path.abspath(__file__)
c = s.replace(os.path.basename(os.path.abspath(__file__)), "")

with open(c + "test.json", encoding="utf8") as file:
	dict_ = json.load(file)
for i in dict_:
	dict_[i].pop("HOLIDAY_EVENT_PLAY_AND_GET_REWARD_DURAK")
	dict_[i].pop("HOLIDAY_EVENT_ABOUT_TOOLTIP_TEXT_DURAK")
	dict_[i].pop("HOLIDAY_EVENT_PLAY_AND_GET_REWARD_VIDEOPOKER")
	dict_[i].pop("HOLIDAY_EVENT_ABOUT_TOOLTIP_TEXT_VIDEOPOKER")

with open(c + "test.json", "w", encoding="utf8") as file:
    json.dump(dict_, file, ensure_ascii=False)

print("OK")


