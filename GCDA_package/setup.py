import setuptools
# 需要将那些包导入
packages = ["GCDA"]

# 导入静态文件
file_data = [("GCDA", ["GCDA/german_credit_data.csv"])]

# 第三方依赖
requires = ["pandas>=0.20.0", "sklearn>=0.0", "seaborn>=0.9.0"]

# 自动读取readme
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GCDA",  # 包名称
    version="0.1.1",  # 包版本
    description="German Credit Data Analysis",  # 包详细描述
    long_description=long_description,  # 长描述，通常是readme，打包到PiPy需要
    long_description_content_type="text/markdown",
    author="Dear MrWangwll",  # 作者名称
    author_email="1256847435@qq.com",  # 作者邮箱
    url="https://github.com/DearMrWangwll",  # 项目官网
    packages=packages,  # 项目需要的包
    data_files=file_data,  # 打包时需要打包的数据文件，如图片，配置文件等
    include_package_data=True,  # 是否需要导入静态数据文件
    python_requires=">=3.0, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3*",  # Python版本依赖
    install_requires=requires,  # 第三方库依赖
    zip_safe=False,  # 此项需要，否则卸载时报windows error
    classifiers=[  # 程序的所属分类列表
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
