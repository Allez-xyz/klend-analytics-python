import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
from external_klend_utils import (
    get_all_obligations_df,
    get_kamino_lend_program,
    get_all_obligations,
    EXTERNAL_KLEND_UTILS_VERSION,
)
import os
from dotenv import load_dotenv
import sys
import pandas as pd


async def main():
    if EXTERNAL_KLEND_UTILS_VERSION:
        print(f"version {EXTERNAL_KLEND_UTILS_VERSION}")
    else:
        print("none found")
    market = "BJnbcRHqvppTyGesLzWASGKnmnF1wq9jZu6ExrjT7wvF"
    uri = os.getenv("SOLANARPC_HTTP_URI")
    kamino_lend_program = get_kamino_lend_program(uri)
    obligations_list = await get_all_obligations(
        kamino_lend_program, market_pubkey=market
    )
    obl_df = get_all_obligations_df(obligations_list, only_positive_deposit=True)
    print(obl_df.columns)


if __name__ == "__main__":
    asyncio.run(main())
