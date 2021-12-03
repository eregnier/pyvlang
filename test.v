[export: 'add']
fn add(x int, y int) int {
	return x + y
}

[export: 'echo']
fn echo(ctext &char) &char {
    mut s := unsafe { cstring_to_vstring(ctext) }
    /// do stuff with `s`
    return s.str
}

fn main() {
	print("hello")
}