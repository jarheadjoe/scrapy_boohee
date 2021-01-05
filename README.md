# scrapy_boohee
最全的爬取薄荷网食物热量统计，8k+食物详情与图片

#### 使用说明

- 首先运行食物名称爬虫

  > scrapy_boohee/: __scrapy crawl food_name -o food_name.json__

  如果出现503(爬虫部分失败)，则将food_name.json的内容移至food_name_backup.json，再次执行上面的命令。名称爬虫会爬取不在backup文件中的内容

  若全部200(爬取完成)，则将backup中的所有内容合并至food_name.json

- 接着运行食物详情爬虫

  > scrapy_boohee/: __scrapy crawl food_detail -o food_detail.json__

  如果出现503(爬虫部分失败)，则将food_detail.json的内容移至food_deatil_backup.json，再次执行上面的命令。名称爬虫会爬取不在backup文件中的内容

  若全部200(爬取完成)，则将backup中的所有内容合并至food_deatil.json

- 运行data_transfer.py 中的trans_json_to_csv_all会将内容全部写入一个csv中；trans_json_to_csv则会按类别写入csv文件夹内的对应的以类别命名的csv中

- 运行get_pic.py下载所有图片

#### 注意事项

所有文件夹与文件已经提前创建。部分文件为我运行的结果，可以作为参考

#### 申明

- 本仓库发布的`scrapy_boohee`项目中涉及的任何脚本，仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断。
- 本项目内所有资源文件，禁止任何公众号、自媒体进行任何形式的转载、发布。
- `jarheadjoe` 对任何脚本问题概不负责，包括但不限于由任何脚本错误导致的任何损失或损害。
- 间接使用脚本的任何用户，包括但不限于建立VPS或在某些行为违反国家/地区法律或相关法规的情况下进行传播, `jarheadjoe` 对于由此引起的任何隐私泄漏或其他后果概不负责。
- 请勿将`scrapy_boohee`项目的任何内容用于商业或非法目的，否则后果自负。
- 如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
- 您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
- 本项目遵循`GPL-3.0 License`协议，如果本特别声明与`GPL-3.0 License`协议有冲突之处，以本特别声明为准。





