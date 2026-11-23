import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10


def get_user(user_id):
    """მომხმარებლის მონაცემები მოაქვს API-დან; 404-ისას აბრუნებს None-ს."""
    response = requests.get(f"{BASE_URL}/users/{user_id}", timeout=TIMEOUT)

    if response.status_code == 404:
        return None

    # 500 და სხვა HTTP შეცდომები აქ HTTPError-ს გამოიწვევს.
    response.raise_for_status()
    return response.json()


def print_users():
    """ბეჭდავს მოთხოვნილ მომხმარებლებს ან შეტყობინებას, თუ ისინი არ არსებობს."""
    for user_id in (1, 2, 999):
        user = get_user(user_id)
        if user is None:
            print(f"მომხმარებელი {user_id} ვერ მოიძებნა")
        else:
            city = user["address"]["city"]
            print(f"{user['name']} | {user['email']} | {city}")


def crud_tour():
    """ასრულებს CREATE, READ, PUT, PATCH და DELETE მოთხოვნებს."""
    # CREATE
    new_post = {
        "title": "ახალი პოსტი",
        "body": "ტექსტი",
        "userId": 1,
    }
    create_response = requests.post(
        f"{BASE_URL}/posts", json=new_post, timeout=TIMEOUT
    )
    create_response.raise_for_status()
    created_post = create_response.json()
    post_id = created_post["id"]
    print(f"CREATE: {create_response.status_code}, id={post_id}")

    # READ: JSONPlaceholder შექმნილ ჩანაწერს რეალურად არ ინახავს, ამიტომ 404 მოსალოდნელია.
    read_response = requests.get(f"{BASE_URL}/posts/{post_id}", timeout=TIMEOUT)
    if read_response.status_code != 404:
        read_response.raise_for_status()
    print(f"READ {post_id}: {read_response.status_code}")

    # UPDATE (PUT): მთლიანი ობიექტის ჩანაცვლება.
    full_post = {
        "id": 1,
        "title": "სრულად შეცვლილი",
        "body": "სრული ტექსტი",
        "userId": 1,
    }
    put_response = requests.put(
        f"{BASE_URL}/posts/1", json=full_post, timeout=TIMEOUT
    )
    put_response.raise_for_status()
    put_result = put_response.json()
    print(
        f"UPDATE (PUT): {put_response.status_code}, "
        f"title={put_result['title']}"
    )

    # UPDATE (PATCH): მხოლოდ სათაურის შეცვლა.
    patch_response = requests.patch(
        f"{BASE_URL}/posts/1",
        json={"title": "ნაწილობრივ შეცვლილი"},
        timeout=TIMEOUT,
    )
    patch_response.raise_for_status()
    patch_result = patch_response.json()
    print(
        f"UPDATE (PATCH): {patch_response.status_code}, "
        f"title={patch_result['title']}"
    )

    # DELETE
    delete_response = requests.delete(f"{BASE_URL}/posts/1", timeout=TIMEOUT)
    delete_response.raise_for_status()
    print(f"DELETE: {delete_response.status_code}, {delete_response.json()}")


def main():
    print_users()
    crud_tour()


if __name__ == "__main__":
    main()
