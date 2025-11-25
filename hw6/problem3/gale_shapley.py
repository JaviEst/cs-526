from collections import deque
from collections.abc import Iterable

PreferenceList = dict[str, list[str]]
Matchings = dict[str, str]


def gale_shapley(men_preferences: PreferenceList, women_preferences: PreferenceList) -> Matchings:
    if len(men_preferences) != len(women_preferences):
        raise ValueError("Unequal number of men and women preferences supplied")

    men = list(men_preferences.keys())
    women = set(women_preferences.keys())

    for prefs in men_preferences.values():
        if set(prefs) != women:
            missing = women.difference(prefs)
            extra = set(prefs).difference(women)
            raise ValueError(
                "Men preference lists must list each woman exactly once;"
                f" missing={missing} extra={extra}"
            )

    for woman, prefs in women_preferences.items():
        if set(prefs) != set(men):
            missing = set(men).difference(prefs)
            extra = set(prefs).difference(men)
            raise ValueError(
                f"Preference list for woman '{woman}' must contain every man exactly once;"
                f" missing={missing} extra={extra}"
            )

    women_rankings = {
        woman: {man: rank for rank, man in enumerate(prefs)}
        for woman, prefs in women_preferences.items()
    }

    free_men: deque[str] = deque(men)
    proposal_index = {man: 0 for man in men}
    engagements: dict[str, str] = {}

    while free_men:
        man = free_men.popleft()
        prefs = men_preferences[man]
        if proposal_index[man] >= len(prefs):
            # Ran out of women to propose to; this indicates malformed data.
            raise ValueError(f"Man '{man}' has no remaining women to propose to")

        woman = prefs[proposal_index[man]]
        proposal_index[man] += 1
        current_partner = engagements.get(woman)

        if current_partner is None:
            engagements[woman] = man
            continue

        if women_rankings[woman][man] < women_rankings[woman][current_partner]:
            engagements[woman] = man
            free_men.append(current_partner)
        else:
            free_men.append(man)

    return {man: woman for woman, man in engagements.items()}


def parse_preferences(lines: Iterable[str]) -> tuple[PreferenceList, PreferenceList]:
    cleaned = [line.strip() for line in lines if line.strip()]
    if not cleaned:
        raise ValueError("Input file is empty")

    try:
        count = int(cleaned[0])
    except ValueError as exc:  # pragma: no cover - defensive
        raise ValueError("First line must specify participant count") from exc

    if count <= 0:
        raise ValueError("Participant count must be positive")

    expected_lines = 1 + 2 * count
    if len(cleaned) < expected_lines:
        raise ValueError(
            "Preference file ended early; expected "
            f"{expected_lines} non-empty lines but found {len(cleaned)}"
        )

    men_lines = cleaned[1 : count + 1]
    women_lines = cleaned[count + 1 : 1 + 2 * count]

    men_preferences: PreferenceList = {}
    women_preferences: PreferenceList = {}

    for line in men_lines:
        tokens = line.split()
        if len(tokens) != count + 1:
            raise ValueError(
                "Each man's preference row must list the man name followed by "
                f"{count} women"
            )
        man, *prefs = tokens
        men_preferences[man] = prefs

    for line in women_lines:
        tokens = line.split()
        if len(tokens) != count + 1:
            raise ValueError(
                "Each woman's preference row must list the woman name followed by "
                f"{count} men"
            )
        woman, *prefs = tokens
        women_preferences[woman] = prefs

    if len(men_preferences) != count or len(women_preferences) != count:
        raise ValueError("Preference lists contain duplicate participant names")

    return men_preferences, women_preferences


def is_stable(
    matches: Matchings,
    men_preferences: PreferenceList,
    women_preferences: PreferenceList,
) -> bool:
    women_partner = {woman: man for man, woman in matches.items()}
    women_rankings = {
        woman: {man: rank for rank, man in enumerate(prefs)}
        for woman, prefs in women_preferences.items()
    }

    for man, current_woman in matches.items():
        man_prefs = men_preferences[man]
        current_index = man_prefs.index(current_woman)
        preferred_women = man_prefs[:current_index]

        for woman in preferred_women:
            partner = women_partner.get(woman)
            if partner is None:
                return False
            if women_rankings[woman][man] < women_rankings[woman][partner]:
                return False

    return True
