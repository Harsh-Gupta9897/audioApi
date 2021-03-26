from django.apps import apps


def get_instances_from_list_of_string(
        names_as_list_of_string: list, model_import_string: str
):
    """
    Given a list of strings which represent the `name` column in the models, this helper method will
    get the instances or create the instances with the corresponding name and will returns a list of instances.
    This is defined here to keep the code DRY and maintainable. `model_import_string` is the string used
    to import the model using `apps.get_model`. This is used to get the skills
    and languages dynamically on the serializer
    """

    # output instances
    instances = []

    # get or create the instances from the list
    for name in names_as_list_of_string:
        instance, _ = apps.get_model(model_import_string).objects.get_or_create(
            name=name
        )
        instances.append(instance)

    return instances


def get_instances_from_list_of_link(
        names_as_list_of_link: list, model_import_string: str, user_id: int
):
    """
    Given a list of strings which represent the `name` column in the models, this helper method will
    get the instances or create the instances with the corresponding name and will returns a list of instances.
    This is defined here to keep the code DRY and maintainable. `model_import_string` is the string used
    to import the model using `apps.get_model`. This is used to get the skills
    and languages dynamically on the serializer
    """

    # output instances
    instances = []

    # get or create the instances from the list
    for link in names_as_list_of_link:
        instance, _ = apps.get_model(model_import_string).objects.get_or_create(
                                                                                user_id=user_id,
                                                                                social_link=link
                                                                                )
        instances.append(instance)

    return instances

