import 'dart:math';
import 'package:flutter/material.dart';

class FloatingIconsBackground extends StatefulWidget {
  const FloatingIconsBackground({Key? key}) : super(key: key);

  @override
  FloatingIconsBackgroundState createState() => FloatingIconsBackgroundState();
}

class FloatingIconsBackgroundState extends State<FloatingIconsBackground> with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  final int numberOfIcons = 15;
  final List<String> symbols = ['₺', '\$', '€', '₿'];
  late List<_FloatingIcon> _icons;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: const Duration(seconds: 20),
    )..repeat(); // Loop the animation continuously
  }

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    // Initialize icons once we know screen size
    final size = MediaQuery.of(context).size;
    _icons = List.generate(numberOfIcons, (index) => _FloatingIcon.random(size, symbols));
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: _controller,
      builder: (context, child) {
        final size = MediaQuery.of(context).size;
        for (var icon in _icons) {
          icon.update(size); // Move icons based on logic
        }

        return Stack(
          children: _icons.map((icon) {
            return Positioned(
              left: icon.x,
              top: icon.y,
              child: Opacity(
                opacity: icon.opacity,
                child: Text(
                  icon.symbol,
                  style: TextStyle(
                    fontSize: icon.size,
                    color: Colors.grey.withValues(alpha: 0.15),
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
            );
          }).toList(),
        );
      },
    );
  }
}

class _FloatingIcon {
  double x;
  double y;
  double speedX;
  double speedY;
  double size;
  double opacity;
  String symbol;

  _FloatingIcon({
    required this.x,
    required this.y,
    required this.speedX,
    required this.speedY,
    required this.size,
    required this.opacity,
    required this.symbol,
  });

  factory _FloatingIcon.random(Size screenSize, List<String> symbols) {
    final rand = Random();
    return _FloatingIcon(
      x: rand.nextDouble() * screenSize.width,
      y: rand.nextDouble() * screenSize.height,
      speedX: (rand.nextDouble() - 0.5) * 1, // small random speed
      speedY: (rand.nextDouble() - 0.5) * 1, // small random speed
      size: rand.nextDouble() * 30 + 20, // size between 20 and 50
      opacity: rand.nextDouble() * 0.4 + 0.1, // opacity between 0.1 and 0.5
      symbol: symbols[rand.nextInt(symbols.length)],
    );
  }

  void update(Size screenSize) {
    x += speedX;
    y += speedY;

    // Wrap around logic
    if (x < -size) x = screenSize.width;
    if (x > screenSize.width) x = -size;
    if (y < -size) y = screenSize.height;
    if (y > screenSize.height) y = -size;
  }
}
