# generated by datamodel-codegen:
#   filename:  sample_data.json
#   timestamp: 2021-08-09T01:10:01+00:00
from typing import List

from pydantic import BaseModel


class ModelInput(BaseModel):
    x: List[int]
