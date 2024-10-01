document.addEventListener("DOMContentLoaded", function () {
  // Selecciona todas las celdas con la clase 'stock-cell'
  const stockCells = document.querySelectorAll(".stock-cell");

  stockCells.forEach(function (cell) {
    // Obtener el valor de 'data-stock' y convertirlo a número
    const stockActual = parseInt(cell.getAttribute("data-stock"));

    // Aplicar el color de fondo basado en el valor de 'stock_actual'
    if (stockActual <= 10) {
      cell.style.backgroundColor = "#D12923";
    } else if (stockActual < 50) {
      cell.style.backgroundColor = "#F8BD4F";
    } else if (stockActual > 50) {
      cell.style.backgroundColor = "#30B52C";
    }
  });
});
