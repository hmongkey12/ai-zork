# AI-ZORK
Python app utilizing flask and Jinja to display text

## Usage
> The **Choose Starting Scenes** are Dune, Star Wars, and Hitchhikers.
> The **Enter Your Name** will be used as a session id to store the session data.
> The **What do you want to do in the scene?** will be used to add the user defined action.
> It will take about **2 mins** to download the machine learning models

## Usage Example
![Screen Shot 2022-05-27 at 5 10 24 PM](https://user-images.githubusercontent.com/9085803/170801918-5eb35527-8810-435e-a58d-c10156e888ed.png)

## Results
> The results will be the excerpt from the starting scene and generated text from the AI.

![Screen Shot 2022-05-27 at 5 06 31 PM](https://user-images.githubusercontent.com/9085803/170801747-c4728f1d-c990-49aa-b4fc-c8fc8b146c01.png)

## Requirements
To use the machine learning models on the linux virtual machine for Alta3, you will need to install pytorch and transformers

``` 
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
```

![Screen Shot 2022-05-26 at 8 52 04 PM](https://user-images.githubusercontent.com/9085803/170797263-184c1e92-5582-43a0-96f6-1d34df409911.png)

```
pip install transformers
```

It generally takes about 2 mins, since the models have to be downloaded each time the program runs, and the model has to perform tokenization.

