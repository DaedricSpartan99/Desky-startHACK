
export async function advanced_search(filters) {

  var filter_map = structuredClone(filters);

  // replace date range 

  // remap status
  if (filters['status']) {

    filter_map['status'] = Object.entries(filters['status']).filter(([k, v]) => v === true);
    filter_map['status'] = Object.keys(Object.fromEntries(filter_map['status']))
  }

  // clean from null fields
  for (var prop in filter_map) {
    if (filter_map[prop] === null || filter_map[prop] === undefined) {
      delete filter_map[prop];
    }
  }

  // conclude GET request
  return fetch(process.env.REACT_APP_API_URL + 'advanced-search/?' + new URLSearchParams(filter_map).toString(), {
    method : 'GET',
    headers : { 
      "Accept" : "application/json"
    }
  });
}

export async function search(input) {

  var filter_map = {'keyword' : input};

  // conclude GET request
  return fetch(process.env.REACT_APP_API_URL + 'booking/search/?' + new URLSearchParams(filter_map).toString(), {
    method : 'GET',
    headers : { 
      "Accept" : "application/json"
    }
  });
}


/*
 *  Login and access
 */

export async function login(server, username, password) {
  return fetch(server + 'api/auth/login/', {
    method : 'POST',
    body : JSON.stringify({'username' : username, 'password' : password}),
    headers : { 
      "Content-Type" : "application/json",
      "Accept" : "application/json"
    }
  });
}


