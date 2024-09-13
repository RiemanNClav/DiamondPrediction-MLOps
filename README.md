END-TO-END MLOPs Project


Broken DAG: [/opt/airflow/dags/dags.py]
Traceback (most recent call last):
  File "/opt/airflow/dags/src/DimondPricePrediction/pipelines/training_pipeline.py", line 1, in <module>
    from src.DimondPricePrediction.components.data_ingestion import DataIngestion
  File "/opt/airflow/dags/src/DimondPricePrediction/components/data_ingestion.py", line 9, in <module>
    from sklearn.model_selection import train_test_split
ModuleNotFoundError: No module named 'sklearn'



Broken DAG: [/opt/airflow/dags/dags.py]
Traceback (most recent call last):
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "/opt/airflow/dags/dags.py", line 7, in <module>
    from src.DimondPricePrediction.pipelines.training_pipeline import TrainingPipeline
ModuleNotFoundError: No module named 'src'