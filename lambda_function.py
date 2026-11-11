def lambda_handler(event, context):
    request_id = random.randint(1000, 9999)
    # 処理の開始をログに出力する
    print(f"処理を開始しました。リクエストID: {request_id}")
    print("何らかの処理をしています...")
    # 処理の完了をログに出力する
    print(f"処理が完了しました。リクエストID: {request_id}")
    return {"requestId": request_id}