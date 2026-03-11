List2020 =['15. “Work What Is Good Toward All”',
'22. Are You Benefiting From Jehovah’s Provisions?',
'32. Coping With Life’s Anxieties',
'35. Can You Live Forever? Will You?',
'37. Are God’s Ways Really Beneficial?',
'38. Act Wisely as the End Draws Near',
'53. Does Your Thinking Agree With God’s?',
'58. Who Are the Real Followers of Christ?',
'69. Renewing the Spirit of Self-Sacrifice',
'72. Love Identifies the True Christian Congregation',
'78. Serve Jehovah With a Joyful Heart',
'85. Good News in a Violent World',
'107. Hold a Good Conscience in a Sinful World',
'114. Appreciating Marvels of God’s Creation',
'142. Why Take Refuge in Jehovah',
'147. Trust in Jehovah’s Saving Power',
'148. Do You Share God’s View of Life?',
'150. Is This World Doomed to Ruin?',
'168. You Can Feel Safe in This Troubled World!',
'176. Real Peace and Security—When?',
'182. What God’s Kingdom Is Doing for Us Now',
'186. Unite With God’s Happy People',
'189. Walking With God Brings Blessings Now and Forever',
'190. A Promise of Perfect Family Happiness',
'191. How Love and Faith Conquer the World',
'192. Are You on the Road to Everlasting Life?',
'193. Rescue From World Distress']

List2021 = ['10. Be Honest in All You Say and Do',
'14. A Clean People Honors Jehovah',
'16. Keep Growing in Your Relationship With God',
'19. Your Future—How Can It Be Known?',
'26. Does God Count You Personally Important?',
'28. Show Respect and Love in Your Marriage',
'31. Happy Though Hungry—How Can It Be?',
'42. How the Kingdom of God Affects You',
'45. Follow the Way to Life',
'52. Who Is Your God?',
'56. Into the New World Under Christ’s Leadership',
'63. Do You Have the Evangelizing Spirit?',
'71. How to Keep Spiritually Awake',
'72. Love Identifies the True Christian Congregation',
'78. Serve Jehovah With a Joyful Heart',
'99. Why You Can Trust the Bible',
'114. Appreciating Marvels of God’s Creation',
'120. Why Submit to God’s Rulership Now',
'125. Why Mankind Needs a Ransom',
'126. Who Can Be Saved?',
'129. Is the Trinity a Scriptural Teaching?',
'130. The Earth Will Remain Forever',
'158. Be Courageous, and Trust in Jehovah',
'173. Is There a True Religion From God’s Standpoint?',
'178. Walk in the Way of Integrity',
'180. The Resurrection—Why That Hope Should Be Real to You',
'181. Is It Later Than You Think?',
'183. Turn Your Eyes Away From Worthless Things!',
'187. Why Would a Loving God Permit Wickedness?',
'193. Rescue From World Distress',
'194. How Godly Wisdom Benefits Us']

myset = set()
dup = []
for e in List2020:
	myset.add(e)
for e in List2021:
	if not e in myset:
		myset.add(e)
	else:
		dup.append(e)
# print(myset)


for e in dup:
	print(e)

