from Backend.models import *

SPELLS: list[dict] = [
    {
        "name": "Rot",
        "god": God.SULFUR,
        "affinity_level": 1,
        "description": (
            "Rot the victim from inside out to make them vulnerable to attacks. "
            "Increase the enemy's damage taken dice by +1 of the same type as the "
            "original attack for all types of attacks. If the spell is used on "
            "objects, they receive double damage. The Spell lasts for 1d4 turns."
        ),
        "enhancements": [
            {
                "name": "Rotting",
                "cost_mp": 4,
                "affinity_required": 2,
                "description": (
                    "Increase the enemy's damage taken dice by +3, instead of 1. "
                    "If the spell is used on objects, they receive tripled damage."
                ),
            },
            {
                "name": "Putrefy",
                "cost_mp": 8,
                "affinity_required": 3,
                "description": (
                    "Increase the enemy's damage taken dice by +5, instead of 1. "
                    "If the spell is used on objects, they receive quadruple damage."
                ),
            },
        ],
    },
    {
        "name": "Mastery over Vermin",
        "god": God.SULFUR,
        "affinity_level": 2,
        "description": (
            "Gain the ability to talk to those who are often left unseen. You can "
            "summon a swarm of worms to attack enemies within a radius of 3 squares "
            "from the point where you summon them. The worms can cause a random "
            "effect determined by 1d4, which can be Confusion, Poisoning, Nausea, "
            "or Nothing. All enemies within the area must roll against your Conjuring "
            "test to evade. The effect ends at the end of the scene."
        ),
        "enhancements": [
            {
                "name": "Vermin Side",
                "cost_mp": 4,
                "affinity_required": None,
                "description": (
                    "You can ask 3 questions to worms such as frogs, rats, "
                    "earthworms and pigeons; they will truly answer according to "
                    "their knowledge. Furthermore, they can sacrifice themselves "
                    "to feed you by serving as Tier 0 Food."
                ),
            },
            {
                "name": "True Master",
                "cost_mp": 4,
                "affinity_required": None,
                "description": (
                    "Roll 3d4 and add all the effects that drop; if the Confusion "
                    "or Nausea effects drop twice the Poisoning condition level "
                    "increases by 1."
                ),
            },
        ],
    },
    {
        "name": "Flesh Puppetry",
        "god": God.SULFUR,
        "affinity_level": 2,
        "description": (
            "Puppeteer severed limbs at your disposal to attack the enemy. You need "
            "sawed off limbs to do this. Mechanically, it acts as a Combatant Ally, "
            "which you can command to attack using a Simple Action. It gains a bonus "
            "of 4 + your Tenacity to hit, and its punch deals 1d8 damage. The hands "
            "also have Forcing (Guts) equal to +4 and carry out any request you "
            "order. Animated body parts only have 2 MARK before dying instead of 3."
        ),
        "enhancements": [
            {
                "name": "Helping Hand",
                "cost_mp": 4,
                "affinity_required": None,
                "description": "The attack and Forcing (Guts) bonus increases to +8.",
            },
            {
                "name": "Quick Hands",
                "cost_mp": 4,
                "affinity_required": None,
                "description": (
                    "When performing a Simple Action to attack with animated body "
                    "parts, you can use this enhanced effect to make them attack "
                    "four times instead of just once."
                ),
            },
        ],
    },
    {
        "name": "Mischief of Rats",
        "god": God.SULFUR,
        "affinity_level": 3,
        "description": (
            "Summon a mischief of rats to disrupt the enemy. Rats spread confusion "
            "and disease wherever they go. All enemies within a 3 squares radius "
            "centered on a point of your choice must make an Evading (Resilience) "
            "check against your Conjuring (Tenacity) check. If they fail, they all "
            "take 1d6 of magical damage and are inflicted with Concussion 1."
        ),
        "enhancements": [],
    },

    # ── Alll-mer ─────────────────────────────────────────────────────────────
    {
        "name": "Blood Sword",
        "god": God.HASTUR,
        "affinity_level": 1,
        "description": (
            "The blood of Alll-mer boils and rages even ages after his death. Just "
            "a drop sends swords to the heart of his enemies. You summon a sword "
            "that deals magical damage equal to 1d8. This sword lasts until the end "
            "of the scene and can be used with Conjuring (Tenacity) instead of "
            "Killing (Guts)."
        ),
        "enhancements": [
            {
                "name": "Sharp Sword",
                "cost_mp": 0,
                "affinity_required": 2,
                "description": "You increase the sword's damage by 2d8 instead of 1d8.",
            },
            {
                "name": "Powerful Sword",
                "cost_mp": 0,
                "affinity_required": 3,
                "description": "You increase the sword's damage by 3d8 instead of 1d8.",
            },
        ],
    },
    {
        "name": "Inverse Crown of Thorns",
        "god": God.HASTUR,
        "affinity_level": 3,
        "description": (
            "A glimpse of the pain and suffering Alll-mer the ascended one endured "
            "on the cross. You select a target within your Tenacity in squares from "
            "you. Whenever you receive an attack, half of the damage is dealt to the "
            "selected target as magic damage."
        ),
        "enhancements": [
            {
                "name": "The Pain of the Cross",
                "cost_mp": 0,
                "affinity_required": None,
                "description": (
                    "Make a martyrdom test; if you survive you receive 1 affinity "
                    "to one God of your choice."
                ),
            },
        ],
    },

    # ── NEW_GODS ─────────────────────────────────────────────────────────────────
    {
        "name": "Reveal Aura",
        "god": God.NEW_GODS,
        "affinity_level": 1,
        "description": (
            "You can sense the presence of strong enemies around you. Within a "
            "radius of 20 squares centered on you, you can locate all enemies with "
            "a Threat Level equal to half of your Tenacity value. You know their "
            "Threat Level and where they are located."
        ),
        "enhancements": [
            {
                "name": "Humor Aura",
                "cost_mp": 0,
                "affinity_required": None,
                "description": (
                    "You can use this spell to see the real feelings of certain "
                    "people, such as whether they are sad, happy, angry, content, etc."
                ),
            },
        ],
    },
    {
        "name": "Mind Read",
        "god": God.NEW_GODS,
        "affinity_level": 2,
        "description": (
            "A moon magic that reveals the inner thoughts of fellow humans. This "
            "spell allows you to read the surface thoughts of a target, and to "
            "resist this test, the target must roll a Tenacity +5 test. If you "
            "succeed, the target won't know you're reading their mind, and if you "
            "fail, the target will be informed that someone tried to invade their "
            "head."
        ),
        "enhancements": [
            {
                "name": "Enhanced Telepathy",
                "cost_mp": 4,
                "affinity_required": None,
                "description": (
                    "If you fail the test, the target is not informed that someone "
                    "tried to invade their mind, but the bonus they must roll "
                    "increases to +10 instead of +5."
                ),
            },
        ],
    },
    {
        "name": "Golden Gates",
        "god": God.NEW_GODS,
        "affinity_level": 3,
        "description": (
            "A gift from the Moon God himself. Gain access to golden gates that "
            "lead you out from madness and world of deceit. To make this spell "
            "work, you must cast it multiple times in different places. The spell "
            "must be drawn on the ground, so you must be present and have melee "
            "range. After casting it for the second time and being on top of the "
            "spell circle, you can teleport between the marked locations of the spell."
        ),
        "enhancements": [
            {
                "name": "Greater Gates",
                "cost_mp": 4,
                "affinity_required": None,
                "description": (
                    "You can teleport a number of people with you equal to half "
                    "your Tenacity value."
                ),
            },
        ],
    },

    # ── MARDUK ───────────────────────────────────────────────────────────────
    {
        "name": "Pheromones",
        "god": God.MARDUK,
        "affinity_level": 1,
        "description": (
            "Release of pheromones that makes the opponent divert all attention to "
            "the target. You apply the pheromone effect to a willing ally until the "
            "end of the scene. All enemies who attempt to attack must make an "
            "Understanding (Tenacity) test against your initial Conjuring value, and "
            "on a failure, they will attack the target affected by the pheromones."
        ),
        "enhancements": [
            {
                "name": "Hormones and Pheromones",
                "cost_mp": 0,
                "affinity_required": None,
                "description": (
                    "You can use this spell to receive +3 on all Speaking and "
                    "Intimidating tests."
                ),
            },
        ],
    },
    {
        "name": "Loving Whispers",
        "god": God.MARDUK,
        "affinity_level": 2,
        "description": (
            "Concentrated whispers carried out by the older god MARDUK. Heals a "
            "considerable amount of health. Precariously the whisper's effects are "
            "solely based on MARDUK's whims. You heal 2d10+5 Health Points of a "
            "chosen ally within 5 squares of you."
        ),
        "enhancements": [
            {
                "name": "Warming Whispers",
                "cost_mp": 4,
                "affinity_required": None,
                "description": "Increases recover by +2d10.",
            },
        ],
    },
    {
        "name": "Brain Flower",
        "god": God.MARDUK,
        "affinity_level": 2,
        "description": (
            "Plant your personal seeds of brain flower to a fertile ground. Freshly "
            "deceased corpses being the most fertile of grounds. You plant a Brain "
            "flower on a corpse, which restores 1d6 Mind Points. A Brain flower "
            "cannot be planted on a corpse more than once."
        ),
        "enhancements": [
            {
                "name": "Good Fruit",
                "cost_mp": 4,
                "affinity_required": 2,
                "description": "The flower restores 4d4 instead of 1d6.",
            },
        ],
    },
    {
        "name": "Heart Flower",
        "god": God.MARDUK,
        "affinity_level": 2,
        "description": (
            "Plant your personal seeds of heart flower to a fertile ground. Freshly "
            "deceased corpses being the most fertile of grounds. You plant a Heart "
            "flower on a corpse, which restores 1d6 Health Points. A Health flower "
            "cannot be planted on a corpse more than once."
        ),
        "enhancements": [
            {
                "name": "Good Fruit",
                "cost_mp": 4,
                "affinity_required": 2,
                "description": "The flower restores 4d4 instead of 1d6.",
            },
        ],
    },
    {
        "name": "Healing Whispers",
        "god": God.MARDUK,
        "affinity_level": 3,
        "description": (
            "Concentrated whispers carried by the older god MARDUK. Heals a "
            "considerable amount of health of all the party members. You recover "
            "2d6 Health Points for all allies within a 5 squares radius centered "
            "on you."
        ),
        "enhancements": [
            {
                "name": "Warming Whispers",
                "cost_mp": 4,
                "affinity_required": None,
                "description": "Increases recover by +2d6.",
            },
        ],
    },

    # ── MARDUK ──────────────────────────────────────────────────────────────
    {
        "name": "Roots that Reap",
        "god": God.MARDUK,
        "affinity_level": 1,
        "description": (
            "A talented mage can generate a shockwave that travels underground and "
            "forces sharp roots to push through the ground. All enemies within a 3 "
            "squares radius centered on a point of your choice must make an Evading "
            "(Resilience) test against your Conjuring skill. If they fail, they take "
            "4d4 magic damage and suffer the fractured condition."
        ),
        "enhancements": [
            {
                "name": "Crush the Earth",
                "cost_mp": 0,
                "affinity_required": 2,
                "description": (
                    "You can instantly break organic objects like stone, earth, or "
                    "wood walls. The amount you can break is equal to half your "
                    "Tenacity value in height and width, and length."
                ),
            },
        ],
    },
    {
        "name": "Pyromancy Trick",
        "god": God.MARDUK,
        "affinity_level": 1,
        "description": (
            "A simple pyromancy trick to burn your opponents. You inflict the Burn "
            "condition on the enemy and they take double damage from the effect."
        ),
        "enhancements": [
            {
                "name": "Ignition",
                "cost_mp": 0,
                "affinity_required": None,
                "description": "You can set fire to flammable objects.",
            },
        ],
    },
    {
        "name": "Combustion",
        "god": God.MARDUK,
        "affinity_level": 2,
        "description": (
            "A talented mage can control the heart in the atmosphere and create a "
            "large combustion of fire and flames to devour their opponents. You deal "
            "2d4 of magical damage to the opponent and inflict Burn."
        ),
        "enhancements": [
            {
                "name": "Firelight",
                "cost_mp": 0,
                "affinity_required": None,
                "description": "You can set fire to something that is flammable.",
            },
        ],
    },
    {
        "name": "Photosynthesis",
        "god": God.MARDUK,
        "affinity_level": 2,
        "description": (
            "The process in which you use sunlight to create oxygen and energy to "
            "replenish your health gradually over time. Requires sunlight obviously. "
            "When casting this spell on an ally, they receive regeneration of 2 "
            "Health Points per turn for 1d6 turns."
        ),
        "enhancements": [],
    },
    {
        "name": "Scorched Earth",
        "god": God.MARDUK,
        "affinity_level": 2,
        "description": (
            "Scorch your surroundings completely to create an environment that "
            "greatly enhances fire attacks. Causes the Burn effect on everyone "
            "within a 6 squares radius area, whether they are enemies or allies, "
            "and anyone attempting to evade this attack suffers a -2 penalty to "
            "Evading."
        ),
        "enhancements": [
            {
                "name": "Earthquake",
                "cost_mp": 4,
                "affinity_required": None,
                "description": "The penalty increases to -5 instead of -2.",
            },
        ],
    },
    {
        "name": "Greater Photosynthesis",
        "god": God.MARDUK,
        "affinity_level": 3,
        "description": (
            "The process in which you use sunlight to create oxygen and energy to "
            "replenish your health gradually over time. Requires sunlight obviously. "
            "When casting this spell on an ally, they receive regeneration of 4 "
            "Health Points per turn for 6 turns."
        ),
        "enhancements": [
            {
                "name": "Magic Compost",
                "cost_mp": 0,
                "affinity_required": None,
                "description": (
                    "Using this on plants makes them grow to maturity instantly, "
                    "be they trees, bushes or any other type of plant."
                ),
            },
        ],
    },

    # ── Gro-goroth ────────────────────────────────────────────────────────────
    {
        "name": "Necromancy",
        "god": God.GORGOROTH,
        "affinity_level": 1,
        "description": (
            "Bring back life to where it once lingered. The bond between the body "
            "and the soul must still be relatively fresh for the necromancy to work. "
            "You can bring back to life an enemy that has a Threat Level equal to or "
            "less than 1/4 of your Tenacity value as your servant. If the same enemy "
            "dies again while under the effect of this spell, they cannot be "
            "resurrected by necromancy, and this spell does not work on playable "
            "characters. You can have a number of zombies equal to the sum of their "
            "levels equal to 1/4 of your Tenacity value. To order one of them to "
            "attack is a Simple Action."
        ),
        "enhancements": [
            {
                "name": "High Necromancy",
                "cost_mp": 8,
                "affinity_required": 3,
                "description": (
                    "Now you can bring back to life an enemy that has a Threat Level "
                    "equal to or less than 1/2 of your Tenacity value."
                ),
            },
        ],
    },
    {
        "name": "Hurting",
        "god": God.GORGOROTH,
        "affinity_level": 1,
        "description": (
            "Create a devastating vortex out of your concentrated feelings of hurting "
            "and hatred. You deal 1d8 + Tenacity value in physical damage (Blunt, "
            "Slashing or Piercing)."
        ),
        "enhancements": [
            {
                "name": "Hurting Much",
                "cost_mp": 4,
                "affinity_required": None,
                "description": "You can select 2 more enemies at once.",
            },
            {
                "name": "Hate and Hurt",
                "cost_mp": 8,
                "affinity_required": None,
                "description": "You add your Tenacity value twice.",
            },
        ],
    },
    {
        "name": "Blood Golem",
        "god": God.GORGOROTH,
        "affinity_level": 2,
        "description": (
            "Sacrifice blood to summon a golem that fights by your side temporarily. "
            "You create a Blood and Flesh Golem that obeys all your commands. "
            "Mechanically, it acts as a Combatant Ally, which you can command to "
            "attack using a Simple Action. It gains a bonus of 4 + your Tenacity "
            "to hit, and its punch deals 1d12 damage."
        ),
        "enhancements": [
            {
                "name": "Combat Golem",
                "cost_mp": 4,
                "affinity_required": None,
                "description": "The golem's attack bonus becomes 8 + your Tenacity.",
            },
            {
                "name": "Additional Members",
                "cost_mp": 4,
                "affinity_required": 3,
                "description": (
                    "Whenever you command it to attack using a Simple Action, "
                    "it makes two strikes."
                ),
            },
            {
                "name": "Armored",
                "cost_mp": 4,
                "affinity_required": 2,
                "description": "The golem requires 4 MARKs to be destroyed instead of 3.",
            },
            {
                "name": "Claws",
                "cost_mp": 4,
                "affinity_required": None,
                "description": "The golem's punch damage increases to 2d8 instead of 1d12.",
            },
        ],
    },
    {
        "name": "Black Smog",
        "god": God.GORGOROTH,
        "affinity_level": 2,
        "description": (
            "Crystallize manmade darkness born from the industrial age to blind and "
            "suffocate your opponents. You blind all enemies within a 3 squares "
            "radius and deal 1d4-2 (minimum 0) damage to the head. You roll only "
            "once to hit, not adding the Body Location penalty, and all enemies "
            "within the radius must roll Evading."
        ),
        "enhancements": [
            {
                "name": "Barbed Mist",
                "cost_mp": 4,
                "affinity_required": None,
                "description": "Damage changes from 1d4-2 to 1d4.",
            },
        ],
    },
    {
        "name": "Black Orb",
        "god": God.GORGOROTH,
        "affinity_level": 3,
        "description": (
            "A concentrated negative energy that can be hurled at your opponent "
            "multiple times. The orb maintains its form only temporarily before the "
            "ill will disperses. You make four attacks against a target; each attack "
            "must be made with its own hit roll and can aim at different body parts. "
            "Each attack that you hit deals 3d6 of magical damage."
        ),
        "enhancements": [
            {
                "name": "Dark Matter",
                "cost_mp": 4,
                "affinity_required": None,
                "description": (
                    "There is no penalty of the body parts when aiming with the "
                    "Black Orb."
                ),
            },
        ],
    },

    # ── Sulfur God ────────────────────────────────────────────────────────────
    {
        "name": "Longinus",
        "god": God.SULFUR,
        "affinity_level": 1,
        "description": (
            "The blood of Alll-mer boils and rages even ages after his death. Just "
            "a drop thrusts spears to the torso of his enemies. Summon a blood spear "
            "to wield in battle. You summon a spear that deals magical damage equal "
            "to 1d6. This spear lasts until the end of the scene and can be used "
            "with Conjuring (Tenacity) instead of Killing (Guts). Whenever you make "
            "an attack with the spear, you gain +1 Guts (up to a maximum of 4) and "
            "can throw the spear (in a distance equal to your Guts in squares) at an "
            "enemy to deal double damage dice (however, you lose your spear no matter "
            "if you hit or not)."
        ),
        "enhancements": [
            {
                "name": "Sharp Spear",
                "cost_mp": 0,
                "affinity_required": 2,
                "description": "You increase the spear's damage by 2d6 instead of 1d6.",
            },
            {
                "name": "Powerful Spear",
                "cost_mp": 0,
                "affinity_required": 3,
                "description": "You increase the spear's damage by 3d6 instead of 1d6.",
            },
        ],
    },
    {
        "name": "Sulfuric",
        "god": God.SULFUR,
        "affinity_level": 2,
        "description": (
            "You transport the sulfuric rivers of the great God of Sulfur to those "
            "who deserve it. Everyone within a 6 squares radius centered on a point "
            "of your choice, whether allies or enemies, must make an Evading "
            "(Resilience) test against your Conjuring test. On failure, everyone is "
            "inflicted with the Burn condition and takes 6d6 of magic damage. "
            "However, due to the pain and pandemonium caused by this magic, you "
            "apply the Critical State condition to yourself."
        ),
        "enhancements": [],
    },
    {
        "name": "Crown of Thorns",
        "god": God.SULFUR,
        "affinity_level": 3,
        "description": (
            "The crown of thorns makes your suffering pleasing to others in "
            "indescribable ways. You suffer from the Bleeding condition until the "
            "effect of the magic is ceased, and all allies within a 3 squares radius "
            "centered on you receive Health Points equal to the damage from the "
            "bleeding that you receive."
        ),
        "enhancements": [
            {
                "name": "Bleedmore",
                "cost_mp": 4,
                "affinity_required": None,
                "description": (
                    "You increase the damage you take from bleeding from this "
                    "spell by +1d4."
                ),
            },
            {
                "name": "Lethal Bleeding",
                "cost_mp": 4,
                "affinity_required": None,
                "description": (
                    "The bleeding die caused by this spell is now d10 instead of d4."
                ),
            },
        ],
    },

    # ── God of the Depths ─────────────────────────────────────────────────────
    {
        "name": "Mastery over Insects",
        "god": God.SULFUR,
        "affinity_level": 1,
        "description": (
            "Understanding of insects. You can hear and talk with insects of all "
            "sizes. You can ask 5 questions to the insects or even pacify them; the "
            "insects will answer the questions truthfully and can even serve as spies "
            "in certain occasions, being able to receive orders from you. After the "
            "insect completes its mission or follows your orders, the spell is ceased."
        ),
        "enhancements": [
            {
                "name": "Army of Bugs",
                "cost_mp": 8,
                "affinity_required": 3,
                "description": (
                    "You can order the insects to protect you or even to attack "
                    "other creatures, regardless of whether it costs their lives. "
                    "If you try to use this ability on an insect-type creature you "
                    "must make a Conjuring (Tenacity) roll against the creature's "
                    "Understanding (Tenacity) roll; you can only control creatures "
                    "with a difficulty level less than or equal to your Tenacity. "
                    "The bugs will protect you until you perform a Rest Scene, after "
                    "which they will become peaceful and leave."
                ),
            },
        ],
    },
    {
        "name": "Needle Worm",
        "god": God.SULFUR,
        "affinity_level": 1,
        "description": (
            "Harness the strength of a hundred leeches. The price is that you have "
            "to carry them inside you as parasites. You apply the Poisoned (1) and "
            "Bleeding conditions to the enemy, and all damage they take with these "
            "effects is converted into Health Points for you. However, when this "
            "spell ends, you will suffer from Withdrawal effects until you spend an "
            "action during a Rest Scene to vomit the leeches and lose 2 Hunger."
        ),
        "enhancements": [],
    },
    {
        "name": "Locust Swarm",
        "god": God.SULFUR,
        "affinity_level": 2,
        "description": (
            "Summon a swarm of crickets to disrupt the enemy. You inflict the "
            "confusion effect on the target."
        ),
        "enhancements": [
            {
                "name": "Worms of Crickets",
                "cost_mp": 4,
                "affinity_required": 3,
                "description": "You deal 1d6 damage per turn until the end of the scene.",
            },
        ],
    },
    {
        "name": "Flock of Crows",
        "god": God.SULFUR,
        "affinity_level": 2,
        "description": (
            "A swarm of crows fly to your enemy and attempt to tear them apart. You "
            "choose a body part and it is automatically attacked by the swarm; the "
            "hit is instantaneous and causes 1d4+1 damage."
        ),
        "enhancements": [
            {
                "name": "Mutant Swarm",
                "cost_mp": 8,
                "affinity_required": 3,
                "description": (
                    "You create 2 more mutant crow swarms; you can select different "
                    "enemies and different body parts to be attacked (including the "
                    "same enemy in the same body part). Each swarm deals 1d4+1 "
                    "damage, totaling 3d4+3."
                ),
            },
        ],
    },

    # ── New Gods ──────────────────────────────────────────────────────────────
    {
        "name": "Radiation",
        "god": God.NEW_GODS,
        "affinity_level": 1,
        "description": (
            "Makes a thunderous light shine in front of the enemies. You apply the "
            "Light Sensitive condition."
        ),
        "enhancements": [
            {
                "name": "Illuminate",
                "cost_mp": 0,
                "affinity_required": None,
                "description": "You can use this spell to illuminate an area with a 5 squares radius.",
            },
        ],
    },
    {
        "name": "Enchain",
        "god": God.NEW_GODS,
        "affinity_level": 1,
        "description": (
            "Chains jump from the ground and bind the enemy to you, giving an "
            "opportunity for your allies and enemies to make a stronger attack. "
            "You apply the condition Grappled to the target and to yourself."
        ),
        "enhancements": [
            {
                "name": "High Ground",
                "cost_mp": 4,
                "affinity_required": None,
                "description": (
                    "You can create chains that have a size in squares equal to your "
                    "Tenacity value, although a roll is required to scale the chains."
                ),
            },
            {
                "name": "Burden Chains",
                "cost_mp": 8,
                "affinity_required": 2,
                "description": "Apply Paralyzed instead of Grappled.",
            },
        ],
    },
    {
        "name": "Betel Enlightenment",
        "god": God.NEW_GODS,
        "affinity_level": 2,
        "description": (
            "The light of Betel enhances your magical nature. You reduce the cost "
            "of all enhanced effects by -2 until the end of the scene."
        ),
        "enhancements": [
            {
                "name": "Celestially Chosen",
                "cost_mp": 8,
                "affinity_required": None,
                "description": "The reduction increases to -4 instead of -2.",
            },
        ],
    },
    {
        "name": "Chains of Torment",
        "god": God.NEW_GODS,
        "affinity_level": 3,
        "description": (
            "Summon the chains that tormented Chambara the Tormented One for "
            "hundreds of years. You apply Critical State to your opponent, but if "
            "you hit the attack, you apply Terror to yourself until the end of "
            "the scene."
        ),
        "enhancements": [
            {
                "name": "Annihilation",
                "cost_mp": 0,
                "affinity_required": None,
                "description": "Reduce your opponent's health to 1 and your Mind value to 1.",
            },
        ],
    },
]


def seed() -> None:
    return None