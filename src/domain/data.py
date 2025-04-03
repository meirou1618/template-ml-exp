from dataclasses import dataclass

import pandas as pd


@dataclass
class TemplateData:
    X: pd.DataFrame
    y: pd.DataFrame
