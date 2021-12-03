[export: 'add']
fn add(x int, y int) int {
	return x + y
}

[export: 'echo']
fn echo(text string) string {
    return text
}

fn main() {
	print("hello")
}