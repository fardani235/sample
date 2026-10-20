
import pickle
import base64


def deserialize_data(encoded_data):

    decoded_data = base64.b64decode(encoded_data)

    user_data = pickle.loads(decoded_data)

    return user_data


if __name__ == "__main__":
    user_input = input("Enter serialized data: ")

    result = deserialize_data(user_input)

    print("Deserialized data:", result)
