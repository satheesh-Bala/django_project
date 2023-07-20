function updateFields() {
    var selectedSKU = document.getElementById("sku").value;
    var values = selectedSKU.split('   :   ');
    var selectedSku = values[0];
    var selectedName = values[1];

    document.getElementById("skuInput").value = selectedSku;
    alert(selectedSku);
    alert(selectedName);
    document.getElementById("productName").value = selectedName;
}