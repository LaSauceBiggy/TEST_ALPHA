from src.actions.base import BaseAction


class FightSkillAction(BaseAction):
    max_retry = 1
    timeout = 5

    async def _wait(self):
        pass

    async def execute(self):
        pass
