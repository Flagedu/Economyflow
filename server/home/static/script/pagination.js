function getAllUrlParams(url) {
    var queryString = url ? url.split('?')[1] : window.location.search.slice(1);
    var obj = {};
    if (queryString) {
        queryString = queryString.split('#')[0];

        var arr = queryString.split('&');

        for (var i = 0; i < arr.length; i++) {
        // separate the keys and the values
        var a = arr[i].split('=');

        // set parameter name and value (use 'true' if empty)
        var paramName = a[0];
        var paramValue = typeof (a[1]) === 'undefined' ? true : a[1];

        // (optional) keep case consistent
        paramName = paramName.toLowerCase();
        if (typeof paramValue === 'string') paramValue = paramValue.toLowerCase();

        // if the paramName ends with square brackets, e.g. colors[] or colors[2]
        if (paramName.match(/\[(\d+)?\]$/)) {

            // create key if it doesn't exist
            var key = paramName.replace(/\[(\d+)?\]/, '');
            if (!obj[key]) obj[key] = [];

            // if it's an indexed array e.g. colors[2]
            if (paramName.match(/\[\d+\]$/)) {
            // get the index value and add the entry at the appropriate position
            var index = /\[(\d+)\]/.exec(paramName)[1];
            obj[key][index] = paramValue;
            } else {
            // otherwise add the value to the end of the array
            obj[key].push(paramValue);
            }
        } else {
            // we're dealing with a string
            if (!obj[paramName]) {
            obj[paramName] = paramValue;
            } else if (obj[paramName] && typeof obj[paramName] === 'string'){
            obj[paramName] = [obj[paramName]];
            obj[paramName].push(paramValue);
            } else {
            obj[paramName].push(paramValue);
            }
        }
        }
    }

    return obj;
}


function set_url(url_obj){
    var new_url = "";
    counter = 1;
    length = Object.keys(url_obj).length;
    $.each(url_params, function(key, value){
        if(counter == length){
            new_url = new_url + key + "=" + value;
        }else{
            new_url = new_url + key + "=" + value + "&";
        }
        counter++;
    });

    host = HOST;
    path = PATH;
    host_path = host + path;
    final_url = "http://" + host_path + new_url;
    location.href = final_url;
}


function create_url_obj(field_name, filter_value){
    url_params = getAllUrlParams()

    if(!jQuery.isEmptyObject(url_params)){
        $.each(url_params, function(key, value){
            if(key == field_name){     
                list = value.split(",");
                new_list = [];
                list.forEach(function(item){
                    if(filter_value != item){
                        new_list.push(item);
                    }
                });
                new_list.push(filter_value);
                new_value = new_list.join(",");
                url_params[field_name] = new_value;
            }else{
                param_exists = field_name in url_params;
                if(param_exists){

                }else{
                    url_params[field_name] = filter_value;
                }
            }
        });

        //delete empty params
        check_val = field_name in url_params;
        if(!url_params[field_name]){
            delete url_params[field_name];
        }
        set_url(url_params);
    }else{
        url_params[field_name] = filter_value;

        //delete empty params
        check_val = field_name in url_params;
        if(!url_params[field_name]){
            delete url_params[field_name];
        }
        set_url(url_params);
    }
}


function remove_url_obj(field_name, filter_value){
    url_params = getAllUrlParams()
    $.each(url_params, function(key, value){
        if(key == field_name){
            list = value.split(",");
            new_list = [];
            list.forEach(function(item) {
                if(filter_value != item){
                    new_list.push(item);
                }
            });
            new_value = new_list.join(",");
            url_params[field_name] = new_value;

            //delete empty params
            check_val = field_name in url_params;
            if(!url_params[field_name]){
                delete url_params[field_name];
            }
            set_url(url_params)
        }
    });
}

function add_value_to_url_param(name, value){
    url_params = getAllUrlParams()
    url_params[name] = value
    
    //delete empty params
    check_val = name in url_params;
    if(!url_params[name]){
        delete url_params[name];
    }
    set_url(url_params);
}

function remove_url_object_from_url_params(name){
    url_params = getAllUrlParams();
    check_val = name in url_params;
    if(url_params[name]){

    }else{
        delete url_params[name];
        set_url(url_params);
    }
}

// multiple value pass to url params
function add_multi_value_to_url_param(obj){
    url_params = getAllUrlParams()
    $.each(obj, function(key, value){
        url_params[key] = value;
        check_val = key in url_params;
        if(!url_params[key]){
            delete url_params[key];
        }
    });
    set_url(url_params);
}