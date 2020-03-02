from dask_jobqueue import SGECluster
from dask.distributed import Client


def run_jobs(
        fn,
        inputs,
        jobs=1,
        memory='1GB',
        timeout_s='600',
        queue='all.q',
        proc_per_worker=1,
        cores_per_proc=1,
        env_extra=None,
        **kwargs
):
    if env_extra is None:
        env_extra = []
    with SGECluster(
            queue=queue,
            walltime=timeout_s,
            processes=proc_per_worker,
            memory=memory,
            cores=cores_per_proc,
            env_extra=env_extra  # e.g. ['export ENV_VARIABLE="SOMETHING"', 'source myscript.sh']
    ) as cluster:
        with Client(cluster) as client:
            cluster.scale(jobs)
            futures = client.map(fn, inputs)
            results = client.gather(futures)
    return results
