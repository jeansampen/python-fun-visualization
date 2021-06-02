import time


def timeit(procedure):
    def timed(*args, **kw):
        if 'timed' in kw and kw['timed']:
            if 'procedure_name' in kw:
                procedure_name = kw['procedure_name']
            else:
                procedure_name = procedure.__name__
            log = print
            procedure_start_time = time.time()
            log('\n')
            log(f'--------------{procedure_name} START-----------------------')
            result = procedure(*args, **kw)
            log(f'--------------{procedure_name} END, EXEUCTION_TIME = {time.time() - procedure_start_time} seconds------------------')
            log('\n')
            return result
        else:
            return procedure(*args, **kw)
    return timed