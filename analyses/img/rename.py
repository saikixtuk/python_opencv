"""
os
    os依存モジュール
"""
import os


class Rename:
    """
    写真の名前を書き換える.
    """

    def __init__(self):
        self.curdir = os.path.dirname(__file__) + "/"
        self.list_file = "filelist.txt"
        self.ext_list = [".JPG", ".png", ".jpg", ".jpeg"]
        # ファイルリスト.txtの削除
        self.remove_list()
        # ファイルリスト.txtの作成
        self.create_list()

    def main(self):
        """
        実行関数.
        """
        print("実行開始.")
        self.rename()
        print("実行終了.")

    def remove_list(self):
        """
        テキストファイルを削除する.
        """
        if os.path.exists(self.curdir + self.list_file):
            os.remove(self.curdir + self.list_file)

    def create_list(self):
        """
        空テキストファイルの作成.
        """
        print(self.curdir)
        with open(self.curdir+self.list_file, 'w'):
            pass

    def rename(self):
        """
        ファイル名を書き換える.
        """

        name_count = 0
        file_list = os.listdir(self.curdir)
        # カレントディレクトリを取得
        parent_path = os.path.abspath(__file__).split("\\")
        write_txt = str(parent_path[-2])

        for i in file_list:
            ext = os.path.splitext(i)[1]
            if ext in self.ext_list:
                rename_file = "trial" + str(name_count)+".jpg"
                rename_path = self.curdir+rename_file
                os.rename(self.curdir+i, rename_path)
                print("[SUCCESS] from : {}, to : {}".format(
                    self.curdir+i, rename_path))
                self.write_text(rename_file, write_txt)
                name_count = name_count + 1
            if ext == "png":
                print(i + "はjpg形式に変換されました.")

    def write_text(self, txt, parent):
        """
        テキストファイルにリネーム後の名前を出力する.
        """
        file_list = self.curdir + self.list_file
        with open(file_list, mode='w') as f_val:
            f_val.write("./" + parent + "/" + txt + "\n")


if __name__ == "__main__":
    try:
        RENAME = Rename()
        RENAME.main()
    except Exception as e:
        print(e.args)
        print(Exception)
        os.system('PAUSE')
