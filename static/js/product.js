async function addProductAJAX(event) {
  event.preventDefault();

  const form = event.target;
  const formData = new FormData(form);

  try {
    const response = await fetch(PRODUCT_ADD_ENDPOINT, {
      method: "POST",
      headers: {
        "X-CSRFToken": formData.get("csrfmiddlewaretoken"),
      },
      body: formData,
    });

    if (!response.ok) throw new Error("Failed to add product");
    const data = await response.json();

    document.getElementById("createModal").classList.add("hidden");
    form.reset();

    if (window.showToast) showToast("Product Added!", `${data.name} berhasil ditambahkan 💕`);
    document.dispatchEvent(new Event("productAdded"));
  } catch (err) {
    console.error(err);
    if (window.showToast) showToast("Error", "Gagal menambahkan produk 😢");
  }
}

async function deleteProductAJAX(id) {
  if (!confirm("Yakin ingin menghapus produk ini?")) return;

  const url = PRODUCT_DELETE_ENDPOINT_BASE.replace("00000000-0000-0000-0000-000000000000", id);
  try {
    const response = await fetch(url, {
      method: "DELETE",
      headers: { "X-CSRFToken": getCookie("csrftoken") },
    });
    if (!response.ok) throw new Error("Failed to delete product");

    if (window.showToast) showToast("Product Deleted!", "Produk berhasil dihapus 🗑️");
    document.dispatchEvent(new Event("productDeleted"));
  } catch (err) {
    console.error(err);
    if (window.showToast) showToast("Error", "Gagal menghapus produk 😢");
  }
}

function openEditModal(product) {
  document.getElementById("edit-product-id").value = product.id;
  document.getElementById("edit-name").value = product.name;
  document.getElementById("edit-price").value = product.price;
  document.getElementById("edit-description").value = product.description;
  document.getElementById("editProductModal").classList.remove("hidden");
}

document.getElementById("cancelEditBtn").addEventListener("click", () => {
  document.getElementById("editProductModal").classList.add("hidden");
});

document.getElementById("editProductForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const productId = document.getElementById("edit-product-id").value;
  const formData = new FormData();
  formData.append("name", document.getElementById("edit-name").value);
  formData.append("price", document.getElementById("edit-price").value);
  formData.append("description", document.getElementById("edit-description").value);
  formData.append("csrfmiddlewaretoken", getCSRFToken());

  try {
    const response = await fetch(`/update-product-ajax/${productId}/`, {
      method: "POST",
      body: formData,
    });

    if (response.ok) {
      showToast("✅ Product updated successfully!");
      document.getElementById("editProductModal").classList.add("hidden");
      document.dispatchEvent(new Event("productUpdated"));
    } else {
      showToast("⚠️ Failed to update product");
    }
  } catch (error) {
    console.error("Error updating product:", error);
    showToast("❌ Error updating product");
  }
});

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

document.getElementById("createProductForm").addEventListener("submit", addProductAJAX);
