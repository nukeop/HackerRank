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

fn main()
{
    let mut line = String::new();
    io::stdin().read_line(&mut line).ok().expect("read error");

    let params = str_to_int_vec(&line);

    if ((params[2]-params[0])*(params[3]-params[1]) < 0 && (params[2]-params[0]) % (params[3]-params[1]) == 0){
        println!("YES");
    }
    else{
        println!("NO");
    }
}
