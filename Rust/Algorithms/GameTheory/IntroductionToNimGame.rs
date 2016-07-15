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
    let mut num_test_cases = String::new();
    io::stdin().read_line(&mut num_test_cases).ok().expect("read error");
    let num_test_cases = str_to_int(&num_test_cases);

    for _ in 0..num_test_cases{
        let mut piles = String::new();
        let mut numbers = String::new();
        io::stdin().read_line(&mut piles).ok().expect("read error");
        io::stdin().read_line(&mut numbers).ok().expect("read error");
        let numbers = str_to_int_vec(&numbers);

        let xor = numbers.iter().fold(0, |acc, x| acc^x);
        if xor==0{
            println!("Second");
        } else {
            println!("First");
        }
    }
}
