#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import random
import re
from pathlib import Path


_HEX_RE = re.compile(r"^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$")

DEFAULT_PURPLE_SCALE = [
    "#FAF8FF",  # 0
    "#F0EBFF",  # 1
    "#DDD5FF",  # 2
    "#C6B5FF",  # 3
    "#A78BFA",  # 4
    "#8B5CF6",  # 5
    "#7C3AED",  # 6
    "#6D28D9",  # 7
    "#5B21B6",  # 8
    "#4C1D95",  # 9
]

CANDIDATE_FIELDS = [
    "渠道名称",
    "渠道编码",
    "渠道类型",
    "状态",
    "负责人",
    "更新时间",
    "Tags",
    "Action",
]

STATUS_VALUES = ["启用", "停用", "草稿", "审核中"]
OWNERS = ["张敏", "李航", "周琳", "王宇", "陈澄"]
CHANNEL_TYPES = ["直营", "代理", "平台", "联营"]
TAG_SETS = [
    ["nice", "developer"],
    ["loser"],
    ["cool", "teacher"],
    ["expert", "reviewer"],
]


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate an Ant-style query/list admin page in pure HTML/CSS with semantic table markup."
    )
    parser.add_argument("--out", required=True, help="Output HTML path")
    parser.add_argument("--primary", default=None, help="Primary color hex (default: palette[6])")
    parser.add_argument("--palette", default=None, help="Comma-separated 10-step purple scale")
    parser.add_argument("--brand", default="Company", help="Brand label in page meta")
    parser.add_argument("--title", default="Ant-style Admin Page", help="HTML <title>")
    parser.add_argument("--page-title", default="后台管理", help="Page heading title")
    parser.add_argument("--fields", default=None, help="Comma-separated list fields. If set, use exactly as provided.")
    parser.add_argument("--rows", type=int, default=10, help="Mock row count")
    parser.add_argument("--include-error-state", action="store_true", help="Render first query control in error style.")
    parser.add_argument("--show-list-header", action="store_true", help="Show list title/count header above table.")
    parser.add_argument("--show-vertical-lines", action="store_true", help="Show vertical divider lines between columns.")
    return parser.parse_args()


def _validate_hex(color: str) -> str:
    color = color.strip()
    if not _HEX_RE.match(color):
        raise SystemExit(f"Invalid hex color: {color!r}")
    if len(color) == 4:
        color = "#" + "".join(ch * 2 for ch in color[1:])
    return color.upper()


def _validate_palette(palette: list[str]) -> list[str]:
    if len(palette) != 10:
        raise SystemExit(f"--palette must have exactly 10 colors, got {len(palette)}")
    return [_validate_hex(c) for c in palette]


def _read_template() -> str:
    return (Path(__file__).resolve().parent.parent / "assets" / "admin-states-template.html").read_text(encoding="utf-8")


def _hex_to_rgb(color: str) -> tuple[int, int, int]:
    color = color.lstrip("#")
    return int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)


def _pick_fields(raw_fields: str | None) -> list[str]:
    if raw_fields:
        values = [v.strip() for v in raw_fields.split(",") if v.strip()]
        if not values:
            raise SystemExit("--fields provided but empty")
        return values
    pool = list(CANDIDATE_FIELDS)
    random.shuffle(pool)
    return pool[:5]


def _is_select_field(field: str) -> bool:
    return any(k in field for k in ("状态", "类型", "等级"))


def _is_name_field(field: str) -> bool:
    lower = field.lower()
    return ("name" in lower) or ("名称" in field)


def _is_tags_field(field: str) -> bool:
    lower = field.lower()
    return ("tags" in lower) or ("标签" in field)


def _is_action_field(field: str) -> bool:
    lower = field.lower()
    return ("action" in lower) or ("操作" in field)


def _mock_text(field: str, row_index: int) -> str:
    idx = row_index + 1
    if _is_name_field(field):
        return ["John Brown", "Jim Green", "Joe Black", "Lily Zhang", "Amy Wang"][row_index % 5]
    if "编码" in field or "code" in field.lower():
        return f"CH{idx:04d}"
    if "年龄" in field or "age" in field.lower():
        return str([32, 42, 29, 35, 38][row_index % 5])
    if "地址" in field or "address" in field.lower():
        return [
            "New York No. 1 Lake Park",
            "London No. 1 Lake Park",
            "Sidney No. 1 Lake Park",
            "Tokyo No. 2 Lake Park",
            "Shanghai No. 3 Lake Park",
        ][row_index % 5]
    if "类型" in field:
        return CHANNEL_TYPES[row_index % len(CHANNEL_TYPES)]
    if "状态" in field:
        return STATUS_VALUES[row_index % len(STATUS_VALUES)]
    if "负责人" in field:
        return OWNERS[row_index % len(OWNERS)]
    if "更新时间" in field:
        return f"2026-04-{(idx % 28) + 1:02d}"
    if "创建时间" in field:
        return f"2026-03-{(idx % 28) + 1:02d}"
    return f"{field}{idx}"


def _build_rows(fields: list[str], rows: int) -> list[dict[str, object]]:
    out: list[dict[str, object]] = []
    for row_index in range(rows):
        row: dict[str, object] = {}
        for field in fields:
            if _is_tags_field(field):
                row[field] = list(TAG_SETS[row_index % len(TAG_SETS)])
            elif _is_action_field(field):
                row[field] = ""
            else:
                row[field] = _mock_text(field, row_index)
        out.append(row)
    return out


def _resolve_name_field(fields: list[str]) -> str | None:
    for field in fields:
        if _is_name_field(field):
            return field
    return None


