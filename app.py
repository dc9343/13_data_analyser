from calculation import calculation_total, calculation_min, calculation_max, calculation_ave

if __name__ == '__main__':
    # ユーザからの入力を受け取る
    input_data = input("データを入力してください(スペース区切り) > ")

    # print(input_data)

    # 文字列のリストに変換する
    numbers_as_str = input_data.split(" ")
    # print(numbers_as_str)

    # 整数リストに変換する
    numbers = []  # からのリストを作る(空っぽの箱を作ってそこに入れていくイメージ)

    # input された情報を整数に
    for number_as_str in numbers_as_str:
        int_num = int(number_as_str)  # 整数に変換

        numbers.append(int_num)  # numbersというリストに要素を追加

    # print(numbers)

    # 各統計量を計算する(合計、最大、最小、平均)
    total = calculation_total(numbers)

    # print(total)

    # ユーザに見やすいようにフォーマットする

    # 出力する
    print(f"合計; {total}")

    # [✗] ユーザから整数のリストを受け取る
    # [ ] 最小値を計算する
    # [ ] 入力された数値を比較する
    # [ ] 小さい数字を残していく
    # [ ] 最小値の変数に代入する

    # [ ] 最小値を出力する
    # min = "最小値"

    max = calculation_max(numbers)

    print(f"最大値; {max}")

    min = calculation_min(numbers)

    print(f"最小値; {min}")

    ave = calculation_ave(numbers)

    print(f"平均値; {ave}")
