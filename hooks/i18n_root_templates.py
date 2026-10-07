"""Keep the root search.html and 404.html in the default language.

mkdocs-static-i18n builds the default language first and then rebuilds the whole site once per
alternate language into the same site_dir. The readthedocs theme writes search.html and 404.html to
the site root on every one of those builds, so the language built last (French) overwrote the
English pages that every language links to. Dropping them from the alternate builds leaves the
default language's copies in place.
"""

ROOT_TEMPLATES = {"search.html", "404.html"}


def on_config(config):
    i18n = config.plugins.get("i18n")
    if i18n is None:
        return config
    current = getattr(i18n, "current_language", None)
    default = getattr(i18n, "default_language", None)
    if current and default and current != default:
        config.theme.static_templates.difference_update(ROOT_TEMPLATES)
    return config
