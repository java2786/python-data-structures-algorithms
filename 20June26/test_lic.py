from lic_branch import LICPolicy

policy = LICPolicy("Ramesh")
print(policy)

# print(f"Name: {policy.__holder_name}")
# print(f"Validity: {policy.__validity}")
# print(f"Sum Assured: {policy.__sum_assured}")

policy.__holder_name = "Dinesh"
policy.display()

policy.set_validity(5)
policy.display()

policy.set_validity(12)
policy.display()

