import streamlit as st
from app_pages.multi_page import Multipage
from app_pages.page_calculator import calculator_body

app = Multipage(app_name = "Calculator App")

app.add_page("Calculator", calculator_body)

app.run()
