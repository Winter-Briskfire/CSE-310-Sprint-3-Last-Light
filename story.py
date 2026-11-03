"""Story content for Last Light: Eridani.

Keeping story data separate from the game loop makes branches easy to find,
edit, and expand.
"""


def fx(**changes):
    return changes


SCENES = {
    "opening": (
        "LAST LIGHT",
        "The Eridani system is going dark. The colony world Aurelia has stopped answering, its orbital defense net is firing at empty space, and an unidentified fleet has crossed the outer moons. Your unit receives one final order: hold the line long enough for the last transports to escape.",
        [
            ("Pathfinder - scout the red valleys for survivors.", "verdant", fx(flag="ally")),
            ("Ranger - report to Kestrel Command under fire.", "station", fx(resolve=1)),
            ("Pilot - fly through the orbital debris field.", "nebula", fx(flag="route")),
            ("Signals Officer - recover the buried defense codes.", "archive", fx(clues=1)),
        ],
    ),
    "verdant": (
        "AURELIA'S RED VALLEYS",
        "Dust storms roll across the colony's farming belt. A civilian convoy is pinned between collapsed habitats while an automated distress beacon repeats an old military call sign.",
        [
            ("Guide the convoy through the canyon.", "approach", fx(flag="ally", clues=1, trust=1)),
            ("Reach the beacon and recover its power cell.", "approach", fx(flag="device", health=-1, clues=1)),
            ("Climb the ridge and mark the enemy advance.", "approach", fx(flag="route", resolve=1)),
        ],
    ),
    "station": (
        "KESTREL COMMAND",
        "The colony's defense headquarters is burning one tower at a time. A tired operations chief offers you a clearance chip while dropships lift off without enough fuel for everyone.",
        [
            ("Take command of the last evacuation channel.", "approach", fx(flag="route", clues=1, resolve=1)),
            ("Move through the maintenance tunnels.", "approach", fx(flag="stealth", health=-1)),
            ("Stay behind and help the operations chief.", "approach", fx(flag="ally", trust=1)),
        ],
    ),
    "nebula": (
        "THE ORBITAL DEBRIS FIELD",
        "Wreckage from the defense net fills the dark between Aurelia and its moon. A damaged gunship transmits coordinates for a hidden carrier, then goes silent.",
        [
            ("Dock with the gunship and retrieve its nav core.", "approach", fx(flag="device", clues=1)),
            ("Answer the unknown carrier's challenge.", "approach", fx(flag="password", clues=2, trust=1)),
            ("Plot a low-signature route through the wreckage.", "approach", fx(flag="route", resolve=1, stability=1)),
        ],
    ),
    "archive": (
        "FORT RAVELIN ARCHIVE",
        "Beneath a mountain fortress, the colony's first defense command is still powered. Its newest file predicts the invasion, but the file is encrypted with a commander's voiceprint.",
        [
            ("Decode the invasion forecast.", "approach", fx(flag="password", clues=2)),
            ("Align the fortress's old sensor array.", "approach", fx(flag="device", stability=1)),
            ("Search the armory for an override key.", "approach", fx(flag="override", health=-1, resolve=1)),
        ],
    ),
    "approach": (
        "THE EVACUATION LINE",
        "A civilian transport is trapped at the last jump corridor. Enemy ships are closing, but the transport carries a tactical fragment that could expose a gap in the invasion fleet.",
        [
            ("Stay and escort the transport.", "research", fx(trust=2, resolve=1)),
            ("Transmit the jump solution and continue.", "research", fx(clues=1, stability=1)),
            ("Take the tactical fragment and leave.", "research", fx(flag="device", trust=-1, clues=1)),
        ],
    ),
    "research": (
        "THE GHOST CARRIER",
        "The hidden carrier is still broadcasting orders from a crew that died hours ago. Their final message says the enemy is learning from every rescue, every lie, and every sacrifice made on Aurelia.",
        [
            ("Decode the final command from a distance.", "understation", fx(clues=2, stability=1, flag="failsafe")),
            ("Board the carrier and retrieve its combat core.", "understation", fx(flag="device", health=-1, clues=1)),
            ("Destroy the carrier before the signal spreads.", "understation", fx(trust=-1, stability=-1)),
        ],
    ),
    "understation": (
        "THE FALLEN BATTERY",
        "A buried defense battery is the only weapon still facing orbit. Its crew is trapped below ground, and a small resistance unit needs your help before the battery's reactor overloads.",
        [
            ("Rescue the crew and hold the battery.", "core", fx(trust=2, health=-1, flag="ally")),
            ("Route power through the old targeting system.", "core", fx(clues=1, stability=1)),
            ("Slip into the command bunker unseen.", "core", fx(flag="stealth", resolve=1)),
        ],
    ),
    "core": (
        "THE LAST DEFENSE GRID",
        "Above Aurelia, the defense grid unfolds like a burning crown. Fleet Commander Veyr offers one final bargain: surrender the grid and the transports live, or fire it and turn the whole system into a graveyard.",
        [
            ("Use your best discovered advantage.", "advantage", fx()),
            ("Fire the defense grid at the invasion fleet.", "free", fx()),
            ("Give the grid complete control.", "perfect", fx()),
            ("Shut down the grid and evacuate in the dark.", "quiet", fx()),
        ],
    ),
}


