1. 配置虚拟环境 python3 -m venv env
2. 激活虚拟环境 ./Script/bin/activate
3. 下载环境安装依赖 pip3 install -r requirements.txt -i http://pypi.douban.com/simple -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
4. 配置数据，将数据文件放置在docs目录下，例如目前的：20221.docx、20222.docx
5. 执行脚本提取文件：python3 extract_nums_info.py 
6. 提取的文件最后会放置在：extract_out目录下的2022_en.xlsx中
7. 注意：执行脚本钱需要先把docs和extract_out目录下的文件清除，避免把测试数据提取出俩