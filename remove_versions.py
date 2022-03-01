import boto3

client = boto3.client('lambda')


def get_functions():

    functions = []
    response = client.list_functions(
        MaxItems=50
    )

    functions.extend(response['Functions'])

    # ページング
    while True:
        if not response.get('NextMarker'):
            break

        marker = response['NextMarker']
        response = client.list_functions(
            Marker=marker,
            MaxItems=50
        )
        functions.extend(response['Functions'])

    return(functions)


def get_versions(functionname):

    versions = []
    response = client.list_versions_by_function(
        FunctionName=functionname,
        MaxItems=50
    )

    versions.extend(response['Versions'])

    # ページング
    while True:
        if not response.get('NextMarker'):
            break

        marker = response['NextMarker']
        response = client.list_versions_by_function(
            FunctionName=functionname,
            Marker=marker,
            MaxItems=50
        )
        versions.extend(response['Versions'])

    return(versions)


def handler():
    # Lambdaの一覧を取得
    functions = get_functions()

    for function in functions:
        # バージョンの一覧を取得
        versions = get_versions(function['FunctionName'])

        for version in versions:
            # LATESTは削除しない
            if version['Version'] == '$LATEST':
                continue
            # バージョン削除の実行
            client.delete_function(
                FunctionName=function['FunctionName'],
                Qualifier=version['Version']
            )


if __name__ == '__main__':
    handler()
