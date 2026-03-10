import 'package:flutter/material.dart';
import 'theme.dart';
import 'widgets/custom_card.dart';
import 'widgets/glass_card.dart';
import 'widgets/floating_icons_background.dart';
import 'widgets/glowing_add_button.dart';

void main() {
  runApp(const AkilliAboneApp());
}

class AkilliAboneApp extends StatelessWidget {
  const AkilliAboneApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Akıllı Abone',
      theme: AppTheme.lightTheme,
      home: const DashboardScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class DashboardScreen extends StatelessWidget {
  const DashboardScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          // Background layer with floating icons
          const Positioned.fill(
            child: FloatingIconsBackground(),
          ),

          // Foreground content
          SafeArea(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const SizedBox(height: 20),

                // Top section: Spending Summary (Glassmorphism)
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 20.0),
                  child: GlassCard(
                    width: double.infinity,
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          'Aylık Harcama Özeti',
                          style: TextStyle(
                            fontSize: 16,
                            color: AppTheme.textColor.withValues(alpha: 0.8),
                          ),
                        ),
                        const SizedBox(height: 10),
                        const Text(
                          '₺ 12,450.00',
                          style: TextStyle(
                            fontSize: 32,
                            fontWeight: FontWeight.bold,
                            color: AppTheme.textColor,
                          ),
                        ),
                        const SizedBox(height: 5),
                        Row(
                          children: [
                            Icon(Icons.arrow_upward, color: Colors.red[400], size: 16),
                            const SizedBox(width: 4),
                            Text(
                              '%4 geçen aya göre artış',
                              style: TextStyle(
                                fontSize: 12,
                                color: Colors.red[400],
                              ),
                            ),
                          ],
                        ),
                      ],
                    ),
                  ),
                ),

                const SizedBox(height: 40),

                // Middle section: Upcoming Payments
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 20.0),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      const Text(
                        'Yaklaşan Ödemeler',
                        style: TextStyle(
                          fontSize: 20,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      TextButton(
                        onPressed: () {},
                        child: const Text(
                          'Tümü',
                          style: TextStyle(color: AppTheme.primaryColor),
                        ),
                      ),
                    ],
                  ),
                ),

                const SizedBox(height: 10),

                // Horizontally scrollable Neumorphic Cards
                SizedBox(
                  height: 160,
                  child: ListView.builder(
                    scrollDirection: Axis.horizontal,
                    padding: const EdgeInsets.symmetric(horizontal: 10.0),
                    itemCount: 3,
                    itemBuilder: (context, index) {
                      final items = [
                        {'title': 'Netflix', 'amount': '₺ 149.99', 'date': 'Yarın', 'icon': Icons.movie},
                        {'title': 'Elektrik Faturası', 'amount': '₺ 850.00', 'date': '3 Gün Sonra', 'icon': Icons.electrical_services},
                        {'title': 'Spor Salonu', 'amount': '₺ 600.00', 'date': '5 Gün Sonra', 'icon': Icons.fitness_center},
                      ];

                      return Padding(
                        padding: const EdgeInsets.symmetric(horizontal: 10.0, vertical: 10.0), // padding for shadow
                        child: CustomCard(
                          width: 140,
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Container(
                                padding: const EdgeInsets.all(8),
                                decoration: BoxDecoration(
                                  color: AppTheme.primaryColor.withValues(alpha: 0.1),
                                  shape: BoxShape.circle,
                                ),
                                child: Icon(
                                  items[index]['icon'] as IconData,
                                  color: AppTheme.primaryColor,
                                ),
                              ),
                              const Spacer(),
                              Text(
                                items[index]['title'] as String,
                                style: const TextStyle(
                                  fontWeight: FontWeight.bold,
                                  fontSize: 14,
                                ),
                                maxLines: 1,
                                overflow: TextOverflow.ellipsis,
                              ),
                              const SizedBox(height: 4),
                              Text(
                                items[index]['amount'] as String,
                                style: TextStyle(
                                  color: AppTheme.textColor.withValues(alpha: 0.6),
                                  fontSize: 13,
                                ),
                              ),
                              const SizedBox(height: 4),
                              Text(
                                items[index]['date'] as String,
                                style: const TextStyle(
                                  color: Colors.redAccent,
                                  fontSize: 12,
                                  fontWeight: FontWeight.w500,
                                ),
                              ),
                            ],
                          ),
                        ),
                      );
                    },
                  ),
                ),
              ],
            ),
          ),
        ],
      ),

      // Bottom Navigation & Floating Action Button setup
      floatingActionButton: GlowingAddButton(
        onPressed: () {
          // Action for adding new item
        },
      ),
      floatingActionButtonLocation: FloatingActionButtonLocation.centerDocked,
      bottomNavigationBar: BottomAppBar(
        shape: const CircularNotchedRectangle(),
        notchMargin: 8.0,
        color: Colors.white,
        child: SizedBox(
          height: 60.0,
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: [
              IconButton(
                icon: const Icon(Icons.home, size: 28),
                color: AppTheme.primaryColor,
                onPressed: () {},
              ),
              IconButton(
                icon: const Icon(Icons.bar_chart, size: 28),
                color: Colors.grey,
                onPressed: () {},
              ),
              const SizedBox(width: 48), // Empty space for FAB
              IconButton(
                icon: const Icon(Icons.account_balance_wallet, size: 28),
                color: Colors.grey,
                onPressed: () {},
              ),
              IconButton(
                icon: const Icon(Icons.person, size: 28),
                color: Colors.grey,
                onPressed: () {},
              ),
            ],
          ),
        ),
      ),
    );
  }
}
