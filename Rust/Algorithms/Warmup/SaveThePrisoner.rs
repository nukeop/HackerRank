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


fn main(){
    let mut t = String::new();

    io::stdin().read_line(&mut t).ok().expect("read error");
    let tint = str_to_int(&t);

    for _ in 0..tint{

        let mut nms = String::new();
        io::stdin().read_line(&mut nms).ok().expect("read error");

        let vec = str_to_int_vec(&nms);

        let (n, m, s) = (vec[0], vec[1], vec[2]);

        println!("{}", ((m+s-2) % n) + 1);
    }
}
