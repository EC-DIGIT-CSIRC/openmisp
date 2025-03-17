from openmisp.models.taxonomies.misp import MispTaxonomy, MispTaxonomyConfidenceLevelEntry, MispTaxonomyPredicate
from openmisp.models.taxonomies.tlp import TlpTaxonomy, TlpTaxonomyPredicate
from openmisp.models.taxonomies.utils import (
    build_tag,
    get_all_taxonomies,
    get_predicate_entries,
    get_taxonomy_by_namespace,
    get_taxonomy_from_tag,
    is_valid_tag,
    parse_tag,
)


def main():
    """Main function."""
    print("Example 1: Using a simple taxonomy (TLP)")
    print(f"TLP namespace: {TlpTaxonomy.namespace}")
    print(f"TLP description: {TlpTaxonomy.description[:100]}...")
    print(f"TLP predicates: {[p.value for p in TlpTaxonomyPredicate]}")
    print(f"TLP tag example: {TlpTaxonomy.get_tag(TlpTaxonomyPredicate.RED)}")
    print()

    print("Example 2: Using a complex taxonomy with entries (MISP)")
    print(f"MISP namespace: {MispTaxonomy.namespace}")
    print(f"MISP description: {MispTaxonomy.description[:100] if MispTaxonomy.description else 'No description'}")

    confidence_entries = [entry.value for entry in MispTaxonomyConfidenceLevelEntry]
    print(f"MISP confidence-level entries (direct): {confidence_entries}")

    confidence_entries_util = get_predicate_entries(MispTaxonomy, "confidence-level")
    print(f"MISP confidence-level entries (utility): {confidence_entries_util}")

    confidence_tag = build_tag("misp", "confidence-level", "completely-confident")
    print(f"MISP confidence tag example: {confidence_tag}")

    confidence_tag2 = MispTaxonomy.get_tag(
        MispTaxonomyPredicate.CONFIDENCE_LEVEL, MispTaxonomyConfidenceLevelEntry.COMPLETELY_CONFIDENT
    )
    print(f"MISP confidence tag example (using class): {confidence_tag2}")
    print()

    print("Example 3: Getting all taxonomies")
    taxonomies = get_all_taxonomies()
    print(f"Number of taxonomies: {len(taxonomies)}")
    print(f"First 5 taxonomies: {[t.__name__ for t in taxonomies[:5]]}")
    print()

    print("Example 4: Getting a taxonomy by namespace")
    tlp_taxonomy = get_taxonomy_by_namespace("tlp")
    print(f"Found taxonomy: {tlp_taxonomy.__name__}")
    print()

    print("Example 5: Getting a taxonomy from a tag")
    tag = "tlp:red"
    taxonomy = get_taxonomy_from_tag(tag)
    print(f"Tag: {tag}")
    print(f"Found taxonomy: {taxonomy.__name__}")
    print()

    print("Example 6: Validating tags")
    valid_tag1 = "tlp:red"
    valid_tag2 = "misp:confidence-level='completely-confident'"
    invalid_tag1 = "tlp:invalid"
    invalid_tag2 = "misp:confidence-level='invalid'"
    print(f"Is '{valid_tag1}' valid? {is_valid_tag(valid_tag1)}")
    print(f"Is '{valid_tag2}' valid? {is_valid_tag(valid_tag2)}")
    print(f"Is '{invalid_tag1}' valid? {is_valid_tag(invalid_tag1)}")
    print(f"Is '{invalid_tag2}' valid? {is_valid_tag(invalid_tag2)}")
    print()

    print("Example 7: Parsing tags")
    simple_tag = "tlp:red"
    complex_tag = "misp:confidence-level='completely-confident'"
    print(f"Simple tag: {simple_tag}")
    print(f"Parsed: {parse_tag(simple_tag)}")
    print(f"Complex tag: {complex_tag}")
    print(f"Parsed: {parse_tag(complex_tag)}")


if __name__ == "__main__":
    main()
