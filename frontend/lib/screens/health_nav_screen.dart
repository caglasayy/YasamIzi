import 'package:flutter/material.dart';

class HealthNavScreen extends StatelessWidget {
  const HealthNavScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Acil Durum & Navigasyon'),
      ),
      body: const Center(
        child: Text('Sağlık Navigasyonu (Eczaneler/Hastaneler)'),
      ),
    );
  }
}
