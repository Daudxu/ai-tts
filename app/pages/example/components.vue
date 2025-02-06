<template>
	<view class="wrap">
		<page-nav :desc="desc" title="TTS 语音合成"></page-nav>

		<view class="container">
			<!-- 文本输入框 -->
			<input class="input-box" v-model="text" placeholder="请输入文本" />
			
			<!-- 按钮触发 TTS -->
			<button class="btn" @click="fetchTTS">播放语音</button>
		</view>

	</view>
</template>

<script>
	import list from "./components.config.js";

	export default {
		data() {
			return {
				list: list,
				text: "你好，欢迎使用语音合成！", // 默认文本
				audioSrc: "" // 存储音频 URL
			};
		},
		computed: {
			desc() {
				return this.$t('components.desc');
			}
		},
		onShow() {
			uni.setNavigationBarTitle({
				title: this.$t('nav.components')
			});
		},
		methods: {
			    async fetchTTS() {
			        if (!this.text.trim()) {
			            uni.showToast({ title: "请输入文本", icon: "none" });
			            return;
			        }
			        
			        uni.showLoading({ title: "正在生成语音..." });
			 
			        try {
			            const res = await uni.request({
			                url: "http://127.0.0.1:8000/tts", // 确保这是正确的服务器地址
			                method: "POST",
			                header: { "Content-Type": "application/json" },
			                data: { text: this.text }
			            });
			 
			            uni.hideLoading();
			            
			            if (res[1].statusCode === 200 && res[1].data ) {
			                const audioData = res[1].data;
			                this.playAudio(audioData);
			            } else {
			                uni.showToast({ title: "语音生成失败或数据不完整", icon: "none" });
			            }
			        } catch (err) {
			            uni.hideLoading();
			            uni.showToast({ title: "请求失败", icon: "none" });
			            console.error("TTS 请求错误:", err);
			        }
			    },
			    playAudio(base64Audio) {
			        const audioContext = uni.createInnerAudioContext();
			        audioContext.src = `data:audio/wav;base64,${base64Audio}`; // 确保音频是 WAV 格式
			        audioContext.onPlay(() => {
			            console.log('Playing audio...');
			        });
			        audioContext.onError((err) => {
			            console.error('Audio error:', err); // 更简单的错误打印
			            if (err && err.errMsg) {
			                console.error('Detailed error:', err.errMsg);
			            }
			        });
			        audioContext.play();
			    }
		}
	};
</script>

<style lang="scss" scoped>
.container {
	display: flex;
	flex-direction: column;
	align-items: center;
	padding: 20px;
}

.input-box {
	width: 80%;
	height: 40px;
	padding: 10px;
	border: 1px solid #ccc;
	border-radius: 5px;
	margin-bottom: 15px;
}

.btn {
	background-color: #007aff;
	color: white;
	padding: 10px 20px;
	border-radius: 5px;
	font-size: 16px;
}
</style>



