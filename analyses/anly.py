# opencvをimport
"""
cv2
    画像解析モジュール
os
    os依存モジュール
copy
    コピーモジュール
datetime
    日時計算モジュール
"""
import os
import copy
import datetime
import cv2


class FaceAnalys:
    """
    顔情報解析クラス.
    """

    def __init__(self, img):
        curdir = os.path.dirname(__file__) + "/"
        self.face_path = curdir+'base_data/haarcascade_frontalface_default.xml'
        self.push_path = curdir+"img/push/"
        self.get_path = curdir+"img/"
        self.cut_path = curdir+"img/push/later/"
        self.img_name = img

    def main(self):
        """
        メインスクリプト関数
        """
        print("【{}】実行開始.".format(datetime.datetime.now()))
        self.face_cac()
        print("【{}】実行終了.".format(datetime.datetime.now()))

    def face_cac(self):
        """
        顔認証を行う
        """
        # 物体の特徴を記述したXML形式のカスケードファイルを読み込む
        face_cascade = cv2.CascadeClassifier(self.face_path)
        # モザイク用
        self.pixlation(face_cascade)

    def pixlation(self, face_cascade):
        """
        モザイク化処理.
        """
        # 画像ファイルを読み込み
        src = cv2.imread(self.get_path + self.img_name)
        # 画像の二値化
        src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(src_gray)
        self.check_region(faces, src)

    def check_region(self, faces, src):
        """
        顔情報の領域を取得する.
        faces : face
            顔の座標情報
        src : cv2
            読み込んだ画像の情報
        """
        face_list = os.listdir(self.cut_path)
        face_num = len(face_list)
        count = face_num + 1
        pixel = copy.copy(src)
        out_face = copy.copy(src)
        step = 0
        for x_val, y_val, w_val, h_val in faces:
            self.cut_pixlation(pixel, x_val, y_val, w_val, h_val)
            self.output_face(out_face, x_val, y_val, w_val, h_val, count)
            count = count + 1
            step = step + 1
        if step == 0:
            print("認識できる情報がありませんでした。")
        cv2.imwrite(self.push_path + self.img_name, pixel)

    def cut_pixlation(self, src, x_val, y_val, w_val, h_val):
        """
        取得した顔情報にモザイクをかける.
        """
        ratio = 0.05
        # モザイク処理
        small = cv2.resize(src[y_val: y_val + h_val, x_val: x_val + w_val], None, fx=ratio, fy=ratio,
                           interpolation=cv2.INTER_NEAREST)
        src[y_val: y_val + h_val, x_val: x_val + w_val] = cv2.resize(small, (w_val, h_val),
                                                                     interpolation=cv2.INTER_NEAREST)

    def output_face(self, src, x_val, y_val, w_val, h_val, count):
        """
        顔画像の切り出し.
        """
        # 顔の切り出し処理
        face_cut = src[y_val:y_val+h_val, x_val:x_val+w_val]
        img_path = self.cut_path + str(count) + '.jpg'
        cv2.imwrite(img_path, face_cut)
        print(img_path)


if __name__ == "__main__":
    ERR_FLG = False
    img_list = (os.listdir(os.path.join(os.path.dirname(__file__), "img")))
    try:
        i = 0
        while ERR_FLG is False:
            set_file = "trial{}.jpg".format(i)
            if set_file in img_list:
                FACE = FaceAnalys(set_file)
                i += 1
            else:
                break
            # メイン処理
            FACE.main()
    except Exception as e:
        ERR_FLG = True
        # 続行するには何かキーを押してください...
        os.system('PAUSE')
