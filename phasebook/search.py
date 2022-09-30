from flask import Blueprint, request

from .data.search_data import USERS

bp = Blueprint("search", __name__, url_prefix="/search")

@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200

def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """
    output = []
    if "id" in args:
        for x in USERS:
            if x["id"] == args["id"]:
                output.append(x)
    if "name" in args:
        for x in USERS:
            if args["name"].lower() in x["name"].lower():
                output.append(x)
    if "age" in args:
        for x in USERS:
            if (x["age"] == int(args["age"]) or x["age"] == int(args["age"])-1 or x["age"] == int(args["age"])+1) and x not in output:
                output.append(x)
    if "occupation" in args:
        for x in USERS:
            if  args["occupation"].lower() in x["occupation"].lower():
                output.append(x)

    return output

