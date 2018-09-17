from keras.layers import Input, Dense
from keras.models import Model, load_model
from keras.datasets.mnist import load_data
import json

inputs = Input(shape=(3, ))
(data, labels), (test_data, test_lables) = load_data()

x = Dense(4, activation='relu')(inputs)
x = Dense(5, activation='relu')(x)
predictions = Dense(6, activation='softmax')(x)

model = Model(inputs=inputs, outputs=predictions)
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model_json = model.to_json()
print(model_json)

weithts_list = model.get_weights()
print(weithts_list)
for index in weithts_list:
    print(index)
#weithts_json = json.dumps(weithts_list)

model.save("keras_array.model")
#model.fit(data, labels)
del model

model = load_model('keras_array.model')
print(model.to_json())
