# Developer Notes
## Unique Variant Slots
- Unique: Carpets, Glass Panes, Fence Gates, Sheets, Posts, Chutes, Concrete Sheet, Thatch Roof
- Unique2: Banisters, Concrete Quarter, Hedge, Hollow Logs, decorative_blocks:stone_pillar, (Stripped)Beams
- Unique3: Boardwalks, Concrete Chunk, Palisades
- Unique4: Supports
## Mod Overlap Protocol
- Make sure this isn't a use-case for Almost Unified
- Choose a mod/block to take priority
- Tag any disabled alternatives as #strangejourney:mod_overlap
- Scripts will take care of disabling crafting of alternatives
## Loot Options
What makes a good loot item to populate shops and loot tables is that it's 1) a commodity that you always want and that hording feels good 2) not a farmable resource 3) not something the player has to work hard for 4) not something the player will eventually have far too much of (1 can be ignored if it's been made exclusively obtainable through said loot methods, like Plushies will be through gacha rolls)
### Examples of Bad Loot
- EnderIO's old capacitors are all unique (not commodities) which CAN work as a reward, but hoarding them feels awful (rarely useful) which violates 1.
- Things like Berries and Apricorns from Cobblemon are farmable, once you have one you can easily get more, thus violating 2. Giving one could jumpstart the player, and they'd never want it as a reward again (because they can now farm it) or even worse act as a way for them to just buy it en masse without setting up a farm (directly removing gameplay)
- You'd think 3 would be easy to not mess up, but I've seen a million modpacks give out stuff like late game weapons and nether stars as randomized quest rewards. What the hell were they thinking?
- Diamonds are the quintessential example of something that violates 4. Early game diamonds are hard to come by and extremely valuable (violating 3, cheapening how good it feels to find your first) but extremely abundant as the game progresses, even without automation methods.
### Examples of Good Loot (That Will Likely be Utilized)
- Cobblemon: CobGyms keys, Relic Coins, XP Candy
- Gacha Rolls for Collectibles: Plushies, Hats, IE Shader Grab-Bags, Trading Card Booster Packs
- Emeralds (Vanilla MC's own "Currency," you're directly incentivized to horde it and doing so feels pretty good)
- Explorer Maps to various structures w/o another way of locating them
## Loot Addendum: Paraglider Heart Containers and Stamina
Paraglider's player upgrades are special in that they directly violate 1 by being turned into NOT a commodity. In essence, though they're all technically the same item, each Heart Container is given once for a specific event (the first time killing a boss). Stamina vessels are unimplemented, but they'll likely be given out for visiting important structures, biomes, and dimensions (an exploration reward).