from typing import cast
from middleware.assets.models.core.items import Inventory
from middleware.config import Result, IOError_, NotFoundError, ok
from middleware.assets.models.core.characters import Character, CharacterCondition, CharacterKnowledge, CharacterSkill, CharacterStat
from Backend.api.repository import CharacterRepository, CharacterStatRepository, CharacterConditionRepository, CharacterKnowledgeRepository, CharacterSkillRepository, InventoryRepository, StatRepository

class CharacterService:
    @classmethod
    async def create_character(cls, name: str, level: int = 1, backstory: str | None = None, origin_id: int | None = None, soul_id: int | None = None) -> Result[Character, IOError_]:
        new_char = Character(
            name=name,
            level=level,
            backstory=backstory,
            origin_id=origin_id,
            soul_id=soul_id,
        )

        char_res = await CharacterRepository.create(new_char)
        if char_res.is_err():
            return char_res

        created_char = char_res.unwrap()

        new_inventory = Inventory(character_id=cast(int, created_char.id))
        await InventoryRepository.create(new_inventory)

        stats_res = await StatRepository.get_all()
        if stats_res.is_ok():
            stats = stats_res.unwrap()
            base_char_stats = []
            for s in stats: base_char_stats.append(CharacterStat(character_id=cast(int, created_char.id), stat_id=cast(int, s.id)))
            if base_char_stats: await CharacterStatRepository.create_all(base_char_stats)

        return ok(created_char)

    @classmethod
    async def get_character_profile(cls, character_id: int) -> Result[Character, NotFoundError | IOError_]:
        return await CharacterRepository.get_full(character_id)

    @classmethod
    async def add_skill(cls, character_id: int, skill_id: int) -> Result[CharacterSkill, IOError_ | NotFoundError]:
        check_res = await CharacterSkillRepository.get_by_composite_id(character_id, skill_id)
        if check_res.is_ok(): return check_res
        return await CharacterSkillRepository.create(CharacterSkill(character_id=character_id, skill_id=skill_id))

    @classmethod
    async def add_condition(cls, character_id: int, condition_id: int) -> Result[CharacterCondition, IOError_ | NotFoundError]:
        check_res = await CharacterConditionRepository.get_by_composite_id(character_id, condition_id)
        if check_res.is_ok():return check_res
        return await CharacterConditionRepository.create(CharacterCondition(character_id=character_id, condition_id=condition_id))

    @classmethod
    async def remove_condition(cls, character_id: int, condition_id: int) -> Result[None, NotFoundError | IOError_]:
        return await CharacterConditionRepository.delete_by_composite_id(character_id, condition_id)

    @classmethod
    async def add_knowledge(cls, character_id: int, knowledge_id: int, is_proficient: bool = False) -> Result[CharacterKnowledge, IOError_ | NotFoundError]:
        check_res = await CharacterKnowledgeRepository.get_by_composite_id(
            character_id, knowledge_id)
        if check_res.is_ok():
            existing = check_res.unwrap()
            if existing.is_proficient != is_proficient:
                del_res = await CharacterKnowledgeRepository.delete_by_composite_id(character_id, knowledge_id)
                if del_res.is_err(): return del_res  # type: ignore
            else: return check_res

        return await CharacterKnowledgeRepository.create(CharacterKnowledge(character_id=character_id, knowledge_id=knowledge_id, is_proficient=is_proficient))
