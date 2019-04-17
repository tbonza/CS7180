# (generated with --quick)

import datetime
import image_preprocessing
import logging
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar

Adam: module
ImageDataPipeline: Type[image_preprocessing.ImageDataPipeline]
Input: Any
Lambda: module
Model: module
ModelCheckpoint: module
SonyDataGenerator: Type[image_preprocessing.SonyDataGenerator]
datetime: Type[datetime.datetime]
frozen_mod: Dict[str, Any]
json: module
logger: logging.Logger
logging: module
mod: Dict[str, Any]
os: module
tf: module

AnyStr = TypeVar('AnyStr', str, bytes)

class LeakyReLU(Any):
    def __init__(self, **kwargs) -> None: ...


def callbacks(model_type) -> list: ...
def create_patch(X, ps = ...) -> Any: ...
def custom_evaluate_sony(test_dataflow, test_dataflow2, model, model_name, idp) -> Tuple[List[Tuple[Any, Any]], List[Tuple[Any, Any]]]: ...
def enable_cloud_log(level = ...) -> None: ...
def eval_frozensony(mod: dict) -> None: ...
def freeze_sony_model(model) -> Dict[str, Any]: ...
def functional_sony() -> Dict[str, Any]: ...
def mean_absolute_error(y_true, y_pred) -> Any: ...
def restore_model(mod: dict, model_name) -> Any: ...
def run_frozensony(mod: dict) -> None: ...
def train_frozen_model(train_dataflow, val_dataflow, epochs: int, mod: dict, model_type: str, lr: float) -> Tuple[Any, Any]: ...
def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
