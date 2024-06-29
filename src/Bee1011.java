package src;


class Bee1011 {
    public static void main(String[] args) {
        int radius = Integer.parseInt(System.console().readLine());
        double result = (4.0/3) * 3.14159 * Math.pow(radius, 3);
        String formatted = String.format("%.3f", result);
        System.out.println(String.format("VOLUME = %s", formatted));
    }
}