def _render_tags(tags: list[str]) -> str:
    items: list[str] = []
    for tag in tags:
        color = "ant-tag-geekblue" if len(tag) > 5 else "ant-tag-green"
        if tag == "loser":
            color = "ant-tag-volcano"
        items.append(f'<span class="ant-tag {color}">{html.escape(tag.upper())}</span>')
    return '<span class="cell-tags">' + "".join(items) + "</span>"


def _render_action(name: str) -> str:
    safe_name = html.escape(name)
    return (
        '<span class="cell-actions">'
        f'<a class="ant-link">Invite {safe_name}</a>'
        '<span class="ant-divider-vertical"></span>'
        '<a class="ant-link">Delete</a>'
        '</span>'
    )


def _render_name(value: str) -> str:
    return f'<a class="ant-link">{html.escape(value)}</a>'


def _build_query_fields(fields: list[str], include_error: bool) -> str:
    controls: list[str] = []
    for i, field in enumerate(fields[:4]):
        safe_field = html.escape(field)
        error_class = " is-error" if include_error and i == 0 else ""
        error_tip = '<div class="error-tip">该字段为必填项</div>' if include_error and i == 0 else ""

        if _is_select_field(field):
            control = (
                '<select class="ant-select{error}">'
                '<option value="">请选择</option>'
                '<option>选项A</option>'
                '<option>选项B</option>'
                '</select>'
            ).format(error=error_class)
        else:
            control = f'<input class="ant-input{error_class}" placeholder="请输入" />'

        controls.append(
            '<div class="field">'
            f'<div class="field-label">{safe_field}</div>'
            f"{control}"
            f"{error_tip}"
            '</div>'
        )
    return "".join(controls)


def _build_table_head_cells(fields: list[str]) -> str:
    return "".join(f"<th>{html.escape(field)}</th>" for field in fields)


def _build_table_body_rows(fields: list[str], rows_data: list[dict[str, object]]) -> str:
    name_field = _resolve_name_field(fields)
    rows: list[str] = []

    for row_index, row in enumerate(rows_data):
        cells: list[str] = []
        for field in fields:
            if _is_tags_field(field):
                tags = row.get(field, [])
                if not isinstance(tags, list):
                    tags = []
                cell_content = _render_tags([str(tag) for tag in tags])
            elif _is_action_field(field):
                if name_field:
                    name_value = str(row.get(name_field, "Record"))
                else:
                    name_value = f"Record {row_index + 1}"
                cell_content = _render_action(name_value)
            else:
                value = str(row.get(field, ""))
                if _is_name_field(field):
                    cell_content = _render_name(value)
                else:
                    cell_content = f'<span class="cell-text">{html.escape(value)}</span>'
            cells.append(f"<td>{cell_content}</td>")
        rows.append("<tr>" + "".join(cells) + "</tr>")
    return "".join(rows)


def _build_list_header(rows: int, show_list_header: bool) -> str:
    if not show_list_header:
        return ""
    return (
        '<div class="list-head">'
        '<h2>列表结果</h2>'
        f'<span class="count">{rows} 条</span>'
        '</div>'
    )


def _render(
    template: str,
    *,
    title: str,
    page_title: str,
    brand: str,
    primary: str,
    palette: list[str],
    query_fields_html: str,
    table_head_cells: str,
    table_body_rows: str,
    rows: int,
    show_list_header: bool,
    show_vertical_lines: bool,
) -> str:
    r, g, b = _hex_to_rgb(primary)
    rendered = (
        template.replace("{{TITLE}}", html.escape(title))
        .replace("{{PAGE_TITLE}}", html.escape(page_title))
        .replace("{{BRAND}}", html.escape(brand))
        .replace("{{PRIMARY}}", primary)
        .replace("{{PRIMARY_RGB}}", f"{r}, {g}, {b}")
        .replace("{{QUERY_FIELDS}}", query_fields_html)
        .replace("{{TABLE_HEAD_CELLS}}", table_head_cells)
        .replace("{{TABLE_BODY_ROWS}}", table_body_rows)
        .replace("{{ROWS}}", str(rows))
        .replace("{{LIST_HEADER}}", _build_list_header(rows, show_list_header))
        .replace("{{VERTICAL_CLASS}}", "with-vertical-lines" if show_vertical_lines else "")
    )
    for i, color in enumerate(palette):
        rendered = rendered.replace(f"{{{{PURPLE_{i}}}}}", color)
    return rendered


def main() -> None:
    args = _parse_args()
    if args.rows < 1:
        raise SystemExit("--rows must be >= 1")

    out_path = Path(args.out).expanduser().resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if args.palette:
        palette_raw = [v.strip() for v in args.palette.split(",") if v.strip()]
        palette = _validate_palette(palette_raw)
    else:
        palette = _validate_palette(list(DEFAULT_PURPLE_SCALE))

    primary = _validate_hex(args.primary) if args.primary else palette[6]
    fields = _pick_fields(args.fields)
    rows_data = _build_rows(fields, args.rows)

    query_fields_html = _build_query_fields(fields, args.include_error_state)
    table_head_cells = _build_table_head_cells(fields)
    table_body_rows = _build_table_body_rows(fields, rows_data)

    html_text = _render(
        _read_template(),
        title=args.title,
        page_title=args.page_title,
        brand=args.brand.strip() or "Company",
        primary=primary,
        palette=palette,
        query_fields_html=query_fields_html,
        table_head_cells=table_head_cells,
        table_body_rows=table_body_rows,
        rows=args.rows,
        show_list_header=args.show_list_header,
        show_vertical_lines=args.show_vertical_lines,
    )

    out_path.write_text(html_text, encoding="utf-8")
    print(str(out_path))


if __name__ == "__main__":
    main()
