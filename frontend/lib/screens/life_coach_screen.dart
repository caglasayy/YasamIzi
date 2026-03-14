import 'package:flutter/material.dart';

class LifeCoachScreen extends StatelessWidget {
  const LifeCoachScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Yaşam Koçu'),
      ),
      body: const Center(
        child: Text('Yaşam Koçu (DoğaReçetem & Wellness)'),
      ),
    );
  }
}
