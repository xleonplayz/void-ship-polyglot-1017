use std::io::{self,Read};
fn main(){let mut raw=String::new();let _=io::stdin().read_to_string(&mut raw);if raw.contains("/health"){println!("{{\"ok\":true,\"service\":\"ledger\"}}")}else{println!("{{\"entries\":[{{\"id\":\"a\",\"amount\":1200}},{{\"id\":\"b\",\"amount\":800}}]}}")}}
