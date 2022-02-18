
class ImageCopy:

    DEFAULT_IMAGE_PATH = r"C:\Users\gksxo\Desktop\Folder\github\GDSC_GCP_django_test\django_TEST\static\testImage.png"

    @staticmethod
    def make_folder_cmd():
        """ 폴더 생성 cmd """
        for i in range(101, 113):
            print(i, end=" ; ")
        for i in range(201, 210):
            print(i, end=" ; ")
        # mkdir 101 ; 102 ; 103 ; 104 ; 105 ; 106 ; 107 ; 108 ; 109 ; 110 ; 111 ; 112 ; 201 ; 202 ; 203 ; 204 ; 205 ; 206 ; 207 ; 208 ; 209 ;

    @staticmethod
    def copy_cmd(folder_path):
        """ 복사 cmd 생성 """
        for i in range(101, 113):
            cmd = (
                "copy "
                "C:\\Users\\gksxo\\Desktop\\Folder\\github\\GDSC_GCP_django_test\\django_TEST\\static\\testImage.png "
                f"C:\\Users\\gksxo\\Desktop\\Folder\\github\\GDSC_GCP_django_test\\django_TEST\\static\\{folder_path}\\{i}\\testImage.png;"
            )
            print(cmd)

        for i in range(201, 210):
            cmd = (
                "copy "
                "C:\\Users\\gksxo\\Desktop\\Folder\\github\\GDSC_GCP_django_test\\django_TEST\\static\\testImage.png "
                f"C:\\Users\\gksxo\\Desktop\\Folder\\github\\GDSC_GCP_django_test\\django_TEST\\static\\{folder_path}\\{i}\\testImage.png;"
            )
            print(cmd)

if __name__ == '__main__':
    # ImageCopy.make_folder_cmd()
    # ImageCopy.copy_cmd("report")
    # ImageCopy.copy_cmd("report_solved")
    pass
