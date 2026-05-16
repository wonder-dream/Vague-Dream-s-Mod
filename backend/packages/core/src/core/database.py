from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from config import get_settings

engine = None
async_session_maker = None

Base = declarative_base()



def init_engine():
    global engine, async_session_maker

    settings = get_settings()
    url = settings.database_url

    engine = create_async_engine(
        url=url,
        pool_size=10,
        max_overflow=20,
        pool_pre_ping=True,
        echo=True,          # 上线前记得改回 False
    )

    async_session_maker = async_sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

async def get_db() :
    session = async_session_maker()

    try:
        yield session
        await session.commit()
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()
