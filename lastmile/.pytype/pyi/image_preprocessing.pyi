# (generated with --quick)

import logging
from typing import Any, Callable, Dict, Generator, Iterable, Iterator, List, NoReturn, Optional, Tuple, TypeVar

as_strided: Any
kimg: module
logger: logging.Logger
logging: module
np: module
os: module
pickle: module

AnyStr = TypeVar('AnyStr', str, bytes)
_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')
_T3 = TypeVar('_T3')
_T4 = TypeVar('_T4')
_T5 = TypeVar('_T5')
_T6 = TypeVar('_T6')

class ImageDataGenerator(object):
    batch_size: Any
    covm: Any
    meanm: Any
    num_images: Any
    patch_size: Any
    prepfuncs: Dict[str, Optional[Callable]]
    preprocessing_function: Any
    random_seed: Any
    stride: Any
    def __init__(self, preprocessing_function = ..., stride = ..., batch_size = ..., patch_size = ..., random_seed = ..., meanm_fpath = ..., covm_fpath = ..., image_dims = ..., num_images = ...) -> None: ...
    def _dirflow_train_val_raise(self, dirpath) -> Generator[Any, Any, None]: ...
    def _train_val_sony(self, sony_list: str) -> Generator[Any, Any, None]: ...
    def bl(self, image, sample = ...) -> Any: ...
    def bl_cd(self, image, sample = ...) -> Any: ...
    def bl_cd_pn(self, image, sample = ...) -> Any: ...
    def bl_cd_pn_ag(self, image, sample = ...) -> Any: ...
    def crop(self, image) -> Any: ...
    def crop_images(self, data) -> Any: ...
    def dirflow_test_raise(self, dirpath) -> Generator[Tuple[Any, Any], Any, None]: ...
    def dirflow_test_sony(self, sony_test_list) -> Generator[Any, Any, None]: ...
    def dirflow_train_raise(self, dirpath) -> Generator[Any, Any, None]: ...
    def dirflow_train_sony(self, sony_train_list: str) -> Generator[Any, Any, None]: ...
    def dirflow_val_raise(self, dirpath) -> Generator[Any, Any, None]: ...
    def dirflow_val_sony(self, sony_val_list: str) -> Generator[Any, Any, None]: ...
    def extract_patches(self, data) -> Any: ...
    def image_to_arr(self, img_path) -> Any: ...
    def parse_sony_list(self, sony_list: str) -> List[Tuple[Any, Any]]: ...
    def read_pickle(self, fpath) -> Any: ...
    def reconstruct_patches(self, patches, image_size) -> Any: ...
    def reformat_imgpath(self, img_path: str) -> str: ...
    def valid_sample(self) -> NoReturn: ...


@overload
def product(iter1: Iterable, iter2: Iterable, iter3: Iterable, iter4: Iterable, iter5: Iterable, iter6: Iterable, iter7: Iterable, *iterables: Iterable) -> Iterator[tuple]: ...
@overload
def product(iter1: Iterable[_T1]) -> Iterator[Tuple[_T1]]: ...
@overload
def product(iter1: Iterable[_T1], iter2: Iterable[_T2]) -> Iterator[Tuple[_T1, _T2]]: ...
@overload
def product(iter1: Iterable[_T1], iter2: Iterable[_T2], iter3: Iterable[_T3]) -> Iterator[Tuple[_T1, _T2, _T3]]: ...
@overload
def product(iter1: Iterable[_T1], iter2: Iterable[_T2], iter3: Iterable[_T3], iter4: Iterable[_T4]) -> Iterator[Tuple[_T1, _T2, _T3, _T4]]: ...
@overload
def product(iter1: Iterable[_T1], iter2: Iterable[_T2], iter3: Iterable[_T3], iter4: Iterable[_T4], iter5: Iterable[_T5]) -> Iterator[Tuple[_T1, _T2, _T3, _T4, _T5]]: ...
@overload
def product(iter1: Iterable[_T1], iter2: Iterable[_T2], iter3: Iterable[_T3], iter4: Iterable[_T4], iter5: Iterable[_T5], iter6: Iterable[_T6]) -> Iterator[Tuple[_T1, _T2, _T3, _T4, _T5, _T6]]: ...
@overload
def product(*iterables: Iterable, repeat: int = ...) -> Iterator[tuple]: ...
def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
