# Style-Transfer-Assignment
A style Transfer algo inspired by Fast Style Transfer and Neural Style Transfer.

### Results

#### Content Image: 
![content](https://github.com/RudeNinja/Style-Transfer-Assignment/blob/main/content.png)


## Some of the results with different style pre-trained models:

![wreck](https://github.com/RudeNinja/Style-Transfer-Assignment/assets/79577317/29402be8-b391-4198-a849-b158deb4bed0)                  

![udnie](https://github.com/RudeNinja/Style-Transfer-Assignment/assets/79577317/522b81a0-3f7d-4629-9429-af9d88068ef2)
![scream](https://github.com/RudeNinja/Style-Transfer-Assignment/assets/79577317/2e99e44d-53f1-406a-8668-060d45bfb896)

## Instructions to RUN

Download the models folder from **[here](https://drive.google.com/drive/folders/1bD2FqHgujMOrR1zCJcRkhSXmWA5ShblH?usp=sharing)** <br>
Download the data folder from **[here](https://drive.google.com/drive/folders/1YQSm8b2OWvxLfftDjeOsO1I_vMSo3QBe?usp=sharing)** <br>

Download and place the above two folders after downloading inside the cloned repo folder.

Run the command: 
```
python evaluate.py --checkpoint path/to/style/model.ckpt \
  --in-path dir/of/test/imgs/ \
  --out-path dir/for/results/
```

Replace the **path/to/style/model.ckpt** with path to your **model.ckpt** (use any one model from the models folder downloaded above).

For running on assets, replace the path to the assests folder and output folder in **batch_eval.py** file with your desired destination.

Run the command:
```
python batch_eval.py
```
My results can be viewed in the folders named **output_whole, output_assets** in this repo.
Alternatively you can download the whole codebase **[here](https://drive.google.com/drive/folders/1C4rpqK5w9hUjFG4xUTC3awbfbD1hcbdw?usp=sharing)** and just run the given commands.

The explanation video can be found **[here](https://drive.google.com/file/d/1DDQvtnMwHp6sSvZdixWOm-xC-swQxZZ8/view?usp=sharing)**
