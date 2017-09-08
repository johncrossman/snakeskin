import pytest
from snakeskin.models.tenant import Tenant
from snakeskin.models.user import User

@pytest.fixture
def fixture_tenants(app, db_session):

    ucb = Tenant(name='UC Berkeley', scheme='https', domain='bcourses.berkeley.edu', token='secret')
    ucoe = Tenant(name='UC Online Education', scheme='https', domain='cole2.uconline.edu', token='secret')

    db_session.add(ucb)
    db_session.add(ucoe)
    db_session.commit()

    return [ucb, ucoe]

@pytest.fixture
def fixture_tenant_users(db_session):
    tenant = Tenant(name='Faber College')

    db_session.add(tenant)
    db_session.commit()

    dorfman = User('Kent Dorfman', '2031393275', tenant)
    kroger = User('Larry Kroger', '3032092610', tenant)

    db_session.add(dorfman)
    db_session.add(kroger)
    db_session.commit()

    return [dorfman, kroger]
