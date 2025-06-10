import shutil
import filecmp
from pathlib import Path

def get_good_filename(fname, target_folder):
    """
    fname is a file name like 9595.png;
    target_folder is the folder where the file should be saved, like restricted/assets/pictures1.
    While the file name exists in target_folder, add an '_' character right before the suffix part of the filename and return it
    for example, 9595_.png.
    """
    target_folder = Path(target_folder)
    suffix = fname.suffix   # Get the file extension
    good_filename = fname.name  # Start with the original filename

    # Check if the file already exists in the target folder
    while (target_folder / good_filename).exists():
        # If it exists, modify the filename by adding an underscore before the suffix
        good_filename = f"{fname.stem}_{suffix}"
        fname = Path(good_filename)  # Update fname to the new good filename
    return good_filename


def make_copy(fname, source_folder, target_folder):
    """
    fname is a file name like 9595.png, which is the file to copy;
    source_folder is the folder where the file is located, like restricted/assets/pictures1;
    target_folder is the folder where the file should be copied, like restricted/assets/pictures2.
    before copying, call get_good_filename to get a good file name to make sure the file name is unique in the target folder.
    """

    # Get the good filename
    good_filename = get_good_filename(fname, target_folder)

    # Construct full source and target paths
    source_path = source_folder / fname
    target_path = target_folder / good_filename

    # Copy the file
    shutil.copy2(source_path, target_path)
    print(f"Copied {source_path} to {target_path}")
    return Path(target_path / good_filename)

def compare_all_images_between_folders(folder1, folder2):
    """
    Compare every image in folder1 with every image in folder2, regardless of filename.
    """
    folder1 = Path(folder1)
    folder2 = Path(folder2)
    images1 = list(folder1.glob('*.png'))
    images2 = list(folder2.glob('*.png'))

    for img1 in images1:
        for img2 in images2:
            identical = filecmp.cmp(img1, img2, shallow=False)
            if identical:
                print(f"{img1.parent.name}/{img1.name} and {img2.parent.name}/{img2.name} are duplicated.")
            #print(f"{img1.name} vs {img2.name}: {'Identical' if identical else #'Different'}")


if __name__ == "__main__":
    # # Test case: copy restricted/pictures1/1262.png to restricted/pictures3/1262.png
    # src = Path.cwd() / 'restricted' / 'assets' / 'pictures1' / '1262.png'
    # dst = Path.cwd() / 'restricted' / 'assets' / 'pictures2' / 'abcd.png'
    # copy_file(src, dst)
    
    # # Example usage:
    # folder1 = Path.cwd() / 'restricted' / 'assets' / 'pictures1'
    # folder2 = Path.cwd() / 'restricted' / 'assets' / 'pictures2'
    # compare_all_images_between_folders(folder1, folder2)

    # # Example usage of get_good_filename
    # file_path = Path.cwd() / 'restricted' / 'assets' / 'pictures3'
    # # fname = Path('0000.png')
    # # fname = Path('1262.png')
    # fname = Path('9595.png')
    # good_filename = get_good_filename(fname, file_path)
    # print(f"Good filename: {good_filename}")
    # Example usage of make_copy
    source_folder = Path.cwd() / 'restricted' / 'assets' / 'pictures1'
    target_folder = Path.cwd() / 'restricted' / 'assets' / 'pictures3'
    fname = Path('1262.png')
    copied_file = make_copy(fname, source_folder, target_folder)
    print(f"Copied file: {copied_file}")