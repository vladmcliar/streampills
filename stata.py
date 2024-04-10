import streamlit as st

# Заголовок приложения
st.title('Демо веб-приложения для сбора статы командами AI-Support.')
st.markdown('Служит для автоматизированного подсчёта ЧИА, ЧИЗЗ, ЧИКЗ, метрик интент-аналитиков, СХ и разработчиков и отправки данных в DWH для того, чтобы наши отчёты по метрикам эффективности тянули')
# Функция для отображения содержимого в теле приложения
def display_content(content):
    if content == 'Data task':
        st.header('Data task')
        st.write('Тут считаем метрики интент-аналитиков и профит')
    elif content == 'Procedure':
        st.header('Procedure')
        st.write('Тут можно считать отвалы и подводит результаты аб')
    elif content == 'Monitoring':
        st.header('Monitoring')
        st.write('Тут итоги мониторингов. Отправляем данные в DWH чтобы отчёты тянули это всё')

# Левая панель с заголовком "Тип задач" и кнопками
st.sidebar.title('Тип задач')
if st.sidebar.button('Data task'):
    display_content('Data task')
if st.sidebar.button('Procedure'):
    display_content('Procedure')
if st.sidebar.button('Monitoring'):
    display_content('Monitoring')

# Тело приложения
st.header('Ввод данных')

# Добавление поля ввода для даты начала теста
start_date = st.date_input('Дата начала теста')

# Добавление поля ввода для даты окончания теста
end_date = st.date_input('Дата окончания теста')

# Добавление выпадающего списка для выбора ключа интента
if 'Procedure' in st.session_state:
    intent_key_label = 'Ключ процедуры'
else:
    intent_key_label = 'Ключ интента'

intent_key_options = ('Ключ 1', 'Ключ 2', 'Ключ 3') if 'Procedure' not in st.session_state else ('Ключ процедуры',)
intent_key = st.selectbox(f'Выберите {intent_key_label}', intent_key_options)

# Добавление поля ввода текста для ключа задачи в Jira
jira_key = st.text_input('Введите ключ задачи в Jira')

# Добавление кнопки
button_clicked = st.button('Нажмите для отправки')

# Если кнопка была нажата, отобразить сообщение с выбранными данными
if button_clicked:
    st.write('Дата начала теста:', start_date)
    st.write('Дата окончания теста:', end_date)
    st.write(f'{intent_key_label}:', intent_key)
    st.write('Ключ задачи в Jira:', jira_key)
