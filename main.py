from clicksignlib import ClickSign
from clicksignlib.environments import SandboxEnvironment
from clicksignlib.run_in_asyncio import run
from clicksignlib.adapters import AioHttpAdapter


def func():
    cs = ClickSign(access_token="5b16a751-a78f-4713-a20c-02a4dcf26b19",
                   environment=SandboxEnvironment(), requests_adapter=AioHttpAdapter())
    x = cs.template.list()
    print(x)
    run(x)
