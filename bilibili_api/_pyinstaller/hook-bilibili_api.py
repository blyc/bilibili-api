from typing import List, Tuple

from PyInstaller.utils.hooks import collect_data_files, copy_metadata

datas: List[Tuple[str, str]] = collect_data_files("bilibili_api")
datas += copy_metadata("bilibili-api-python")
