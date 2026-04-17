from __future__ import annotations

import logging
from typing import Any
from Backend.api.templates import feats, spells
from Backend.api.models.core.skills import Enhanced, Skill, SkillFeat, SkillSpell, SkillType, God
from Backend.api.data.repository import EnhancedRepository, SkillRepository, SkillFeatRepository, SkillSpellRepository

log = logging.getLogger(__name__)


def _load_existing_skill_labels(skill_type: SkillType) -> set[str]:
    result = SkillRepository.get_by_type(skill_type)
    if result.is_err():
        log.error("Impossibile caricare le skill esistenti (%s): %s",
                  skill_type, result.unwrap_err())
        return set()
    return {skill.label for skill in result.unwrap()}


def _load_existing_enhanced_labels() -> set[str]:
    result = EnhancedRepository.get_all()
    if result.is_err():
        log.error("Impossibile caricare gli Enhanced esistenti: %s",
                  result.unwrap_err())
        return set()
    return {e.label for e in result.unwrap()}


def _get_or_create_enhanced(label: str, description: str | None, existing_labels: set[str]) -> Enhanced | None:
    if label in existing_labels:
        result = EnhancedRepository.get_by_label(label)
        if result.is_err():
            log.error(
                "Enhanced '%s' segnalato come esistente ma non trovato: %s", label, result.unwrap_err())
            return None
        return result.unwrap()

    enhanced = Enhanced(label=label, description=description)
    result = EnhancedRepository.create(enhanced)
    if result.is_err():
        log.error("Impossibile creare Enhanced '%s': %s",
                  label, result.unwrap_err())
        return None

    existing_labels.add(label)
    log.debug("Enhanced creato: %s", label)
    return result.unwrap()


def _seed_feats(feats: list[dict[str, Any]], existing_labels: set[str]) -> tuple[int, int]:
    inserted = skipped = 0

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
        skill_result = SkillRepository.create(skill)
        if skill_result.is_err():
            log.error("Impossibile creare Skill '%s': %s",
                      label, skill_result.unwrap_err())
            continue

        created_skill = skill_result.unwrap()

        skill_feat = SkillFeat(skill_id=created_skill.id)
        feat_result = SkillFeatRepository.create(skill_feat)
        if feat_result.is_err():
            log.error("Impossibile creare SkillFeat per '%s': %s",
                      label, feat_result.unwrap_err())
            continue

        existing_labels.add(label)
        log.debug("Talento inserito: %s", label)
        inserted += 1

    return inserted, skipped


def _seed_spells(spells: list[dict[str, Any]], existing_skill_labels: set[str], existing_enhanced_labels: set[str]) -> tuple[int, int]:
    inserted = skipped = 0

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
            enhanced = _get_or_create_enhanced(
                label=enh_data["name"],
                description=enh_data.get("description"),
                existing_labels=existing_enhanced_labels,
            )

        skill = Skill(
            label=label,
            description=spell_data.get("description"),
            type=SkillType.spell,
        )
        skill_result = SkillRepository.create(skill)
        if skill_result.is_err():
            log.error("Impossibile creare Skill '%s': %s",
                      label, skill_result.unwrap_err())
            continue

        created_skill = skill_result.unwrap()

        god_value: God = spell_data["god"]
        affinity_level: int | None = spell_data.get("affinity_level")

        skill_spell = SkillSpell(
            skill_id=created_skill.id,
            affinity_with=god_value,
            affinity_level=affinity_level,
            enhanced_effect_id=enhanced.id if enhanced is not None else None,
        )
        spell_result = SkillSpellRepository.create(skill_spell)
        if spell_result.is_err():
            log.error("Impossibile creare SkillSpell per '%s': %s",
                      label, spell_result.unwrap_err())
            continue

        existing_skill_labels.add(label)
        log.debug("Incantesimo inserito: %s (dio=%s)", label, god_value.value)
        inserted += 1

    return inserted, skipped


def run_seed() -> None:
    logging.basicConfig(level=logging.INFO)

    existing_feat_labels = _load_existing_skill_labels(SkillType.feat)
    existing_spell_labels = _load_existing_skill_labels(SkillType.spell)
    existing_enhanced_labels = _load_existing_enhanced_labels()

    feat_ins, feat_skip = _seed_feats(feats, existing_feat_labels)
    log.info("Talenti → inseriti: %d | saltati: %d", feat_ins, feat_skip)

    spell_ins, spell_skip = _seed_spells(
        spells, existing_spell_labels, existing_enhanced_labels)
    log.info("Incantesimi → inseriti: %d | saltati: %d", spell_ins, spell_skip)

    log.info("=== Seed completato ===")
