import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize


def print_value_range(data):
    # 打印 对应列 的 取值范围
    print("Purpose : ", data.Purpose.unique())
    print("Sex : ", data.Sex.unique())
    print("Housing : ", data.Housing.unique())
    print("Saving accounts : ", data["Saving accounts"].unique())
    print("Checking account : ", data["Checking account"].unique())


def map2num(data):
    # 将 取值范围（非数值） 映射为 具体的数字
    # Purpose
    data["Purpose"] = data["Purpose"].map({
        'radio/TV': 0,
        'education': 1,
        'furniture/equipment': 2,
        'car': 3,
        'business': 4,
        'domestic appliances': 5,
        'repairs': 6,
        'vacation/others': 7,
    }).astype(float)

    # Sex
    data["Sex"] = data["Sex"].map({
        'male': 0,
        'female': 1,
    }).astype(float)

    # Housing
    data["Housing"] = data["Housing"].map({
        'own': 0,
        'free': 1,
        'rent': 2,
    }).astype(float)

    # Saving accounts
    data["Saving accounts"] = data["Saving accounts"].map({
        'little': 0,
        'moderate': 1,
        'quite rich': 2,
        'rich': 3,
    }).astype(float)
    # nan —— 缺失值，用已知的数据的平均值代替
    average_saving_accounts = data["Saving accounts"].dropna().mean()
    data["Saving accounts"] = data["Saving accounts"].fillna(
        average_saving_accounts)

    # Saving accounts
    data["Checking account"] = data["Checking account"].map({
        'little': 0,
        'moderate': 1,
        'rich': 2,
    }).astype(float)
    # nan —— 缺失值，用已知的数据的平均值代替
    average_checking_account = data["Checking account"].dropna().mean()
    data["Checking account"] = data["Checking account"].fillna(
        average_checking_account)

    return data


def visualize(data):
    # 绘制所有属性两两对应的散点图
    sns.pairplot(data)
    plt.show()

    # 绘制 Credit amount - Duration 散点图
    plt.scatter(data["Credit amount"], data["Duration"])
    plt.show()

    # 绘制 Saving accounts - Duration 散点图
    plt.scatter(data["Saving accounts"], data["Duration"])
    plt.show()

    # 绘制 Purpose 直方图
    fig = data["Purpose"].hist(bins=8)
    fig.text(-1, 150, "Frequency", ha='center')
    fig.text(0, -30, "radio", ha='center')
    fig.text(1, -50, "education", ha='center')
    fig.text(2, -30, "furniture", ha='center')
    fig.text(3, -50, "car", ha='center')
    fig.text(4, -30, "business", ha='center')
    fig.text(5, -50, "appliances", ha='center')
    fig.text(6, -30, "repairs", ha='center')
    fig.text(7, -50, "vacation", ha='center')
    plt.show()

    # 绘制 Purpose 直方图（只考虑 2000 < Credit amount <= 5000）
    limited_credit = data[(data["Credit amount"] <= 5000)]
    limited_credit = limited_credit[(limited_credit["Credit amount"] >
                                     2000)]  # 教程的代码好像有问题
    fig = limited_credit["Purpose"].hist(bins=8)
    fig.text(-1, 60, "Frequency", ha='center')
    fig.text(0, -30, "radio", ha='center')
    fig.text(1, -50, "education", ha='center')
    fig.text(2, -30, "furniture", ha='center')
    fig.text(3, -50, "car", ha='center')
    fig.text(4, -30, "business", ha='center')
    fig.text(5, -50, "appliances", ha='center')
    fig.text(6, -30, "repairs", ha='center')
    fig.text(7, -50, "vacation", ha='center')
    plt.show()

    # 绘制 Age 直方图
    fig = data.Age.hist(bins=60)
    fig.text(10, 25, "Frequency", ha='center')
    fig.text(50, -10, "Age", ha='center')
    plt.show()

    # 绘制 Job 直方图
    fig = data.Job.hist()
    fig.text(-0.5, 350, "Frequency", ha='center')
    fig.text(0, -100, "UnSkilled", ha='center')
    fig.text(1, -100, "UnSkilled Resident", ha='center')
    fig.text(2, -100, "Skilled", ha='center')
    fig.text(3, -100, "Highly Skilled", ha='center')
    plt.show()


def cluster(data):
    # 使用 k-均值聚类 算法对数据进行分类
    label = KMeans().fit_predict(data)

    # 显示分类结果（对 Credit amount - Age 散点图 染色）
    plt.scatter(data['Credit amount'], data['Age'], c=label)
    plt.show()

    return label


def decomposition(data, label):
    # 使用 主成分分析法（PCA） 对数据进行降维（降到2维方便可视化）
    X_norm = normalize(data)
    y_PCA = PCA(n_components=2).fit_transform(X_norm, 2)
    print(y_PCA.shape)

    # 显示降维结果
    plt.scatter(y_PCA[:, 0], y_PCA[:, 1], c=label)
    plt.show()


def main():
    # 导入数据
    import os
    file_path = os.path.join(
        os.path.dirname(__file__), "german_credit_data.csv")
    Data = pd.read_csv(file_path)

    # 检查文件是否正确读入
    print(Data.columns)
    print(Data.head(n=10))
    print_value_range(Data)

    # 数据预处理
    Data = map2num(Data)
    print(Data.head(10))  # 打印处理后的数据

    # 绘图
    visualize(Data)

    # 使用 sklearn 进行进一步数据处理
    label = cluster(Data)
    decomposition(Data, label)


if __name__ == "__main__":
    main()
