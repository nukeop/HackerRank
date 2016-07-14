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
    let vec = str_to_int_vec(&line);
    let (n, k) = (vec[0], vec[1]);

    line = String::new();
    io::stdin().read_line(&mut line).ok().expect("read error");
    let arr = str_to_int_vec(&line);

    let mut count = 0;
    for j in 0..n{
        for i in 0..j{
            if ((arr[i as usize] + arr[j as usize])%k) == 0{
                count+=1;
            }
        }
    }

    println!("{}", count);
}
