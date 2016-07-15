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
    let mut a = String::new();
    let mut b = String::new();
    io::stdin().read_line(&mut a).ok().expect("read error");
    io::stdin().read_line(&mut b).ok().expect("read error");
    let a = str_to_int_vec(&a);
    let b = str_to_int_vec(&b);
    let mut scorea = 0;
    let mut scoreb = 0;

    for i in 0..3{
        if a[i]>b[i] {
            scorea += 1;
        } else if a[i]<b[i] {
            scoreb += 1;
        }
    }

    println!("{} {}", scorea, scoreb);
}
