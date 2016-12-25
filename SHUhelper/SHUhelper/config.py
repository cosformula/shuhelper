'''
cofig there
'''
import os
from SHUhelper import app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.contrib.cache import MemcachedCache
from werkzeug.contrib.cache import SimpleCache
#CACHE = MemcachedCache(['127.0.0.1:11211'])
from flask import Flask
basedir = os.path.abspath(os.path.dirname(__file__))
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'course.db'),
                       DEBUG=False,
                       SECRET_KEY='shuhelper',
                       USERNAME='admin',
                       PASSWORD='default'))
app.secret_key = u'key'
class DevlopmentConfig(Config):
    DEBUG = True;
    CACHE = SimpleCache()

class ProductionConfig(Config):
    CACHE = MemcachedCache(['127.0.0.1:11211'])

class TesingConfig(Config):
    pass

config = {
    'development' : DevlopmentConfig,
    'tesing' : TesingConfig,
    'prooduction' : ProductionConfig,
    'default' : DevlopmentConfig
    }

DAILY_WORDS = [u"在正午的阳光之下,正洋溢着春天的甜美芬芳 (咦明明是冬天",
               u"再见并不意味着分别，那是还会相见的约定 ",
               u"凋零飘落的花瓣 缤纷化作细雪之时",
               u"这个世界就犹如是你和我的,仅属你我两人的东西",
               u"看那漫天繁星正为你闪耀不已",
               u"無限大な夢のあとの 何もない世の中じゃ",
               u"我也喜欢雨天哦 你的雨伞很温暖",
               u"在正午的阳光之下,正洋溢着春天的甜美芬芳 咦明明是冬天",
               u"只要有想见的人，就不再是孤单一人",
               u"你帮助了迷路的我， 如果能实现，我想带你。 去看绚丽的山岚，去看秀丽的溪谷。 这份心情，人类如何称呼的呢？",
               u"才见乔叶绿，又闻杜鹃鸣，夏至木鱼美，独钓此山中。",
               u"就好像是在图书馆里一个人自习的时候，不自觉地在桌子上，又或者是在笔记本的空白处写下「阿良良木翼」这样一个名字。",
               u"那指着天空的身影和天真无邪的声音",
               u"Hello How are you",
               u"悄悄的等待着 阳光照亮这个房间之时",
               u"我的愿望 只有一个那就是 全部 全部 全部 全部喜欢上你♡",
               u"你一定是用同样的笑容，对其它女孩子笑的吧",
               u"还会再次在同样的地方相遇的",
               u"几经相会 得知夙愿",
               u"世界 在你手中 耀放异彩",
               u"因为啊无论是黎明 或是黄昏 我都有千言万语想要传达给你呢",
               u"可以拥抱的话 就好像能够合在一起似的",
               u"仅仅依靠奇迹，一定会有缺陷的，所以我们才，紧紧握住彼此的手",
               u"DON'T PANIC",
               u"总而言之，不论发生了什么，只要还没死，人生就还没有结束－－人生仍会继续。也不会出现什么片尾曲或者STAFF字幕之类的东西",
               u"我们信守这些不言自明的真理：人人生而平等",
               u"人们不都是喜欢看着大家的笑容活下去吗？",
               u"在虚构的故事中寻找真实感的人一定脑袋有问题",
               u"猫经常揣手是因为他们知道这样很萌吗？",
               u"今天也肯定有某人，在世界的某个地方死去哦？所以穿丧服吧",
               u"诸葛亮知识广博，乃至在三国杀中需要三张将牌才能勉强概括他的技能。",
               u"英文咒语翻译成中文还有法术效果吗",
               u"莱特兄弟发明飞机以前，任何人如果想要飞到其他地方，都必须将 200 磅重的氦气吃下肚。",
               r"如果生活给了你土豆，就把他炸成土豆片 \(^o^)/ ",
               u"你今天真好看(*^_^*)",
               u"我们的成功是不应该通过企求别人的懈怠来达到的",
               u"本想给你做菜，可惜我没有锅。本想给你织围巾，可惜我没有线。本想给你写首诗，可惜我没有笔。",
               r"人生 ！ (/▽＼=)",
               u"自强不息",
               u"我们都是孤单的动物。我们把全部人生用来减轻孤独。",
               u"『这个世界上不存在才华，也不存在天赋，都是把事情一遍一遍重复做，下笨功夫，的来的成绩。』",
               u"『我岁数大了，就是想为国家多做贡献，其他无所挂念。』——钱伟长",
               u"每逢你想要批评任何人时，请记住，这个世界上所有的人，并不是个个都有过你所拥有的那些优越条件",
               u"以回赠她曾经送给我的那些可爱笑容",
               u"You will make a great discovery.",
               u"『这个世界上不存在才华，也不存在天赋，都是把事情一遍一遍重复做，下笨功夫，的来的成绩。』",
               u"前路未必顺利，但前路一定精彩",
               u"这颗星球上有无数微不足道的生命，但每一个生命都是可以歌唱的。",
               u"『这个世界上不存在才华，也不存在天赋，都是把事情一遍一遍重复做，下笨功夫，的来的成绩。』",
               u"年轻人是时常错过老人的",
               u"所有的爱都是为了相聚，只有父母与儿女的爱是为了别离",
               u"社会就是靠这种『异类』进步的呀",
               u"艺术，为了艺术的艺术，是这个世界上唯一重要的事情；艺术家凭一己之力赋予这荒谬的世界以意义。"]
