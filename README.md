# gen_sample_data
This Python script helps you generate sample train, validation data from the data. The data is expected to be in a directory having sub-directories for each class. Each sub-directory consists of images belong to that class.

Running this script will create train and validation directory in output directory that will have the sample data. Next it will generate sub-directories with each class name. It will transfer the number of images specified in train_size for sample training data and val_size for sample validation data.

<b> Usage </b>

python3 gen_sample.py [-h] path-to-input_dir path-to-output_dir train_size val_size
