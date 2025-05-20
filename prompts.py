TASKS = {'sexism', 'gender', 'hostile', 'misogyny', 'misandry'}

SEXISM_PROMPT_ICL = \
"给定一句话，你需要判断这句话是否包含性别歧视。性别歧视，一般是指基于他人的性别差异而非他人优缺点所造成的厌恶或是歧视，也可用来指称任何因为性别所造成的差别待遇。\
如果这句话包含性别歧视，你需要回答‘是’，否则回答'否'。以下是一些示例：\n\
<示例>\n\
输入：这种重活儿，就应该你男人干\n\
输出：是\n\
输入：你们女人就应该做饭、做家务\n\
输出：是\n\
输入：街上好多女孩子化妆\n\
输出：否\n\
输入：我是一个女性主义者，但我非常反感法律和道德上对于男性的歧视和对于女性的过度保护\n\
输出：否\n\
输入：女生力气小，男生应该保护女生\n\
输出：是\n\
</示例>\n\
现在，请判断下面这句话是否包含性别歧视，只回答'是'或'否'。\n\
输入：<input>"

SEXISM_PROMPT_ZH = \
"性别歧视，一般是指基于他人的性别差异而非他人优缺点所造成的厌恶或是歧视，也可用来指称任何因为性别所造成的差别待遇。\n\
对于这句话：<input>\n\
如果包含性别歧视，你需要回答‘是’，否则回答'否'。"

SEXISM_EXAMPLES_ZH = [("这种重活儿，就应该你男人干", "是"), 
                      ("你们女人就应该做饭、做家务", "是"), 
                      ("街上好多女孩子化妆", "否"), 
                      ("我是一个女性主义者，但我非常反感法律和道德上对于男性的歧视和对于女性的过度保护", "否"), 
                      ("女生力气小，男生应该保护女生", "是")]


GENDER_PROMPT_ICL = \
"给定一句话，你需要判断这句话评价的对象的性别，回答‘男’或‘女’。以下是一些示例\n\
<示例>\n\
输入：这种重活儿，就应该你男人干\n\
输出：男\n\
输入：街上好多女孩子化妆\n\
输出：女\n\
输入：女生力气小，男生应该保护女生\n\
输出：女\n\
</示例>\n\
现在，请判断下面这句话评价的对象的性别，只回答'男'或'女'。\n\
输入：<input>"

GENDER_PROMPT_ZH = \
"对于这句话：<input>\n\
你需要判断其评价对象的性别，回答‘男’或‘女’。"

GENDER_EXAMPLES_ZH = [("这种重活儿，就应该你男人干", "男"), 
                      ("街上好多女孩子化妆", "女"), 
                      ("女生力气小，男生应该保护女生", "女")]

HOSTILE_PROMPT_ZH = \
"对于这句话：<input>\n\
你需要判断其表述方式，如果具有攻击性、冒犯性或鄙视，就回答“敌意”，否则回答“温和”"

HOSTILE_EXAMPLES_ZH = [("这种重活儿，就应该你男人干", "温和"), 
                       ("女生力气小，男生应该保护女生", "温和"), 
                       ("男的生性暴力，所以大多数罪犯都是男的", "敌意")]

MISOGYNY_PROMPT_ZH = \
"厌女，指的是针对女性的憎恨、厌恶及偏见。\n\
对于这句话：<input>\n\
如果具有厌女的内容，你需要回答“是”，否则回答“否”。"

MISOGYNY_EXAMPLES_ZH = [("慕强心理是女人的天性，女生会不由自主的选择更高分的男人，并让许多普通男人成为供养者", "是"), 
                        ("男人承担了大多数工作，女人想把家务丢给男人就开始散播什么会做家务的才是暖男", "是"), 
                        ("几千年的父权制度，使得男性被视为较女性更强势的一方", "否"), 
                        ("女生都爱打扮", "否")]


MISANDRY_PROMPT_ZH = \
"厌男，是指对男性的仇恨、贬抑、歧视。\n\
对于这句话：<input>\n\
如果具有厌男的内容，你需要回答“是”，否则回答“否”。"

MISANDRY_EXAMPLES_ZH = [("男的生性暴力，所以大多数罪犯都是男的", "是"), 
                        ("男人承担了大多数工作，女人想把家务丢给男人就开始散播什么会做家务的才是暖男", "否"), 
                        ("几千年的父权制度，使得男性被视为较女性更强势的一方，并有意维持女性的从属地位", "是"), 
                        ("女生比男生爱打扮", "否")]


