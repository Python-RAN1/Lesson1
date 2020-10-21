import os
import re
import mobatch_tool

log_path = mobatch_tool.mobatch_tool(1,2,3)

def log_split(log_path,split_path):
    # 遍历log目录中的所有log文件
    for  root_dir, dirs, files in os.walk(log_path):
        for file in files:
            # 获取log文件名
            site_name = file.split(".")[0].upper()
            # 判断路径是否存在如果不存在就创建
            if not os.path.isdir(split_path+"/"+site_name):
                os.makedirs(split_path+"/"+site_name)
            with open(f"{root_dir}/{file}","r") as f:
                # 读取log文件
                log = f.read()
                # 对log文件中的指令进行切割
                log_list = log.split(f"{site_name}> ")
                x = False
                for command_info in log_list:
                    # 获取指令
                    command = re.split("\n",command_info)[0]
                    # 判断指令是否为ltall
                    if "".join(re.split("\s",command)) in ["ltall",]:
                        x = True
                    if x:
                        # 将指令中的空格或.替换成下划线
                        command = re.sub(r"\s|[\.]",r"_",command)
                        # 将每条指令结果写入log
                        with open(f"{split_path}/{site_name}/{command}.log","w") as log_file:
                            log_file.write(command_info)
    # 执行完成后返回切割路径
    return split_path
if __name__ == '__main__':
    # 需要传递两个参数
    log_split("./logs/","./log_split/")