from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import func

# 데이터베이스 엔진 설정
engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()

# 모델 베이스 클래스
Base = declarative_base()

def print_all_data(session):
    # 모든 사용자 출력
    all_users = session.query(User).all()
    print("All Users:")
    for user in all_users:
        print(user)

    # 모든 게시글 출력
    all_posts = session.query(Post).all()
    print("All Posts:")
    for post in all_posts:
        print(post)


# 사용자 테이블을 정의하는 모델
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    posts = relationship("Post", back_populates="author")

    def __repr__(self):
        return f"<User(name={self.name}, age={self.age})>"

# 게시글 테이블을 정의하는 모델
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    author = relationship("User", back_populates="posts")

    def __repr__(self):
        return f"<Post(title={self.title}, content={self.content})>"

# 테이블 생성
Base.metadata.create_all(engine)
print("Tables created.")
print_all_data(session)

# 데이터 추가
new_user = User(name='John Doe', age=28)
new_post = Post(title='Hello World', content='This is a test post.', author=new_user)
session.add(new_user)
session.add(new_post)
session.commit()
print("Added new user and post:", new_user, new_post)
print_all_data(session)

# 데이터 조회
users = session.query(User).filter(User.age > 20).all()
print("Users older than 20:", users)
print_all_data(session)

# 데이터 수정
user = session.query(User).filter_by(name='John Doe').first()
if user:
    user.age = 30
    session.commit()
    print("Updated user age:", user)
    print_all_data(session)

# 데이터 삭제
session.delete(new_post)
session.commit()
print("Deleted post:", new_post)
print_all_data(session)

# 복합 쿼리
users_with_posts = session.query(User).join(Post).filter(Post.content.like('%test%')).all()
print("Users with posts containing 'test':", users_with_posts)
print_all_data(session)
