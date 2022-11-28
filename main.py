from QuizFunction import Quiz

words = {
    "どんな困難にも負けないで立ち向かうこと。" : "不撓不屈",
    "力の限りを尽くして努力すること｡" : "粉骨砕身",
    "そばの人に遠慮せず、 勝手に振る舞うこと。" : "傍若無人",
    "体中が傷だらけの状態。 各方面から非難中傷を受け、精神的に痛めつけられているさま。" : "満身創痍",
    "何のわだかまりもなく、 澄みきって静かな心の状態。 「一の心境」" : "明鏡止水",
    "目標に向かって、勇ましく全身すること。" : "勇往邁進",
    "私心を捨て、 国や社会のために尽くすこと。" : "滅私奉公",
    "何事にも用意がすみずみまで行き届き、手抜かりのないこと。" : "用意周到",
    "こつこつと苦労や努力を積み重ねること。" : "粒粒辛苦",
    "日本固有の精神と西洋の学問。 また、その両者を兼ね備えていること｡" : "和魂洋才",
    "恋仲になった初め。 また、 そのきっかけとなったできごと。" : "馴れ初め",
    "普通の人なら両立出来ないような二つの職業を、一人の人が持つこと。" : "二足の草鞋を履く",
    "骨を折らないで利益を得ること｡ 少ない労力で得るもの多いこと｡" : "濡れ手で粟",
    "とりつくろっていた正体が現れる。" : "馬脚を現す",
    "値打ちが高くなる。 貫禄がつく。 「経歴に一」" : "箔が付く",
    "非常に危険で、冷や冷やするような思い｡" : "薄氷を踏む",
    "抑えきれないほど、盛んな勢いがあること。" : "破竹の勢い",
    "その世界で実力があり、 発言力が大であること。" : "幅を利かす",
    "生活の心配がなく、 安楽して暮らすこと。" : "左団扇",
    "用件を聞くか聞かないかのうちに拒絶すること。" : "門前払い",
    "うそをつくこと｡" : "二枚舌",
    "人を冷たい目で見たり、冷遇したりすること。" : "白眼視",
    "今まで誰もやらなかったことを成し遂げること｡" : "破天荒",
    "恥を恥とも思わないこと。" : "破廉恥",
    "景色や季節をうたった歌。 季節の感じを表しているもの｡" : "風物詩",
    "風のようにどこからともなくやって来た人。 気まぐれな人。" : "風来坊",
    "無愛想な顔。 ふくれ面。" : "仏頂面",
    "信念を持ち、 何事にも屈しないこと。 かたく信じて変えないこと。" : "不退転",
    "今までに一度も起こったことがないこと。" : "未曾有",
    "気を使って必要以上に世話を焼こうとする気持ち。" : "老婆心",
    "商品の市場全体に占める割合。 一つのものを分かち合い共有すること。" : "シェア",
    "冷笑する様子。皮肉。" : "シニカル",
    "位置や配置がそれまでと変わること｡" : "シフト",
    "両刀論法。 板ばさみ。" : "ジレンマ",
    "釣り合いの取れていること。 均整。" : "シンメトリー",
    "ものごとに対するときの立場や、 取り組む姿勢。" : "スタンス",
    "禁欲的。 感情に動かされず、 苦楽を超越する様子 (した人)。" : "ストイック",
    "理論。学説。" : "セオリー",
    "対象によって異なった価値判断の基準を使い分けること｡" : "ダブルスタンダード",
    "ある方向へ変化していく、全体的な傾向。" : "トレンド",
    "『城の崎にて』『清兵衛と瓢箪』「夜行路』" : "志賀直哉",
    "『お目出たき人』『友情』" : "武者小路実篤",
    "『或る女』『惜みなく愛は奪ふ』" : "有島武郎",
    "『羅生門』『鼻』『戯作三昧』『地獄変』『藪の中』『河童』" : "芥川龍之介",
    "『伊豆の踊子』『雪国』『山の音』" : "川端康成",
    "『日輪』『機械』" : "横光利一",
    "『父帰る』『恩讐の彼方に』" : "菊池寛",
    "『山椒魚』『ジョン万次郎漂流記』『黒い雨』" : "井伏鱒二",
    "『富嶽百景』『走れメロス』『津軽』『斜陽』『人間失格』" : "太宰治",
    "『春と修羅』『銀河鉄道の夜』『注文の多い料理店』『風の又三郎』" : "宮沢賢治",
    "『道程』『智恵子抄』" : "高村光太郎",
    "『月に吠える』『青猫』" : "萩原朔太郎",
    "『山羊の歌』『在りし日の歌』" : "中原中也",
    "『測量船』『駱駝の瘤にまたがって』" : "三好達治",
    "『邪宗門』『思ひ出』『桐の花』" : "北原白秋",
    "『二十億光年の孤独』" : "谷川俊太郎",
    "『みだれ髪』" : "与謝野晶子",
    "『あこがれ』『一握の砂』『悲しき玩具』" : "石川啄木",
    "『赤光』『柿本人麿』『白き山』" : "斎藤茂吉",
    "『サラダ記念日』" : "俵万智"
}

questions = words

quiz = Quiz(questions)
result = quiz.quiz_handler()
print(result)








