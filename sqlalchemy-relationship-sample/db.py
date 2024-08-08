import os

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# DBファイル作成
base_dir = os.path.dirname(__file__)
database = "sqlite:///" + os.path.join(base_dir, "data.sqlite")

# データベースエンジンを作成
db_engine = create_engine(database, echo=True)
Base = declarative_base()


# モデル
# 部署
class Department(Base):
    # テーブル名
    __tablename__ = "departments"
    # 部署ID
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 部署名
    name = Column(String, nullable=False, unique=True)
    # リレーション：1対多
    employees = relationship("Employee", back_populates="department")

    # 表示用関数
    def __str__(self):
        return f"部署ID：{self.id}, 部署名：{self.name}"


# 従業員
class Employee(Base):
    # テーブル名
    __tablename__ = "employees"
    # 従業員ID
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 従業員名
    name = Column(String, nullable=False)
    # 部署ID
    # ForeignKeyには「テーブル名.カラム名」を指定
    department_id = Column(Integer, ForeignKey("departments.id"))
    # リレーション：1対1
    department = relationship(
        "Department", back_populates="employees", uselist=False
    )

    # 表示用関数
    def __str__(self):
        return f"従業員ID：{self.id}, 従業員名：{self.name}"


# テーブル操作
print("(1)テーブルを削除してから作成")
Base.metadata.drop_all(db_engine)
Base.metadata.create_all(db_engine)

# セッションの生成
session_maker = sessionmaker(bind=db_engine)
session = session_maker()

# データ作成
print("(2)データ登録：実行")

# 部署
dept01 = Department(name="開発部")
dept02 = Department(name="営業部")

# 従業員
emp01 = Employee(name="太郎")
emp02 = Employee(name="ジロウ")
emp03 = Employee(name="さぶろう")
emp04 = Employee(name="花子")

# 部署に従業員を紐付ける
# 開発部：太郎、ジロウ
dept01.employees.append(emp01)
dept01.employees.append(emp02)

# 営業部：さぶろう、花子
dept02.employees.append(emp03)
dept02.employees.append(emp04)

# セッションで「部署」を登録
session.add_all([dept01, dept02])
session.commit()

print("(3)データ参照：実行")
print("■：Employeeの参照")
target_emp = session.query(Employee).filter_by(id=1).first()
print(target_emp)
print("■：Employeeに紐付いたDepartmentの参照")
print(target_emp.department)

print("■" * 100)

print("■：Departmentの参照")
target_dept = session.query(Department).filter_by(id=1).first()
print(target_dept)
print("■：Departmentに紐付いたのEmployeeの参照")
for emp in target_dept.employees:
    print(emp)
