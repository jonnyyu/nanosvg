import os
import os.path as osp
import subprocess
from zipfile import ZipFile

SRC_FILES= [
    'src/nanosvg.h',
    'src/nanosvgrast.h',
    'example/stb_image_write.h',
    'src/nanosvg.props'
]

def main():
    os.makedirs('dist', exist_ok=True)
    zip_fname = osp.join('dist', pkg_name())
    with ZipFile(zip_fname, 'w') as zipObj:
        for file in SRC_FILES:
            zipObj.write(file, osp.join('NanoSVG', osp.basename(file)))
    print(f'zip file= {zip_fname}')
    return 0

def git_sha():
    return subprocess.check_output(
        ['git', 'describe', '--always']).decode().strip()

def pkg_name():
    return f'nanosvg_headers_{git_sha()}.zip'

if __name__ == '__main__':
    import sys
    sys.exit(main())