import streamlit as st

# Заголовок приложения
st.title('Демо веб-приложения для сбора статы командами AI-Support.')
st.markdown('Служит для автоматизированного подсчёта ЧИА, ЧИЗЗ, ЧИКЗ, метрик интент-аналитиков, СХ и разработчиков и отправки данных в DWH для того, чтобы наши отчёты по метрикам эффективности тянули')
st.write('Для начала работы выбери тип задачи слева')

intent_key_options = ('Ключ 1', 'Ключ 2', 'Ключ 3') if 'Procedure' not in st.session_state else ('Ключ процедуры',)
bl_options = ('Семейный банк', 'Кредитки','Дебетовки')
channel_options = ('Желтое приложение', 'Мобайл', 'HR', 'SME', 'Invest')

# Функция для отображения полей для ввода в зависимости от выбранной кнопки
def display_input_fields(content):
    if content == 'Data task':
        st.title('Интент-аналитик')
        ch_name = st.selectbox(f'Выберите канал', channel_options)
        b_line = st.selectbox(f'Выберите бизнес-линию', bl_options)
        start_date = st.date_input('Дата начала теста')
        end_date = st.date_input('Дата окончания теста')
        intent_key = st.selectbox(f'Выберите интент', intent_key_options)
        jira_key = st.text_input('Введите ключ задачи в Jira')
        send_data = st.button('Отправить данные')
    elif content == 'Procedure':
        st.title('Разработчик сценариев')
        ch_name = st.selectbox(f'Выберите канал', channel_options)
        b_line = st.selectbox(f'Выберите бизнес-лнию', bl_options)
        proc_key_label = st.text_input(f'Введите ключ процедуры')
        start_date = st.date_input('Дата начала теста')
        end_date = st.date_input('Дата окончания теста')
        send_data = st.button('Отправить данные')
    elif content == 'Monitoring':
        st.title('Аналитик клиентского опыта')
        ch_name = st.selectbox(f'Выберите канал', channel_options)
        b_line = st.selectbox(f'Выберите бизнес-лнию', bl_options)
        start_date = st.date_input('Дата начала теста')
        end_date = st.date_input('Дата окончания теста')
        intent_key = st.selectbox(f'Выберите интент', intent_key_options)
        proc_key_label = st.text_input(f'Введите ключ процедуры')
        send_data = st.button('Отправить данные')
    elif content == 'Admin':
        st.title('Панель администратора')
        st.write('Тут можно изменить коэффициенты ЧИА, ЧИКЗ, ЧИЗЗ')
        b_line = st.selectbox(f'Выберите бизнес-лнию', bl_options)
        kfc = st.text_input('Коэффициент')
        send_data = st.button('Отправить данные')

# Левая панель с заголовком "Меню" и кнопками
st.sidebar.title('Меню')
selected_content = st.sidebar.button('Data task')
if selected_content:
    display_input_fields('Data task')

selected_content = st.sidebar.button('Procedure')
if selected_content:
    display_input_fields('Procedure')

selected_content = st.sidebar.button('Monitoring')
if selected_content:
    display_input_fields('Monitoring')

selected_content = st.sidebar.button('Admin')
if selected_content:
    display_input_fields('Admin')
