import pandas as pd

# 冠詞辞書
articles={
    "m":["le","un"],
    "f":["la","une"],
    "mp":["les","des"],
    "fp":["les","des"]
}

# 単語の性辞書
mots={
    "ombre":"f",
    "nuit":"f",
    "voyage":"m",
    "maisons":"fp",
    "ami":"m",
    "poésie":"f"
}

# 母音
voyelles=["a","e","i","o","u","h"]

# Excelを読む
df=pd.read_excel("/content/mots.xlsx")



articles_def=[]
articles_indef=[]

# Excelの「単語」列を順番に読む
for mot in df["単語"]:

    # 辞書にあるか確認
    if mot in mots:

        genre=mots[mot]

        # 定冠詞
        article_def=articles[genre][0]

        # 不定冠詞
        article_indef=articles[genre][1]

        # 母音なら le/la → l'
        if mot[0] in voyelles:

            if article_def=="la":
                article_def="l'"

            elif article_def=="le":
                article_def="l'"

        # 定冠詞の表示
        if article_def=="l'":

            articles_def.append(
                article_def+mot
            )

        else:

            articles_def.append(
                article_def+" "+mot
            )

        # 不定冠詞
        articles_indef.append(
            article_indef+" "+mot
        )

    else:

        articles_def.append(
            "未登録"
        )

        articles_indef.append(
            "未登録"
        )

# Excel列追加
df["定冠詞"]=articles_def
df["不定冠詞"]=articles_indef

# 保存
df.to_excel(
    "resultat.xlsx",
    index=False
)

print("完成")