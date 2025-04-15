from dataclasses import dataclass

import pandas as pd


@dataclass
class TemplateTrainData:
    X: pd.DataFrame
    y: pd.DataFrame
