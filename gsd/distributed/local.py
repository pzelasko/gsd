from concurrent.futures import ProcessPoolExecutor


def run_jobs(
        fn,
        inputs,
        jobs=1,
        **kwargs
):
    with ProcessPoolExecutor(jobs) as ex:
        return list(ex.map(fn, inputs))
