# LAYER 1

parsing_document_start = {
    "layer": 1,
    "task_name": "Parsing provided document",
    "sub_task_name": None,
    "status": "processing",
    "message": "Started parsing the provided document",
    "data": None
}

parsing_document_end = {
    "layer": 1,
    "task_name": "Parsing provided document",
    "sub_task_name": None,
    "status": "finished",
    "message": "Parsing completed successfully",
    "data": {}
}

scrape_home_start = {
    "layer": 1,
    "task_name": "Scraping Home page",
    "sub_task_name": None,
    "status": "processing",
    "message": "Started scraping journal homepage",
    "data": None
}

scrape_home_end = {
    "layer": 1,
    "task_name": "Scraping Home page",
    "sub_task_name": None,
    "status": "finished",
    "message": "Journal homepage scraped successfully",
    "data": {
        "CURRENT_PAGE_LINK": "...",
        "Journal Title": "...",
        "Volume": "...",
        "Issue": "...",
        "Date": "...",
        "Articles": [...],
        "CoverPageLink": "..."
    }
}

validate_coverpage = {
    "layer": 1,
    "task_name": "Validating coverpage",
    "sub_task_name": None,
    "status": "finished",
    "message": "Coverpage link validated",
    "data": {
        "is_valid": True,
        "link_checked": "..."
    }
}

validate_home_info = {
    "layer": 1,
    "task_name": "Validating Journal home page info with provided info",
    "sub_task_name": None,
    "status": "finished",
    "message": "Homepage journal info matches the provided document",
    "data": {
        "match": True,
        "mismatches": []
    }
}

# LAYER 2

collect_and_validate_links = {
    "layer": 2,
    "task_name": "Collecting all the links from Home Page extract and validating it",
    "sub_task_name": None,
    "status": "finished",
    "message": "All article links collected and validated",
    "data": {
        "total_links": 20,
        "valid_links": 20,
        "invalid_links": []
    }
}

# LAYER 3 — ARTICLE 1

article1_html_scrape = {
    "layer": 3,
    "task_name": "Scraping Article info from html page and pdf and checking consistency",
    "sub_task_name": "Scraping Article1 from html",
    "status": "finished",
    "message": "Article1 HTML content scraped",
    "data": {"title": "...", "authors": [...], "journal": "..."}
}

article1_pdf_scrape = {
    "layer": 3,
    "task_name": "Scraping Article info from html page and pdf and checking consistency",
    "sub_task_name": "Scraping Article1 from pdf",
    "status": "finished",
    "message": "Article1 PDF content scraped",
    "data": {"title": "...", "authors": [...], "journal": "..."}
}

article1_consistency_check = {
    "layer": 3,
    "task_name": "Scraping Article info from html page and pdf and checking consistency",
    "sub_task_name": "Validating consistency",
    "status": "finished",
    "message": "Consistency validated for Article1",
    "data": {
        "title_match": True,
        "authors_match": True,
        "journal_info_match": True
    }
}

article1_open_access_check = {
    "layer": 3,
    "task_name": "Scraping Article info from html page and pdf and checking consistency",
    "sub_task_name": "Validating Open access icons and associated-link",
    "status": "finished",
    "message": "Open access icon and link validated for Article1",
    "data": {"icon_present": True, "link_valid": True}
}

article1_supplementary_check = {
    "layer": 3,
    "task_name": "Scraping Article info from html page and pdf and checking consistency",
    "sub_task_name": "Validating Supplimentry digital content",
    "status": "finished",
    "message": "Supplementary content links validated for Article1",
    "data": {"supplementary_links": [...], "all_valid": True}
}

# LAYER 3 — ARTICLE 2

article2_html_scrape = {
    "layer": 3,
    "task_name": "Scraping Article info from html page and pdf and checking consistency",
    "sub_task_name": "Scraping Article2 from html",
    "status": "finished",
    "message": "Article2 HTML content scraped",
    "data": {"title": "...", "authors": [...], "journal": "..."}
}

article2_pdf_scrape = {
    "layer": 3,
    "task_name": "Scraping Article info from html page and pdf and checking consistency",
    "sub_task_name": "Scraping Article2 from pdf",
    "status": "finished",
    "message": "Article2 PDF content scraped",
    "data": {"title": "...", "authors": [...], "journal": "..."}
}

article2_consistency_check = {
    "layer": 3,
    "task_name": "Scraping Article info from html page and pdf and checking consistency",
    "sub_task_name": "Validating consistency",
    "status": "finished",
    "message": "Consistency validated for Article2",
    "data": {
        "title_match": True,
        "authors_match": True,
        "journal_info_match": True
    }
}

article2_open_access_check = {
    "layer": 3,
    "task_name": "Scraping Article info from html page and pdf and checking consistency",
    "sub_task_name": "Validating Open access icons and associated-link",
    "status": "finished",
    "message": "Open access icon and link validated for Article2",
    "data": {"icon_present": True, "link_valid": True}
}

article2_supplementary_check = {
    "layer": 3,
    "task_name": "Scraping Article info from html page and pdf and checking consistency",
    "sub_task_name": "Validating Supplimentry digital content",
    "status": "finished",
    "message": "Supplementary content links validated for Article2",
    "data": {"supplementary_links": [...], "all_valid": True}
}

# LAYER 3 — FINAL REPORT

final_report_prep = {
    "layer": 3,
    "task_name": "Preparing report and presenting",
    "sub_task_name": None,
    "status": "finished",
    "message": "Final validation report generated",
    "data": {
        "summary": {
            "total_articles": 2,
            "consistency_passed": 2,
            "open_access_valid": 2,
            "supplementary_valid": 2
        }
    }
}
