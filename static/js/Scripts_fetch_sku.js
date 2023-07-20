
function searchSKU() {
    var skuInput = $('#skuInput');
    var sku = skuInput.val();
    var skuDropdown = $('#sku');

    if (sku.length > 0) {
        skuDropdown.empty(); // Clear existing options
        // $('#sku').val(product.sku);
        //  $('#productName').val(product.name);
        $.ajax({
            url: '/fetch_sku/',
            data: { sku: sku },
            dataType: 'json',
            success: function (response) {
                if (response.length > 0) {
                    skuDropdown.empty(); // Clear existing options
                    $.each(response, function (index, product) {
                        var optionValue = product.sku + '   :   ' + product.name;
                        skuDropdown.append($('<option>', {
                            value: optionValue,
                            text: optionValue
                        }));
                    });
                    skuDropdown.show();
                    filterOptions();
                    // Add the "Select Option" option
                    skuDropdown.append($('<option>', {
                        value: 'Clear',
                        text: 'Clear'
                    }));
                    expandCombobox();
                } else {
                    skuDropdown.hide();
                }
            },
            error: function (xhr, textStatus, error) {
                // Handle error case
            }
        });
    } else {
        skuDropdown.hide();
    }
}

function filterOptions() {
    var input = document.getElementById("skuInput");
    var filter = input.value.toUpperCase();
    var select = document.getElementById("sku");
    var options = select.getElementsByTagName("option");
    var hasOptions = false;

    for (var i = 0; i < options.length; i++) {
        var option = options[i];
        if (option.text.toUpperCase().indexOf(filter) > -1) {
            option.style.display = "";
            hasOptions = true;
        } else {
            option.style.display = "none";
        }
    }

    select.style.display = hasOptions ? "" : "none";
}

function expandCombobox() {
    var select = document.getElementById("sku");
    if (select.options.length > 0) {
        select.style.display = "";
        select.size = select.options.length;
    }
}

function collapseCombobox() {
    var select = document.getElementById("sku");
    select.style.display = "none";
    select.size = 1;
}
function updateFields() {
    var selectedSKU = document.getElementById("sku").value;
    var values = selectedSKU.split('   :   ');
    var selectedSku = values[0];
    var selectedName = values[1];

    if (selectedSku != 'Clear') {
        document.getElementById("skuInput").value = selectedSku;
        document.getElementById("productName").value = selectedName;

        var skuInput = document.getElementById("skuInput");
        var productName = document.getElementById("productName");

        skuInput.disabled = true;
        productName.disabled = true;
    }
    else {
        clearFields();
    }
}

function clearFields() {
    var skuInput = document.getElementById("skuInput");
    var productName = document.getElementById("productName");

    skuInput.value = "";
    productName.value = "";

    skuInput.disabled = false;
    productName.disabled = false;
}