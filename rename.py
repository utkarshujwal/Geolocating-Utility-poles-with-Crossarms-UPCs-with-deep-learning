import os
import json

path_json = "./New folder/LS_area/metadata.json"
src_dir = "./New folder/LS_area/"
saved_dir = "./renamedfiles/"

files_list = os.listdir(src_dir)
imgs_list = list(filter(lambda file: ".jpg" in file, files_list))

with open(path_json, 'r', encoding='utf8') as fp:
    json_data = json.load(fp)
    print("Num data samples:", len(json_data))
    
    for i, content_dict in enumerate(json_data):
        # print(i, ":",  content_dict)
        src_filename = content_dict["_file"]
        src_path = os.path.join(src_dir, src_filename)
        if not os.path.exists(src_path):
            continue
        
        test = str(content_dict["location"]["lat"])
        
        # without longitude and latitude
        # tgt_filename = content_dict["pano_id"] + "_" + content_dict["date"] + "_" + content_dict["_file"]
        
        # with longitude and latitude
        tgt_filename = content_dict["pano_id"] + "_" + str(content_dict["location"]["lat"]) + "_" \
                       + str(content_dict["location"]["lng"]) + "_" + content_dict["date"] + "_" + content_dict["_file"]
        tgt_path = os.path.join(saved_dir, tgt_filename)
        os.rename(src_path, tgt_path)
        print("i: %d, renamed_filename: %s" %(i, tgt_filename))
        

