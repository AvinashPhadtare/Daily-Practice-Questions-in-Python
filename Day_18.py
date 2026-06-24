def parse_query_string(qs: str) -> dict:
    query = {}
    result = qs.split('&')
    
    for l in result:
        main_result = l.split("=")
        query[main_result[0]] = main_result[1]
        
    return query

def build_query_string(params: dict) -> str:
    items = params.items()
    query_part = [f"{key}={value}" for key, value in items]

    return "&".join(query_part)



# Example usage

example_query_string = "name=Avinash&age=22&plan=premium&city=Pune"

print(parse_query_string(example_query_string))     #  -> {'name': 'Avinash', 'age': '22', 'plan': 'premium', 'city': 'Pune'}
print(build_query_string(parse_query_string(example_query_string)))  #   -> "name=Avinash&age=22&plan=premium&city=Pune"
