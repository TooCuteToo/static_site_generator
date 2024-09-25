import shutil
from helper import Helper
import os


def main():
    clean_up_dir("public")
    copy_file_to_dest("static", "public")


def clean_up_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)
        return

    print(f"cleaning up the dir: {path}")
    shutil.rmtree(path)


def copy_file_to_dest(source_path, dest_path):
    if os.path.isfile(source_path):
        print(f"copying source file: {source_path} --- dest: {dest_path}")
        shutil.copy(source_path, dest_path)
        return

    list_dir = os.listdir(source_path)

    for dir in list_dir:
        s = os.path.join(source_path, dir)
        d = os.path.join(dest_path, dir)
        print(f"source path: {s} --- dest path: {d}")

        if os.path.isdir(s):
            if not os.path.exists(d):
                print(f"creating dest path: {d}")
                os.mkdir(d)

            copy_file_to_dest(s, d)

        else:
            copy_file_to_dest(s, d)


if __name__ == "__main__":
    main()
