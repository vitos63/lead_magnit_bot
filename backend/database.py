from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

DATABASE_URL = "postgresql+asyncpg://user:password@localhost:5432/lead_magnit_bot"

engine = create_async_engine(DATABASE_URL)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def get_session():
    async with SessionLocal() as session:
        yield session
