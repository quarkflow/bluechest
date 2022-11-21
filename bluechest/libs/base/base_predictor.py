from libs.breast_cancer.predict import predict as predict_breast_cancer

class BasePredictor:

    def __init__(self, scope: str):
        self.scope = scope


    def predict(self, image):
        if self.scope == "breast_cancer":
            predictions = predict_breast_cancer(image=image)
        
        return predictions