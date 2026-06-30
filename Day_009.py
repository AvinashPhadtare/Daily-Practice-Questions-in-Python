import asyncio
import time

async def fetch_member_plan(member_id: int) -> dict:
    await asyncio.sleep(1)  # simulates DB delay
    plans = {1: "basic", 2: "premium", 3: "vip", 4: "basic", 5: "premium"}
    return {"member_id": member_id, "plan": plans.get(member_id, "unknown")}

async def fetch_all_plans(member_ids: list[int]) -> list[dict]:
    tasks = [fetch_member_plan(member_id) for member_id in member_ids]
    return await asyncio.gather(*tasks)

async def main() -> None:
    member_ids = [1, 2, 3, 4, 5]
    start = time.perf_counter()
    plans = await fetch_all_plans(member_ids)
    duration = time.perf_counter() - start

    print(f"Fetched {len(plans)} plans in {duration:.2f} seconds")
    for plan in plans:
        print(plan)

if __name__ == "__main__":
    asyncio.run(main())
