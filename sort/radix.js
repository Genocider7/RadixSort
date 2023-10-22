const order = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];

var array = [];
var operation_div;

function underline_at(text, where) {
  ret = '';
  for (key in text) {
    if (key == where) {
      ret += '<u>' + text[key] + '</u>';
    }
    else {
      ret += text[key];
    }
  }
  return ret;
}

function write_buckets(buckets, underline) {
  let temp = '[';
  let first_alpha = true;
  for (radix in order) {
    if (buckets[order[radix]].length == 0) {
      continue;
    }
    if (first_alpha) {
      first_alpha = false;
    }
    else {
      temp += ', ';
    }
    temp += '{';
    let first_beta = true;
    for (key in buckets[order[radix]]) {
      if (first_beta) {
        first_beta = false;
      }
      else {
        temp += ', ';
      }
      temp += underline_at(buckets[order[radix]][key], underline);
    }
    temp += '}';
  }
  temp += ']<br>'
  operation_div.innerHTML += temp;
} 

function join_buckets(buckets) {
  let ret = [];
  for (let key in order) {
    let radix = order[key];
    for (let key in buckets[radix]) {
      let el = buckets[radix][key];
      ret.push(el);
    }
  }
  return ret;
}

function createEmptyBuckets() {
  let ret = {};
  for (let key in order) {
    ret[order[key]] = [];
  }
  return ret;
}

function turnToStr(arr) {
  let ret = [];
  for (let key in arr) {
    ret.push(arr[key].toString());
  }
  return ret;
}

function get_biggest_length(arr) {
  let biggest = 0;
  for (let key in arr) {
    if (arr[key].length > biggest) {
      biggest = arr[key].length;
    }
  }
  return biggest;
}

function fill_array(arr, size) {
  let ret = [];
  for (let key in arr) {
    let temp = order[0].repeat(size - arr[key].length) + arr[key];
    ret.push(temp);
  }
  return ret;
}

function turnToInt(arr) {
  let ret = [];
  for (let key in arr) {
    ret.push(Number.parseInt(arr[key]));
  }
  return ret;
}

function sort(arr) {
  arr = turnToStr(arr);
  let size = get_biggest_length(arr);
  arr = fill_array(arr, size);

  for (let i = size - 1; i >= 0; i--) {
    let buckets = createEmptyBuckets();
    for (let key in arr) {
      let el = arr[key].split('');
      buckets[el[i]].push(arr[key]);
    }
    write_buckets(buckets, i);
    arr = join_buckets(buckets);
    operation_div.innerHTML += '[' + turnToInt(arr).join(', ') + ']<br>'
  }
  document.getElementById('results').innerHTML = '[' + turnToInt(arr).join(', ') + ']';
}

function parseArgs(text) {
  operation_div.innerHTML = '';
  let arr = text.replaceAll(".", ",").replaceAll(",", " ").split(' ');
  array = [];
  for (let key in arr) {
    if (arr[key] == '') {
      continue;
    }
    let temp = Number.parseInt(arr[key]);
    if (isNaN(temp)) {
      alert('Nie rozpoznano \"' + arr[key] + '\"');
      console.log(arr[key]);
      return false;
    }
    if (temp < 0) {
      alert(arr[key] + ' nie jest liczbą naturalną');
      console.log(arr[key]);
      return false;
    }
    array.push(temp);
  }
  if (array.length == 0) {
    return false;
  }
  operation_div.innerHTML += '[' + array.join(', ') + ']<br>';
  return true;
}

function Start() {
  operation_div = document.getElementById('operation-div');
  document.getElementById('input-button').addEventListener('click', () => {
    if (parseArgs(document.getElementById('input-array').value)) {
      console.log(sort(array));
    }
  });
}

document.addEventListener('DOMContentLoaded', Start);
