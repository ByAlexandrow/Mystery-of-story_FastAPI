import pytest

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.models.user import SuperUser
from app.models.article import Article, Carousel
from app.models.category import Category


DATABASE_URL = 'sqlite+aiosqlite:///./test.db'

engine = create_async_engine(DATABASE_URL, echo=True)
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)


@pytest.fixture(scope='function')
async def test_db():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope='function')
async def db_session(test_db):
    async with TestingSessionLocal() as session:
        yield session


@pytest.fixture(scope='function')
async def fixture_create_test_category(db_session):
    async with db_session as session:
        test_category = Category(
            title='Test Category',
            cover_img='path/to/category_img.jpg',
            description='This is a test category!'
        )
        session.add(test_category)
        await session.commit()
        await session.refresh(test_category)

    return test_category


@pytest.fixture(scope='function')
async def fixture_create_test_article(db_session, fixture_create_test_category):
    async with db_session as session:
        test_article = Article(
            title='Test Article',
            cover_img='path/to/article_img.jpg',
            description='This is a test article!',
            content='Here will be a content for the article!',
            pdf='path/to/the/pdf_file.pdf',
            category_id=fixture_create_test_category.id
        )
        session.add(test_article)
        await session.commit()
        await session.refresh(test_article)

    return test_article


@pytest.fixture(scope='function')
async def fixture_create_test_carousel(db_session, fixture_create_test_article):
    async with db_session as session:
        test_carousel = Carousel(
            title='First Carousel',
            url='path/to/the/first_img.jpg',
            article_id=fixture_create_test_article.id
        )
        session.add(test_carousel)
        await session.commit()
        await session.refresh(test_carousel)
    
    return test_carousel


@pytest.fixture(scope='function')
async def fixture_create_test_admin(db_session):
    async with db_session as session:
        test_admin = SuperUser(
            username='Username',
            first_name='Name',
            last_name='Surname',
            email='admin@mail.ru',
            password='123456789',
            is_admin=True
        )
        session.add(test_admin)
        await session.commit()
        await session.refresh(test_admin)
    
    return test_admin
