## 常用函数

* read(filename) 直接读取ini文件内容
* sections() 得到所有的section，并以列表的形式返回
* options(section) 得到该section的所有option
* items(section) 得到该section的所有键值对
* get(section,option) 得到section中option的值，返回为string类型
* getint(section,option) 得到section中option的值，返回为int类型
* getboolean(section,option)
* getfloat(section,option)
* write(fp) 将config对象写入至某个 .init 格式的文件
* add_section(section) 添加一个新的section
* set( section, option, value) 对section中的option进行设置
* remove_section(section) 删除某个 section
* remove_option(section, option) 删除某个 section 下的 option
