use std::io;
fn main() {
    let mut s2 = String::new();
    let mut s1 = String::new();
    io::stdin().read_line(&mut s1).ok().expect("read error");
    io::stdin().read_line(&mut s2).ok().expect("read error");
    let mut num_1 : i32 = s1.trim().parse().ok().expect("parse error");
    let mut num_2 : i32 = s2.trim().parse().ok().expect("parse error");
    println!("{}", num_1 + num_2);
}
