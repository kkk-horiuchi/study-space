sakura = ["sakura", 28, "pink"]
chaewon = {"name": "chaewon", "old": 25, "color": "silver"}

# 変更
sakura[2] = "ピンク"
# 後ろに追加
sakura.append("sakukku")
# 1のところに差し込み
sakura.insert(1,"HKT")
# 一致した値の削除
sakura.remove(28)
# 0を削除
sakura.pop(0)

# 変更
chaewon["color"] = "銀"
# 追加
chaewon["character"] = "kimachi"
# 変更・追加（複数可）
chaewon.update({"color": "シルバー","pet": "siro"})
# 削除
del chaewon["old"]

print(chaewon)
