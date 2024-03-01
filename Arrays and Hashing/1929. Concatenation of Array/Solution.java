class Solution {
  public int[] getConcatenation(int[] nums) {
      int newLength = nums.length ; // initialize it here so that you don't have to run it once every time in the for loop
      int[] newArray = new int[newLength * 2];
      for(int i = 0; i < newLength; i++) {
          newArray[i] = nums[i];
          newArray[i + newLength] = nums[i];
      }
      // other solutions put System.gc(); here, which I believe reduces the memory taken up before submission
      return newArray;
  }
}