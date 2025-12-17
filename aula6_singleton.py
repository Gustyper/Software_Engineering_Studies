class SingletonRaiz:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print("[INFO] Creating Singleton instance")
            cls._instance = super().__new__(cls)
        else:
            print("[INFO] Returning existing Singleton instance")
            
        return cls._instance
    
    def __init__(self):
        self.data = "Data"
        
 ###############################################################################

print("#" * 60)

from abc import ABC, abstractmethod

class DatasetLoader(ABC):
    @abstractmethod
    def load(self) -> None: ...
    
class Model(ABC):
    @abstractmethod
    def train(self) -> None: ...
    
class Visualizer(ABC):
    @abstractmethod
    def plot(self) -> None: ...
    
    
class DataScienceFactory(ABC):
    @abstractmethod
    def create_dataset_loader(self) -> DatasetLoader: ...
    
    @abstractmethod
    def create_model(self) -> Model: ...
    
    @abstractmethod
    def create_visualizer(self) -> Visualizer: ...
    
    
###############################################################################
# Familia de produtos 1
class PandasDatasetLoader(DatasetLoader):
    def load(self) -> None:
        print("[PandasDatasetLoader] Lendo CSV Local com pandas.read_csv(...). Amostras: 10_000")
        
class SKLearnModel(Model):
    def train(self) -> None:
        print("[SKLearnModel] Treinando LogisticRegression(solver=\"lbfgs\"). Acurácia de validação: 0.67")

class MatplotlibVisualizer(Visualizer):
    def plot(self) -> None: 
        print("[MatplotlibVisualizer] Gerando pyplot e heatmap de correlação no MatplotLib")
        

###############################################################################
# Familia de produtos 2
class SparkDatasetLoader(DatasetLoader):
    def load(self) -> None:
        print("[SparkDatasetLoader] Lendo dados no cluster ")
        
class MLibLearnModel(Model):
    def train(self) -> None:
        print("[SKLearnModel] Treinando RandomForestClassifier(solver=\"lbfgs\"). Acurácia de validação: 0.67")

class SeabornVisualizer(Visualizer):
    def plot(self) -> None: 
        print("[MatplotlibVisualizer] Gerando pyplot e heatmap de correlação no Seaborn")
        
        
###############################################################################
# Fabrica Local
class LocalFactory(DataScienceFactory):
    def create_dataset_loader(self) -> DatasetLoader: 
        print("[LocalFactory: DatasetLoader]")
        return PandasDatasetLoader()
    
    def create_model(self) -> Model: 
        print("[LocalFactory: Model]")
        return SKLearnModel()
        
    def create_visualizer(self) -> Visualizer:
        print("[LocalFactory: Visualizer]")
        return MatplotlibVisualizer()
    
    
###############################################################################
# Fabrica Distribuida
class DistributedFactory(DataScienceFactory):      
    """
    Note que antes estávamos focados em criar UM produto. Agora estamos focados em usar uma FAMÍLIA de produtos compatíveis
    """
    def create_dataset_loader(self) -> DatasetLoader: 
        print("[LocalFactory: DatasetLoader]")
        return SparkDatasetLoader()
    
    def create_model(self) -> Model: 
        print("[LocalFactory: Model]")
        return MLlibmodel()
        
    def create_visualizer(self) -> Visualizer:
        print("[LocalFactory: Visualizer]")
        return SeabornVisualizer()
    
###############################################################################
# Interface
class Applicationinterface:
    def get_factory(self, stsack: str) -> DataScienceFactory:
        if stsack == "local":
            return LocalFactory()
        if stsack == "distributed":
            return DistributedFactory()
        raise ValueError("Deu Ruim")
        
        
###############################################################################

app = Applicationinterface()

factory = app.get_factory("local")
loader = factory.create_dataset_loader()
model = factory.create_model()
viz = factory.create_visualizer()

loader.load()
model.train()
viz.plot()






