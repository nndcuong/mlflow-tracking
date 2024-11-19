import pymysql

def perm_delete_exp():
    connection = pymysql.connect(
        host='localhost',
        user='user',
        password='password',
        db='mlflow',
        cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        queries = """
            USE mlflow;
            DELETE FROM experiment_tags WHERE experiment_id=ANY(SELECT experiment_id FROM experiments where lifecycle_stage="deleted");
            DELETE FROM latest_metrics WHERE run_uuid=ANY(SELECT run_uuid FROM runs WHERE experiment_id=ANY(SELECT experiment_id FROM experiments where lifecycle_stage="deleted"));
            DELETE FROM metrics WHERE run_uuid=ANY(SELECT run_uuid FROM runs WHERE experiment_id=ANY(SELECT experiment_id FROM experiments where lifecycle_stage="deleted"));
            DELETE FROM tags WHERE run_uuid=ANY(SELECT run_uuid FROM runs WHERE experiment_id=ANY(SELECT experiment_id FROM experiments where lifecycle_stage="deleted"));
            DELETE FROM runs WHERE experiment_id=ANY(SELECT experiment_id FROM experiments where lifecycle_stage="deleted");
            DELETE FROM experiments where lifecycle_stage="deleted";
        """
        for query in queries.splitlines()[1:-1]:
            cursor.execute(query.strip())
    connection.commit()
    connection.close()