from __future__ import annotations

import logging
from typing import Any
from middleware.assets.templates import feats, spells, conditions
from middleware.assets.models import Enhanced, Skill, SkillFeat, SkillSpell, SkillType, God, Condition
from Backend.api.repository import EnhancedRepository, SkillRepository, SkillFeatRepository, SkillSpellRepository, ConditionRepository
from middleware.config.core.notification import notify

log = logging.getLogger(__name__)

async def _load_existing_skill_labels(skill_type: SkillType) -> set[str]:
    result = await SkillRepository.get_by_type(skill_type)
    if result.is_err():
        log.error("Impossibile caricare le skill esistenti (%s): %s", skill_type, result.unwrap_err())
        return set()

    skills = result.unwrap()
    labels = {skill.label for skill in skills}

    log.debug("Caricate %d skill esistenti per tipo %s", len(labels), skill_type.value)
    return labels


async def _load_existing_enhanced_labels() -> set[str]:
    result = await EnhancedRepository.get_all()
    if result.is_err():
        log.error("Impossibile caricare gli Enhanced esistenti: %s", result.unwrap_err())
        return set()

    enhanced_list = result.unwrap()
    labels = {e.label for e in enhanced_list}

    log.debug("Caricati %d enhanced esistenti", len(labels))

    return labels

async def _load_existing_condition_labels() -> set[str]:
    result = await ConditionRepository.get_all()
    if result.is_err():
        log.error("Impossibile caricare le Condizioni esistenti: %s", result.unwrap_err())
        return set()

    condition_list = result.unwrap()
    labels = {c.label for c in condition_list}

    log.debug("Caricate %d condizioni esistenti", len(labels))

    return labels


async def _get_or_create_enhanced(label: str, description: str | None, existing_labels: set[str]) -> Enhanced | None:
    if label in existing_labels:
        result = await EnhancedRepository.get_by_label(label)
        if result.is_err():
            log.error("Enhanced '%s' segnalato come esistente ma non trovato: %s", label, result.unwrap_err())
            return None
        return result.unwrap()

    enhanced = Enhanced(label=label, description=description)

    result = await EnhancedRepository.create(enhanced)
    if result.is_err():
        log.error( "Impossibile creare Enhanced '%s': %s", label, result.unwrap_err())
        return None

    existing_labels.add(label)

    log.debug("Enhanced creato: %s", label)

    return result.unwrap()


async def _seed_feats(feats: list[dict[str, Any]], existing_labels: set[str]) -> tuple[int, int]:
    inserted = 0
    skipped = 0

    for feat_data in feats:
        label: str = feat_data["name"]

        if label in existing_labels:
            log.debug("Talento già presente, salto: %s", label)
            skipped += 1
            continue

        skill = Skill(
            label=label,
            description=feat_data.get("description"),
            type=SkillType.feat,
        )

        skill_result = await SkillRepository.create(skill)
        if skill_result.is_err():
            log.error("Impossibile creare Skill '%s': %s", label, skill_result.unwrap_err())
            continue

        created_skill = skill_result.unwrap()
        if created_skill.id is None:
            log.error("Impossibile recuperare l'ID per la Skill '%s'", label)
            continue

        skill_feat = SkillFeat(skill_id=created_skill.id)

        feat_result = await SkillFeatRepository.create(skill_feat)
        if feat_result.is_err():
            log.error("Impossibile creare SkillFeat per '%s': %s", label, feat_result.unwrap_err())
            continue

        existing_labels.add(label)
        inserted += 1

        log.debug("Talento inserito: %s", label)

    return inserted, skipped


