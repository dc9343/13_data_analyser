if __name__ == '__main__':
    # ユーザからの入力を受け取る
    input_data = input("データを入力してください(スペース区切り) > ")

    print(input_data)

    # 文字列のリストに変換する
    numbers_as_str = input_data.split(" ")
    print(numbers_as_str)

    # 整数リストに変換する
    numbers = []  # からのリストを作る(空っぽの箱を作ってそこに入れていくイメージ)

    for number_as_str in numbers_as_str:
        int_num = int(number_as_str)  # 整数に変換

        numbers.append(int_num)  # numbersというリストに要素を追加

    print(numbers)

    # 　input された情報を整数に

    # 各統計量を計算する(合計、平均、・・)

    # ユーザに見やすいようにフォーマットする

    # 出力する

    # 必要な関数はなにか
