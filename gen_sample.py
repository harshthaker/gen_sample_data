import os
from shutil import copyfile
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_dir")
parser.add_argument("output_dir")
parser.add_argument("train_size")
parser.add_argument("val_size")
args=parser.parse_args()

def gen_sample_data(input_dir,output_dir, train_sample_size, val_sample_size):
    
    #storing names of directories-these are class names
    dirs = [d for d in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, d))]
    
    data_dir = ['train','validation'] #array storing train, validation names
    
    #create folders with similar class names for both train and validation in output dir
    for data_name in data_dir:
        for dir_name in dirs:
            output_path = os.path.join(output_dir,data_name,dir_name)
            if not os.path.exists(output_path):
                os.makedirs(output_path)
    
    #copying images from each class dir to train and validation class dir with sample size
    for dir_name in dirs:
        file_names=[]
        for f in os.listdir(os.path.join(input_dir,dir_name)):
            file_names.append(os.path.join(input_dir,dir_name,f))
        for i in range(0,train_sample_size):
            copyfile(file_names[i], os.path.join(output_dir,"train",dir_name,os.path.basename(file_names[i])))
            print(os.path.join(output_dir,"train",dir_name+os.path.basename(file_names[i])))
        for j in range(train_sample_size,(train_sample_size+val_sample_size)):
            copyfile(file_names[j], os.path.join(output_dir,"validation",dir_name,os.path.basename(file_names[j])))
            print(os.path.join(output_dir,"validation",dir_name+os.path.basename(file_names[j])))
        
gen_sample_data(args.input_dir,args.output_dir,int(args.train_size),int(args.val_size))
