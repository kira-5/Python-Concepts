

# sourcery skip: aug-assign, merge-assign-and-aug-assign
some_value = 5


# ? Normal  Assignment Operator
new_value_normal = 0
new_value_normal = new_value_normal + some_value
print(new_value_normal)


# ? Augmented Assignment Operator
new_value_argumented = 0
new_value_argumented += some_value
print(new_value_argumented)
