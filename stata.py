import streamlit as st

class WebApp:
    def __init__(self):
        if 'intent_key_options' not in st.session_state:
            st.session_state.intent_key_options = ('Ключ 1', 'Ключ 2', 'Ключ 3')
        else:
            st.session_state.intent_key_options = ('Ключ процедуры',)

        if 'bl_options' not in st.session_state:
            st.session_state.bl_options = ('Семейный банк', 'Кредитки', 'Дебетовки')

        if 'channel_options' not in st.session_state:
            st.session_state.channel_options = ('Желтое приложение', 'Мобайл', 'HR', 'SME', 'Invest')

    def display_input_fields(self, content):
        if content == 'Data task':
            self.display_data_task()
        elif content == 'Procedure':
            self.display_procedure()
        elif content == 'Monitoring':
            self.display_monitoring()
        elif content == 'Admin':
            self.display_admin()

    def display_data_task(self):
        st.title('Интент-аналитик')
        ch_name = st.selectbox(f'Выберите канал', st.session_state.channel_options, key='channel_data_task')
        b_line = st.selectbox(f'Выберите бизнес-линию', st.session_state.bl_options, key='business_line_data_task')
        start_date = st.date_input('Дата начала теста', key='start_date_data_task', value=st.session_state.get('start_date_data_task', None))
        end_date = st.date_input('Дата окончания теста', key='end_date_data_task', value=st.session_state.get('end_date_data_task', None))
        intent_key = st.selectbox(f'Выберите интент', st.session_state.intent_key_options, key='intent_key_data_task')
        jira_key = st.text_input('Введите ключ задачи в Jira', key='jira_key_data_task', value=st.session_state.get('jira_key_data_task', ''))
        self.display_send_button()

    def display_procedure(self):
        st.title('Разработчик сценариев')
        ch_name = st.selectbox(f'Выберите канал', st.session_state.channel_options, key='channel_procedure')
        b_line = st.selectbox(f'Выберите бизнес-линию', st.session_state.bl_options, key='business_line_procedure')
        proc_key_label = st.text_input(f'Введите ключ процедуры', key='proc_key_label_procedure', value=st.session_state.get('proc_key_label_procedure', ''))
        start_date = st.date_input('Дата начала теста', key='start_date_procedure', value=st.session_state.get('start_date_procedure', None))
        end_date = st.date_input('Дата окончания теста', key='end_date_procedure', value=st.session_state.get('end_date_procedure', None))
        self.display_send_button()

    def display_monitoring(self):
        st.title('Аналитик CX')
        b_line = st.selectbox(f'Выберите бизнес-линию', st.session_state.bl_options, key='business_line_monitoring')
        start_date = st.date_input('Дата начала теста', key='start_date_monitoring', value=st.session_state.get('start_date_monitoring', None))
        end_date = st.date_input('Дата окончания теста', key='end_date_monitoring', value=st.session_state.get('end_date_monitoring', None))
        intent_key = st.selectbox(f'Выберите интент', st.session_state.intent_key_options, key='intent_key_monitoring')
        proc_key_label = st.text_input(f'Введите ключ процедуры', key='proc_key_label_monitoring', value=st.session_state.get('proc_key_label_monitoring', ''))
        self.display_send_button()

    def display_admin(self):
        st.title('Панель администратора')
        st.write('Тут можно изменить коэффициенты ЧИА, ЧИКЗ, ЧИЗЗ')
        b_line = st.selectbox(f'Выберите бизнес-линию', st.session_state.bl_options, key='business_line_admin')
        kfc = st.text_input('Коэффициент', key='kfc_admin', value=st.session_state.get('kfc_admin', ''))
        self.display_send_button()

    def display_send_button(self):
        send_data = st.button('Отправить данные', key='send_data_button')
        if send_data:
            st.write('Данные успешно отправлены')
            
def main():
    if 'web_app' not in st.session_state:
        st.session_state.web_app = WebApp()

    st.title('Демо веб-приложения для сбора статы командами AI-Support.')
    st.markdown('Служит для автоматизированного подсчёта ЧИА, ЧИЗЗ, ЧИКЗ, метрик интент-аналитиков, СХ и разработчиков и отправки данных в DWH для того, чтобы наши отчёты по метрикам эффективности тянули')
    st.write('Для начала работы выбери тип задачи слева')
    st.sidebar.title('Меню')
    selected_content = st.sidebar.radio('Выберите тип задачи', ('Data task', 'Procedure', 'Monitoring', 'Admin'))
    if st.sidebar.button('Открыть'):
        st.session_state.web_app.display_input_fields(selected_content)

if __name__ == "__main__":
    main()

