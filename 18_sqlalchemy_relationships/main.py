from sqlalchemy import (
    create_engine,
    update, func,
)
from sqlalchemy.orm import (
    Session,
    declarative_base, joinedload, selectinload,
)
from models import Base, User, Author, Post
import config

engine = create_engine(
    url=config.DB_URL,
    echo=config.DB_ECHO,
)


def create_user(session: Session, username: str) -> User:
    user = User(username=username)
    print("user", user)
    session.add(user)
    session.commit()
    print("saved_user", user)
    return user


# def create_author(session: Session, name: str, user_id: int)-> Author:
def create_author(session: Session, name: str, user: User) -> Author:
    author = Author(
        name=name,
        user=user,
        # user_id=user_id
    )
    session.add(author)
    session.commit()
    print("created author", author)
    return author


def show_users_with_authors(session: Session):
    users = session.query(User).all()
    for user in users:
        print(user, user.author)


def show_authors_with_users(session: Session):
    authors = (
        session.query(Author).options(
            joinedload(Author.user)).all()
    )
    for author in authors:
        print(author, author.user)


def show_users_only_with_authors(session: Session):
    users = (
        session.query(User)
        # .join(User.author)
        .options(
            joinedload(User.author, innerjoin=True))
        # .filter(Author.user_id.isnot(None),)
        .all()
    )
    for user in users:
        print(user, user.author)


def update_users_email_by_username(session: Session, domain: str, *filters):
    session.query(User).filter(*filters).update({
        User.email: User.username + domain,
    },
        synchronize_session=False
    )
    session.commit()


def find_authors_by_user_email_domain(session: Session, email_domain: str):
    authors = (
        session.query(Author)
        .join(Author.user)
        .filter(User.email.endswith(email_domain))
        .options(joinedload(Author.user))
        .all()
    )
    for author in authors:
        print(author, author.user)


def find_author_by_user_name(session: Session, username: str):
    return (session.query(Author)
            .join(Author.user)
            .filter(User.username == username)
            .one()
            )


def create_post(session: Session, author: Author, *titles: str, ) -> list[Post]:
    posts = [Post(title=title, author_id=author.id,
                  )
             for title in titles
             ]
    session.add_all(posts)
    session.commit()
    print("Post", posts)
    return posts


def show_users_with_author_and_posts(session: Session,):
    users = (
        session.query(User)
        .options(
            # joinedload(User.author).joinedload(Author.post)
            joinedload(User.author).selectinload(Author.post)
        )
        .order_by(User.id)
        .all()
    )
    for user in users:
        print("-user", user)
        if not user.author:
            continue
        print("++ author", user.author)
        print("== posts:")
        for post in user.author.posts:
            print("=", post)


def show_authors_with_users_and_posts(session: Session):
    authors = (
        session.query(Author)
        .options(
            joinedload(Author.user),
            selectinload(Author.posts),
        )
        .order_by(Author.id)
        .all()
    )
    for author in authors:
        print("+", author)
        print("+++", author.user)
        print("== posts:")
        for post in author.posts:
            print("---", post)


def main():
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    with Session(engine) as session:
        # john = create_user(session, username="john")
        # sam = create_user(session, username="sam")
        # author_john = create_author(session, "John Smith", user=john)
        # author_sam = create_author(session, "Sam Backman", user=sam)
        # show_users_with_authors(session)
        # show_authors_with_users(session)
        # show_users_only_with_authors(session)
        # bob = create_user(session, username="bob")
        # alice = create_user(session, username="alice")
        # update_users_email_by_username(session, "@gmail.com",)
        # update_users_email_by_username(session, "@yahoo.com", func.length(User.username) < 4)
        # author_sam = find_author_by_user_name(session, "sam")
        # create_post(session, author_sam, "Postgres news", "MySQL Tutorial")
        # find_authors_by_user_email_domain(session, "@yahoo.com")
        # show_users_with_author_and_posts(session)
        show_authors_with_users_and_posts(session)

if __name__ == '__main__':
    main()
