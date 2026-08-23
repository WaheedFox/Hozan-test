import re

import pytest

from hozan.features.identity import HozanIdentityService, MemoryAccountRepository


@pytest.mark.asyncio
async def test_first_start_creates_one_free_identity():
    service = HozanIdentityService(MemoryAccountRepository())
    account = await service.get_or_create_account(telegram_user_id=123, name="Queen")

    assert account.telegram_user_id == 123
    assert len(account.identities) == 1
    assert account.identities[0].free
    assert re.fullmatch(r"#[0-9]{8}", account.identities[0].value)


@pytest.mark.asyncio
async def test_start_is_idempotent():
    service = HozanIdentityService(MemoryAccountRepository())
    first = await service.get_or_create_account(telegram_user_id=123, name="Queen")
    second = await service.get_or_create_account(telegram_user_id=123, name="Changed")

    assert second == first
    assert len(second.identities) == 1
