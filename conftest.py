import pytest
import allure
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        record_video_dir="videos/", 
        record_video_size={"width": 1280, "height": 720}
    )
    page = context.new_page()
    page.goto("https://www.amazon.in")
    page.wait_for_load_state("domcontentloaded")
    yield page
    context.close()
    browser.close()
    p.stop()



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    # take screenshot ONLY when test fails
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

        if page.video:
            allure.attach.file(
                page.video.path(),
                name="Test Video",
                attachment_type=allure.attachment_type.WEBM
    )