$("#products").DataTable({
  responsive: true,
  serverSide: true,
  processing: true,
  paging: true,
  ordering: false,
  ajax: {
    url: "http://localhost:8000/",
    data: (d) => ({
      draw: d.draw,
      start: d.start,
      length: d.length,
    }),
  },
  rowId: (p) => `p_${p.id}`,
  columns: [
    { data: "title" },
    { data: "description" },
    {
      data: "category",
      className: "product_category",
      createdCell: function (cell) {
        cell.addEventListener("click", showRowId);
      },
    },
    { data: "price" },
  ],
});

function showRowId() {
  console.log(this.parentElement.id);
}
