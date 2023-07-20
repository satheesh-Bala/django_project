function toggleOtherCategory(value) {
    var otherCategoryContainer = document.getElementById("otherCategoryContainer");
    if (value === "Other") {
        otherCategoryContainer.style.display = "block";
    } else {
        otherCategoryContainer.style.display = "none";
    }
}