async def _seed_spells(spells: list[dict[str, Any]], existing_skill_labels: set[str], existing_enhanced_labels: set[str]) -> tuple[int, int]:
    inserted = 0
    skipped = 0

    for spell_data in spells:
        label: str = spell_data["name"]

        if label in existing_skill_labels:
            log.debug("Incantesimo già presente, salto: %s", label)
            skipped += 1
            continue

        enhanced: Enhanced | None = None
        enhancements: list[dict] = spell_data.get("enhancements") or []

        if enhancements:
            enh_data = enhancements[0]
            enhanced = await _get_or_create_enhanced(
                label=enh_data["name"],
                description=enh_data.get("description"),
                existing_labels=existing_enhanced_labels,
            )

        skill = Skill(
            label=label,
            description=spell_data.get("description"),
            type=SkillType.spell,
        )

        skill_result = await SkillRepository.create(skill)
        if skill_result.is_err():
            log.error("Impossibile creare Skill '%s': %s", label, skill_result.unwrap_err())
            continue

        created_skill = skill_result.unwrap()
        if created_skill.id is None:
            log.error("Impossibile recuperare l'ID per la Skill '%s'", label)
            continue

        god_value: God = spell_data["god"]
        affinity_level: int | None = spell_data.get("affinity_level")

        skill_spell = SkillSpell(
            skill_id=created_skill.id,
            affinity_with=god_value,
            affinity_level=affinity_level,
            enhanced_effect_id=enhanced.id if enhanced else None,
        )

        spell_result = await SkillSpellRepository.create(skill_spell)
        if spell_result.is_err():
            log.error("Impossibile creare SkillSpell per '%s': %s", label, spell_result.unwrap_err())
            continue

        existing_skill_labels.add(label)
        inserted += 1

        log.debug("Incantesimo inserito: %s (affinità=%s)", label, god_value.value)
        
    return inserted, skipped

async def _seed_conditions(conditions_list: list[dict[str, Any]], existing_labels: set[str]) -> tuple[int, int]:
    inserted = 0
    skipped = 0

    for cond_data in conditions_list:
        label: str = cond_data["label"]

        if label in existing_labels:
            log.debug("Condizione già presente, salto: %s", label)
            skipped += 1
            continue

        cond = Condition(
            label=label,
            description=cond_data.get("description"),
            is_afflicted=cond_data.get("is_afflicted", False)
        )

        result = await ConditionRepository.create(cond)
        if result.is_err():
            log.error("Impossibile creare Condizione '%s': %s", label, result.unwrap_err())
            continue

        existing_labels.add(label)
        inserted += 1

        log.debug("Condizione inserita: %s", label)

    return inserted, skipped

async def run_seed() -> None:
    log.info("=== Avvio procedura di seeding ===")

    existing_feat_labels = await _load_existing_skill_labels(SkillType.feat)
    existing_spell_labels = await _load_existing_skill_labels(SkillType.spell)
    existing_enhanced_labels = await _load_existing_enhanced_labels()
    existing_condition_labels = await _load_existing_condition_labels()

    log.info(
        "Stato iniziale → feats: %d | spells: %d | enhanced: %d",
        len(existing_feat_labels),
        len(existing_spell_labels),
        len(existing_enhanced_labels),
    )

    feat_ins, feat_skip = await _seed_feats(feats, existing_feat_labels)
    log.info("Talenti → inseriti: %d | saltati: %d | totali: %d", feat_ins, feat_skip, len(existing_feat_labels))

    spell_ins, spell_skip = await _seed_spells(spells, existing_spell_labels, existing_enhanced_labels)
    log.info("Incantesimi → inseriti: %d | saltati: %d | totali: %d", spell_ins, spell_skip, len(existing_spell_labels))
    
    cond_ins, cond_skip = await _seed_conditions(conditions, existing_condition_labels) # SEED CONDIZIONI
    log.info("Condizioni → inserite: %d | saltate: %d | totali: %d", cond_ins, cond_skip, len(existing_condition_labels))

    log.info("Enhanced totali: %d", len(existing_enhanced_labels))
    
    total_inserted = feat_ins + spell_ins + cond_ins
    total_skipped = feat_skip + spell_skip + cond_skip
    if total_inserted == 0 and total_skipped == 0: await notify("⚠️ Seed completato ma nessun record inserito o saltato — verifica i template", level="warning")

    log.info("=== Seed completato con successo ===")