ENDINGS = {
    "advantage": ("THE LAST SIGNAL", "Your recovered codes expose a weakness in the invasion fleet. The defense grid fires only where it must, opening a corridor for the transports and leaving Aurelia a chance to rebuild."),
    "free": ("HOLD THE LINE", "You refuse Veyr's bargain and fire the grid. The transports escape through the opening you create, while your unit stays behind to make sure the enemy never reaches the colony."),
    "perfect": ("THE IRON SHIELD", "You give the grid complete control. No ship crosses the system without permission, and Aurelia is safe for the first time in years. Every survivor wonders what freedom will cost next."),
    "quiet": ("THE LONG NIGHT", "You shut down the defense grid rather than turn Aurelia into a weapon. The transports escape in the dark, and the colony survives with no army left to protect it."),
}


OUTCOMES = {
    "opening": [
        "Your Pathfinder assignment sends you toward the civilian routes in Aurelia's red valleys.",
        "Your Ranger orders put you on the ground at Kestrel Command before the defense network collapses.",
        "Your Pilot clearance gives you one dangerous flight through the debris around Aurelia.",
        "Your Signals Officer credentials unlock a route to Fort Ravelin's buried command archive.",
    ],
    "verdant": [
        "The rescued convoy joins your unit and brings a working terrain map.",
        "The recovered power cell gives your squad enough energy to reach the evacuation line.",
        "Your ridge report reveals where the invasion force will land next.",
    ],
    "station": [
        "The evacuation channel answers, giving you a transport window and a route through the fire.",
        "The maintenance tunnels put you behind the command lockdown, but your armor is damaged.",
        "The operations chief stays at the console and sends a trusted escort with you.",
    ],
    "nebula": [
        "The gunship's nav core identifies a hidden carrier beyond the wreckage.",
        "The carrier's challenge contains an old defense phrase and a set of matching coordinates.",
        "Your low-signature route brings you to the evacuation corridor without alerting the fleet.",
    ],
    "archive": [
        "The forecast confirms that the invasion fleet is using Aurelia's own defense codes.",
        "The sensor array tracks the fleet's command ship through the planet's storms.",
        "The override key opens a sealed weapons route, though the security system injures you.",
    ],
    "approach": [
        "The survivors reach the jump corridor and promise to carry your warning to the transports ahead.",
        "Your repair signal buys the trapped transport time and returns a tactical fragment to your unit.",
        "You leave with the fragment, but the stranded civilians report your position to the enemy.",
    ],
    "research": [
        "The decoded message gives you a safe approach to the ghost carrier and a way to interrupt its broadcast.",
        "The combat core contains a route into the carrier, but radiation leaves you wounded.",
        "The carrier goes silent, removing the immediate threat but destroying evidence your unit needed.",
    ],
    "understation": [
        "The battery crew joins your defense and helps prepare the last firing sequence.",
        "The targeting system comes online and gives you a clean shot at the invasion fleet.",
        "You reach the command bunker unseen, with the defense grid still waiting for an order.",
    ],
}

