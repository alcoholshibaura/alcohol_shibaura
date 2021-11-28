# 感染症予防と衛生的手洗いの推進のためのハンドドライヤ併用式自動アルコール消毒器の開発

## 概要
　私たちはコロナウィルス感染症対策にハンドドライヤを有効活用できないかと考えた。
ハンドドライヤにアルコール噴射機器を取り付け、手の乾燥と手指消毒を同時に行うこと
で、誰もが感染症予防を望むことができる衛生的手洗いという消毒方法を効率よく実践で
きる機器を作ることにした。

## 開発環境
 - OS: Windows 10
 - RTミドルウェア: OpenRTM-aist-1.2.2-RELESE(python 版)
 - 開発環境： Visual Studio Code 2019
 - Python: Python 3.7.3

## ハードウェア
| 部品名　　　　　　　           　| 型番      | 数量 |
|:-------------------------------|:--------:|:----:|
| RGB LED タッチパネル            |          | 1 個 |
| TRASKIT Raspberry Pi 4 Model B |          | 1 個 |
| 超音波センサ                    | HC-SR04  | 1 個 |
| サーボモーター                  | MG92B    | 2 個 |
| 焦電センサ　　　　　　　　　　　  | HC-SR501 | 1 個 |
| シナベニア合板 450mm×300mm×7mm  |          | ５枚 |
| 角材 38mm×18mm×3000mm          |          | 2 本 |
| ステンレスクギ平 13mm           |          | 46本 |
| L 字補強金具                    |           | ６個 |
| ステンレスビス                  |           | 12本 |

## ソフトウェア
 - [center]
 (https://github.com/alcoholshibaura/alcohol_shibaura/tree/master/center)　
 : 出力された情報に応じて各出力ポートから情報を出力する。
 
 - [ultrasound]
 (https://github.com/alcoholshibaura/alcohol_shibaura/tree/master/ultrasound) 
 : 人が機器に手を差し出したことを検出する
 
 - [infrared]
 (https://github.com/alcoholshibaura/alcohol_shibaura/tree/master/infrared) 
 : 設置空間に人が侵入したことを検出する
 
 - [display]
 (https://github.com/alcoholshibaura/alcohol_shibaura/tree/master/display) 
 : ディスプレイに画像を出力したり、音声データを再生したりする
 
 - [servo]
 (https://github.com/alcoholshibaura/alcohol_shibaura/tree/master/servo) 
 : 入力データポートの値に応じてサーボモータを動かす。

## マニュアル
　本コンポーネントの使用方法などはこちらから
 (https://github.com/alcoholshibaura/alcohol_shibaura/blob/master/%E8%AA%AC%E6%98%8E%E6%9B%B8.pdf)

## お問い合わせ
email address : 17072@shibaura.com
