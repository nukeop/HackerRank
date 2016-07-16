use std::io;

fn str_to_int(s: &str) -> i32 {
    let sopt: Option<i32> = s.trim().parse::<i32>().ok();
    match sopt{
        Some(x) => x,
        None => {
            panic!("Not a number");
        }
    }
}

fn str_to_int_vec(s: &str) -> Vec<i32>{
    s.split(' ')
        .map(str_to_int)
        .collect()
}

fn main() {
    let mut n = String::new();
    let mut clouds = String::new();

    io::stdin().read_line(&mut n).ok().expect("read error");
    io::stdin().read_line(&mut clouds).ok().expect("read error");

    let n = str_to_int(&n);
    let clouds = str_to_int_vec(&clouds);

    let mut total = -1;
    let mut index = 0;
    loop{
        if index<n-2 && clouds[(index+2) as usize]==0{
            index+=1;
        }
        total+=1;
        index+=1;

        if index>=n{
            break;
        }
    }
    println!("{}", total);
}
