from flask import Flask
from flask import request
from flask import render_template, redirect, url_for

class ML:
    def __init__(self):
        self.avaliable_models = {
            "face_detection": "/additional_drive/ML/face_detection",
            "car_detection": "/additional_drive/ML/car_detection",
            "shoe_detection": "/additional_drive/ML/shoe_detection",
            "cloth_detection": "/additional_drive/ML/cloth_detection",
            "signal_detection": "/additional_drive/ML/signal_detection",
            "water_level_detection": "/additional_drive/ML/water_level_detection",
            "missile_detection": "/additional_drive/ML/missile_detection"
        }
        self.loaded_models_limit = 2
        self.loaded_models = {
            model: self.load_weights(model)
            for model in list(self.avaliable_models)[:self.loaded_models_limit]
        }
        #Creating a dictionary to Store the number of requests handaled by each model
        self.model_requests = {}
        for model in self.loaded_models:
            self.model_requests[model] = 0
    
    def load_weights(self, model):
        return self.avaliable_models.get(model,None)

    def load_balancer(self, new_model):
        if len(self.loaded_models) < self.loaded_models_limit:
            self.loaded_models[new_model] = self.load_weights(new_model)
            self.model_requests[new_model] = 0
        else:
            least_frequent_used_model = min(self.model_requests, key=self.model_requests.get)
            for model in self.model_requests:
                if self.model_requests[model] == least_frequent_used_model:
                    self.loaded_models.pop(model)
                    self.loaded_models[new_model] = self.load_weights(new_model)
                    self.model_requests[new_model] = 0
                    break
        print(self.loaded_models)
        



app = Flask(__name__)
ml = ML()

@app.route('/get_loaded_models', methods=['GET', 'POST'])
def get_loaded_models():

    return ml.loaded_models
    

@app.route('/process_request', methods=['GET', 'POST'])
def process_request():
    
    model = request.form["model"]
    if model not in ml.loaded_models:
        ml.load_balancer(model)
    ml.model_requests[model] += 1

    return redirect(url_for('index'))


app.run(host='0.0.0.0', port=5000)