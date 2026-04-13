def fusion(nums1, nums2):
    i = 0
    j = 0
    result = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1

    result.extend(nums1[i:])
    result.extend(nums2[j:])

    return result


nums1 = [1, 2, 3]
nums2 = [2, 5, 6]

print(fusion(nums1, nums2))
