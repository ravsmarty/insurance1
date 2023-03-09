from dataclasses import dataclass
from Insurance.entity import config_entity

class DataIngestionArtifact:
    feature_store_file_path:str
    train_file_path: str
    test_file_path:str
