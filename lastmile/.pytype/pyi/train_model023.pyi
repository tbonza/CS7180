# (generated with --quick)

import datetime
import image_preprocessing
import logging
from typing import Any, Dict, Optional, Tuple, Type, TypeVar

Adam: module
ImageDataGenerator: Type[image_preprocessing.ImageDataGenerator]
ModelCheckpoint: module
datetime: Type[datetime.datetime]
logger: logging.Logger
logging: module
np: module
os: module
pickle: module
tf: module

AnyStr = TypeVar('AnyStr', str, bytes)

def callbacks(model_type) -> list: ...
def create_patch(X, ps = ...) -> Any: ...
def enable_cloud_log(level = ...) -> None: ...
def fit_model(train_dataflow, val_dataflow, mod, imgproc, lr, epochs) -> Tuple[Any, Any]: ...
def fit_model_ngpus(X_train, Y_train, model, imgtup, lr = ..., epochs = ...) -> None: ...
def main() -> None: ...
def main_ngpus() -> None: ...
def mean_absolute_error(y_true, y_pred) -> Any: ...
def model02() -> Dict[str, Any]: ...
def model_predict(uneven_batch, file_path, datagen, model) -> Tuple[Any, Any]: ...
def plot_imgpair(Y_pred, Y_true, name) -> None: ...
def plot_loss(fpath, history) -> None: ...
def review_model(test_dataflow, test_imgreview_dataflow, model, history, model_id, imgproc, datagen) -> None: ...
def run_simulation(mod: dict) -> None: ...
def run_sony_images(mod, model_name) -> None: ...
def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
