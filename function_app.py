import azure.functions as func
import logging


app = func.FunctionApp()


@app.timer_trigger(schedule="0 */1 * * * *", arg_name="func_users", run_on_startup=True,
                   use_monitor=False)
def rpp_function_trigger(my_timer: func.TimerRequest) -> None:
    if my_timer.past_due:
        logging.info('The timer is past due!')

    logging.info('Function executed successfully!')
