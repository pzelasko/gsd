def run_jobs(fn, inputs, backend='local', jobs=1, **kwargs):
    if backend == 'local':
        from gsd.distributed.local import run_jobs
    if backend == 'sge':
        from gsd.distributed.sge import run_jobs
    else:
        raise ValueError(f"Unexpected distributed backend type: '{backend}'")
    return run_jobs(fn, inputs, jobs=jobs, **kwargs)
