# Benchmarker

### macro trainer | build optimizer | practice tool

Benchmarker is a Starcraft 2 training mod that can be used with any current ladder map. This tool aims to help players of all levels refine and improve their macro mechanics while at the same time practicing the builds they will need to slay all the nerds and steal their ladder points.

### Features

Reset builds on the fly without having to remake a custom game.

Track personal supply benchmarks by matchup in-game
- Set supply benchmarks at 6, 8, and 10 minutes
- Configure builds to end at either maximum supply or a specific game time
- Benchmarks are automatically saved for future practice sessions
- Benchmarks are tracked separately for each match-up so you can switch between builds quickly and easily

Practice against "benchmark" build orders to refine and optimize your play
- Save your best build orders (per matchup) at the end of each build
- Track your play against a set of "benchmark" build order objectives for real-time feedback
- See real-time “hints” for upcoming build order steps in game
- Display performance feedback of how well you are executing in real time

Display customizable alerts designed to help players get into the rhythm of macroing correctly.  
- Alert when your minerals or gas becomes too high
- Alert when you are about to be supply blocked
- Alert when your race’s macro-mechanic energy gets too high
- Alert when you are forgetting upgrades for too long
- Alert when worker or army production is idle for too long
- Alert when your APM goes below a certain threshold for too long
- Alert when your army has been sitting idle on the map for too long

Provide performance reports after each build to help you create and refine the perfect build order
- Reports on supply benchmark performance
- Reports number of workers created
- Reports amount of time supply blocked
- Reports amount of time production is idle
- Reports total army size/value/supply
- Reports build order steps from current build
- Reports Spending Quotient (SQ) from Do you macro like a pro? (unimplemented)
- Reports average unspent minerals (unimplemented)
- Reports average unspent gas (unimplemented)

In-Game Stats to track your progress in real time
- Provide performance reports after each build to help you create and refine the perfect build order

A [WIN] button... because who doesn’t want a win button?

Supports chat commands and hotkeys for accessing menus in game

### How To Play

**For first time players:**

- Start by selecting a matchup to practice.
- Then select your supply benchmarks for 6:00, 8:00, and 10:00 minutes.
- Select the build completion objective (currently max supply or specified game time).
- Select the final build benchmark time or supply.
- (optional) Select whether to practice against the previous benchmark build order.
- Start your build.

Once you have completed a build you can elect to save it or start over.  If you save your build it becomes available to practice against for that matchup next time you play that matchup.

Build Order steps are marked complete when the correct build-order-eligible unit or upgrade is made.  They are marked failed when the incorrect build-order-eligible unit or upgrade is made

### Recommended Practice Technique

This tool is designed around the idea of perfecting one standard “macro” build for each matchup.  It is intended to help you with learning that build order, improving your macro mechanics, and refining your timings all as part of a single practice session.  For most players below Master League this single build approach is commonly recommended as a great way to improve both on mechanics and understanding basic timings.  So at least until multiple benchmark builds are added (and they almost certainly will be at some point), here are some of my recommended practice techniques:

##### Standard Macro Practice

1. Pick a matchup.
2. Think about what you consider your strongest “standard” macro build in that matchup.
3. Play through that build a couple of times until you’re warmed up.
4. Once you have a build run-through that you are happy with, save it as a benchmark build.
5. For the next 10 - 30 minutes, attempt to refine that build by pushing yourself to exceed the supply benchmarks, and to shave off time from build step timings.
6. Each time you execute the build more cleanly than the current benchmark save that new build as the benchmark to beat.
7. After your chosen time is up or when you are satisfied with your current performance, move on to your next matchup and repeat steps 2 - 6 until done with each matchup.
8. Go on the ladder and collect your wins.

##### Learning A New Build

1. Pick a build.
2. Select the appropriate matchup for the build.
3. Uncheck practice against build order (if checked), or clear the existing build if desired.
4. Play through the new build slowly at first.  It is more important to get the build steps in the right order than to focus on execution or hitting timings the first time through.
5. When the correct build order has been achieved (which you can check on the post-build report), save this build as the new benchmark.
6. Practice against the newly saved benchmark build a couple of times, each time trying to shave a few seconds off the timings, squeezing a few more workers out, or use your resources more efficiently etc…
7. Feel free to also use the [FORK] option to allow for diverging from the new build to add your own style and variations.
8. Proceed to ladder.
9. Slay nerds.

*Note* - Whenever you are able to exceed one or more of the supply benchmarks during a build, don’t forget update the supply benchmarks to reflect the new record.  From there you can tweak them by hand if desired.

More advanced players should ideally be comfortable cycling through different benchmark builds for a matchup since they are already familiar with them.  If a large number of users start to ask for multiple different named benchmark builds it could be implemented before the 1.0 release.

### Useful Tips

- *You can stack build order units* if you make 2 of the same unit type within 15 seconds of each other. If the unit type is valid for tracking in build orders, it will be considered 2x of the same step rather than two independent steps.  This also applies to any number of the same build order unit type within 15 seconds of each other.
- *You can update supply benchmarks automatically* from the post-build report.  This option is available upon finishing a build and lets you automatically save the first three supply benchmarks as the actual supply values from the current build.
- *You can fork a build* by clicking the [FORK] button while practicing against a build order.  This feature lets you use the same first steps as the benchmark build, but upon forking will track the rest of the build as a new build without evaluating objectives.  This can be very useful for experimentation.
- *You can correct a failed step* by performing the correct build step immediately after the failed step.  This allows you to avoid a cascade failure of steps based on a single mistake.  There are some known issues with this functionality and multiple units though
- *Supply producing units are tracked until 40 supply* to help players be more precise with their opening timings.  An option may be added in the future to be able to toggle and configure this behavior.
- *Gas structures are only tracked until 60 supply* to prevent the build order from becoming cluttered later on by structures that are not core to the build order.  This could however be changed to only track up to 6 structures rather than limiting based on supply if the community desires.
