import time
import progressbar


def trigger_function_every_x_seconds(interval, target_function):
    bar = progressbar.ProgressBar(maxval=interval)
    bar.start()

    seconds_passed = 0
    while True:
        time.sleep(1)
        seconds_passed += 1
        bar.update(seconds_passed)

        if seconds_passed >= interval:
            bar.finish()
            bar = progressbar.ProgressBar(maxval=interval)
            print('Timer is calling target function')
            target_function()
            print(f'Target function finished. Going to sleep for {interval} seconds')
            seconds_passed = 0
            bar.start()
