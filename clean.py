# 导入必要库
import pandas as pd
import argparse

# 解析命令行参数（3个位置参数）
parser = argparse.ArgumentParser(description="Data cleaning script for survey data")
parser.add_argument("input1", help="Path to respondent_contact.csv")
parser.add_argument("input2", help="Path to respondent_other.csv")
parser.add_argument("output", help="Path to save cleaned data")
args = parser.parse_args()

# 读取两个原始数据文件
df_contact = pd.read_csv(args.input1)
df_other = pd.read_csv(args.input2)

# 合并文件（内连接，只保留共同的respondent）
df_merged = pd.merge(
    left=df_contact,
    right=df_other,
    left_on="respondent_id",
    right_on="id",
    how="inner"
)
df_merged = df_merged.drop(columns=["id"])  # 删除重复的id列

# 删除有缺失值的行
df_cleaned = df_merged.dropna()

# 过滤job列包含insurance的行（忽略大小写）
df_cleaned = df_cleaned[~df_cleaned["job"].str.contains("insurance", case=False)]

# 打印输出文件形状（Task3要求）
print(f"Cleaned data shape: {df_cleaned.shape}")

# 保存清洗后的数据
df_cleaned.to_csv(args.output, index=False)