from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTICE_FILES = (
    ROOT / "docs" / "_home_notice.md",
    ROOT / "docs_init" / "_home_notice.md",
    ROOT / "docs" / "README.md",
    ROOT / "docs_init" / "README.md",
)


def test_home_notice_contains_stats_and_tutorial_entry():
    for path in NOTICE_FILES:
        content = path.read_text(encoding="utf-8")
        assert "公告与更新" in content, path
        assert 'class="dpr-home-notice-tutorial"' in content, path
        assert "data-dpr-site-stats" in content, path
        assert "data-dpr-daily-readers" in content, path
        assert "data-dpr-fork-count" in content, path
        assert "今天有" in content and "人在看论文" in content, path
        assert "人加入 Daily Paper Reader" in content, path


def test_site_stats_script_is_loaded_without_blocking_core_assets():
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    assert "app/site-stats.js" in html
    assert "[DPR] 首页统计加载失败" in html


def test_home_stats_css_has_desktop_and_mobile_layouts():
    css = (ROOT / "app" / "app.css").read_text(encoding="utf-8")
    assert ".dpr-home-notice-header" in css
    assert ".dpr-home-site-stats" in css
    assert ".dpr-home-site-stat-value" in css
    assert "font-variant-numeric: tabular-nums" in css
    assert "@media (max-width: 600px)" in css


def test_supabase_site_reader_stats_sql_is_least_privilege():
    sql = (ROOT / "sql" / "create_site_reader_stats_schema.sql").read_text(encoding="utf-8").lower()

    assert "create table if not exists public.site_daily_reader_events" in sql
    assert "create table if not exists public.site_daily_reader_counts" in sql
    assert "alter table public.site_daily_reader_events enable row level security" in sql
    assert "alter table public.site_daily_reader_counts enable row level security" in sql
    assert "create schema if not exists private" in sql
    assert "create or replace function private.increment_site_daily_reader_count" in sql
    assert "security definer" in sql
    assert "set search_path = ''" in sql
    assert "grant insert on public.site_daily_reader_events to anon, authenticated" in sql
    assert "grant select on public.site_daily_reader_counts to anon, authenticated" in sql
    assert "for insert" in sql and "with check" in sql
    assert "asia/shanghai" in sql
    assert "visitor_hash ~ '^[a-f0-9]{64}$'" in sql
    assert "grant select on public.site_daily_reader_events to anon" not in sql
