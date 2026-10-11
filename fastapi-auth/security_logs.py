from datetime import datetime, timezone

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    Text,
)

from database import Base


class LoginLog(Base):
    __tablename__ = "login_logs"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String(150), index=True, nullable=False)

    ip_address = Column(String(45), nullable=True)

    user_agent = Column(Text, nullable=True)

    login_time = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    success = Column(Boolean, nullable=False)

    failure_reason = Column(String(100), nullable=True)