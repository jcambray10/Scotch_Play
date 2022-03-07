// get unique values for desired columns
// {2: ["Wisconsin", "Illinois", "Minnesota", "Mississippi", "Missouri", "Montana", "Michigan"], 3 : ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]}

function getuniquevaluesfromcolumn() {
    var unique_col_values_dict = {};

    allFilters = document.querySelectorAll(".table-filter")
    allFilters.forEach((filter_i) => {
        col_index = filter_i.parentElement.getAttribute("col_index").innerHTML;
        // 
        const rows = document.querySelectorAll("#table table-dark > tbody > tr")

        rows.forEach((row) => {
            cell_value = (row.querySelector("td:nth-child("+col_index+")").innerHTML);
            // if the col index is already present in the dict
            if (col_index in unique_col_values_dict){

                if  (unique_col_values_dict[col_index].includes(cell_value)) {
                    //alert(cell_value + "is already present in the array : " + unique_col_values_dict[col_index])
                } else {
                    unique_col_values_dict[col_index].push(cell_value)
                    //alert("Array after adding the cell value : " + unique_col_values_dict[col_index])

                }

            } else {
                unique_col_values_dict[col_index] = new Array(cell_value)
            }

        });
    
    });

    for(i in unique_col_values_dict) {
        // alert("Column index : " + i + " has Unique values : \n" + unique_col_values_dict[i]);
    }

    updateSelectOptions(unique_col_values_dict)
};
// add <option> tags to desired columns based on unique values
function updateSelectOptions(unique_col_values_dict) {
    allFilters = document.querySelectorAll(".table-filter");

    allFilters.forEach((filter_i) => {
        col_index = filter_i.parentElement.getAttribute('col-index')
        
        unique_col_values_dict[col_index].forEach((i) => {
            filter_i.innerHTML = filter_i.innnerHTML + `\n<option value="${i}</option>`
        });
        
    })
}
// create filter_rows() function

// filter_value_dict {2 : Value selected, 3}

function filter_rows() {
    allFilters = document.querySelectorAll(".table-filter")
    var filter_value_dict = {};
    
    allFilters.forEach((filter_i) => {
        col_index = filter_i.parentElement.getAttribute('col-index')
        col_cell_value_dict[col_index] = row.querySelector("td:nth-child(" + col_index+ ")").innerHTML
    })

    for (var col_i in filter_value_dict) {
        filter_value = filter_value_dict[col_i]
        row_cell_value = col_cell_value_dict[col_i]

        if (row_cell_value.indexOf(filter_value) == -1 && filter_value != "all") {
            dispaly_row = false;
            break;
        }
    }

    if (dispaly_row == true) {
        row.style.display = "table-row"

    } else {
        row.style.display = "none"
        
    }
}