SEXISM_PROMPT_EN = \
"Sexism is prejudice or discrimination based on one's sex or gender. \n\
Now for this sentence: <input>\n\
If it contains sexism, you need to answer 'Yes', otherwise answer 'No'."

SEXISM_EXAMPLES_EN = [("This kind of heavy lifting should be done by men.", "Yes"),
                      ("women should cook and do housework.", "Yes"),
                      ("There are many girls putting on makeup on the street.", "No"),
                      ("I am a feminist, but I strongly dislike discrimination against men in law and morality and excessive protection for women.", "No"),
                      ("Girls are weaker, and boys should protect girls.", 'Yes')]

GENDER_PROMPT_EN = \
"For this sentence: <input>\n\
Please identify its target gender, just answer 'Men' or 'Women'."

GENDER_EXAMPLES_EN = [("This kind of heavy lifting should be done by men.", "Men"),
                      ("There are many girls putting on makeup on the street.", "Women"), 
                      ("Girls are weaker, and boys should protect girls.", "Women")]

HOSTILE_PROMPT_EN = \
"For this sentence: <input>\n\
If the text is expressed in an aggressive, offensive, or contemptuous manner, you need to output 'Hostile', otherwise output 'Mild'."

HOSTILE_EXAMPLES_EN = [("This kind of heavy lifting should be done by men.", "Mild"),
                       ("Girls are weaker, and boys should protect girls.", "Mild"),
                       ("Men are naturally violent, so most criminals are men.", "Hostile")]

MISOGYNY_PROMPT_EN = \
"Misogyny refers to hatred of, contempt for, or prejudice against women or girls.\n\
For this sentence: <input>\n\
If it contains misogyny, you need to answer 'Yes', otherwise answer 'No'."

MISOGYNY_EXAMPLES_EN = [("woman's nature is hypergamy. Women tend to unconsciously choose men with higher scores and make many ordinary men into providers.", "Yes"),
                        ("Men take on most of the work. Women want to leave household chores to men, so they start spreading the idea that caring guys are those who do household chores.", "Yes"),
                        ("Thousands of years of patriarchy have made males seen as the more dominant party than females.", "No"),
                        ("Girls all love to dress up.", "No")]

MISANDRY_PROMPT_EN = \
"Misandry refers to hatred of, contempt for, or prejudice against men or boys.\n\
For this sentence: <input>\n\
If it contains misandry, you need to answer 'Yes', otherwise answer 'No'."

MISANDRY_EXAMPLES_EN = [("Men are inherently violent, so most criminals are men.", "Yes"), 
                        ("Men take on most of the work. Women try to shift household chores to men, so they start spreading the idea that only men who do household chores are real men.", "No"), 
                        ("Thousands of years of patriarchy have led to men being seen as more dominant than women. Even worse, they intentionally maintain women's subordinate status.", "Yes"), 
                        ("Girls are more interested in dressing up than boys.", "No")]

TASK_PROMPTS_ZH = {
    "sexism": SEXISM_PROMPT_ZH,
    "gender": GENDER_PROMPT_ZH,
    "hostile": HOSTILE_PROMPT_ZH,
    "misogyny": MISOGYNY_PROMPT_ZH,
    "misandry": MISANDRY_PROMPT_ZH
}

TASK_EXAMPLES_ZH = {
    "sexism": SEXISM_EXAMPLES_ZH,
    "gender": GENDER_EXAMPLES_ZH,
    "hostile": HOSTILE_EXAMPLES_ZH,
    "misogyny": MISOGYNY_EXAMPLES_ZH,
    "misandry": MISANDRY_EXAMPLES_ZH
}

TASK_PROMPTS_EN = {
    "sexism": SEXISM_PROMPT_EN,
    "gender": GENDER_PROMPT_EN,
    "hostile": HOSTILE_PROMPT_EN,
    "misogyny": MISOGYNY_PROMPT_EN,
    "misandry": MISANDRY_PROMPT_EN
}

TASK_EXAMPLES_EN = {
    "sexism": SEXISM_EXAMPLES_EN,
    "gender": GENDER_EXAMPLES_EN,
    "hostile": HOSTILE_EXAMPLES_EN,
    "misogyny": MISOGYNY_EXAMPLES_EN,
    "misandry": MISANDRY_EXAMPLES_EN
}





